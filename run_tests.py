#!/usr/bin/env python3
"""
Script to run tests locally similar to CI pipeline
Based on .github/workflows/ci.yml

This script provides a Python alternative to run_tests.sh for better
cross-platform compatibility.
"""

import os
import subprocess
import sys
from pathlib import Path


class Colors:
    """ANSI color codes for terminal output"""

    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[1;33m"
    BLUE = "\033[0;34m"
    NC = "\033[0m"  # No Color


def print_step(message):
    """Print a step header"""
    print(f"{Colors.BLUE}==== {message} ===={Colors.NC}")


def print_success(message):
    """Print a success message"""
    print(f"{Colors.GREEN}✅ {message}{Colors.NC}")


def print_warning(message):
    """Print a warning message"""
    print(f"{Colors.YELLOW}⚠️  {message}{Colors.NC}")


def print_error(message):
    """Print an error message"""
    print(f"{Colors.RED}❌ {message}{Colors.NC}")


def run_command(cmd, check=True, shell=False):
    """Run a command and return the result"""
    try:
        if isinstance(cmd, str) and not shell:
            cmd = cmd.split()

        result = subprocess.run(
            cmd, capture_output=True, text=True, check=check, shell=shell
        )
        return result
    except subprocess.CalledProcessError as e:
        print_error(
            f"Command failed: {' '.join(cmd) if isinstance(cmd, list) else cmd}"
        )
        print_error(f"Error: {e.stderr}")
        if check:
            sys.exit(1)
        return e


def command_exists(command):
    """Check if a command exists in PATH"""
    try:
        subprocess.run([command, "--version"], capture_output=True, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def check_environment():
    """Check the environment and prerequisites"""
    print_step("Checking environment")

    # Check if we're in the project root
    if not (Path("setup.cfg").exists() and Path("pyproject.toml").exists()):
        print_error("This script must be run from the project root directory")
        sys.exit(1)

    # Check Python version
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    print(f"Python version: {python_version}")

    # Check environment variables
    if not (os.getenv("FFBB_BASIC_AUTH_USER") and os.getenv("FFBB_BASIC_AUTH_PASS")):
        print_warning(
            "Environment variables FFBB_BASIC_AUTH_USER and "
            "FFBB_BASIC_AUTH_PASS are not set"
        )
        print_warning("Some integration tests may fail")
        print("You can set them by:")
        print("  export FFBB_BASIC_AUTH_USER=your_username")
        print("  export FFBB_BASIC_AUTH_PASS=your_password")
        print()


def run_pre_commit():
    """Run pre-commit hooks"""
    print_step("Running static analysis and format checkers")

    if command_exists("pre-commit"):
        try:
            run_command(["pre-commit", "run", "--all-files", "--show-diff-on-failure"])
            print_success("Pre-commit checks passed")
        except subprocess.CalledProcessError:
            print_error("Pre-commit checks failed")
            sys.exit(1)
    else:
        print_warning("pre-commit not found, skipping static analysis")
        print_warning("Install with: pip install pre-commit")


def build_package():
    """Build the package"""
    print_step("Building package distribution files")

    if command_exists("tox"):
        try:
            run_command(["tox", "-e", "clean,build"])
            print_success("Package built successfully with tox")
        except subprocess.CalledProcessError:
            print_error("Package build failed")
            sys.exit(1)
    else:
        print_warning("tox not found, attempting to build with pip")
        try:
            run_command([sys.executable, "-m", "pip", "install", "build"])
            run_command([sys.executable, "-m", "build"])
            print_success("Package built successfully with build")
        except subprocess.CalledProcessError:
            print_error("Package build failed")
            sys.exit(1)


def run_tests():
    """Run the tests"""
    print_step("Running tests")

    if command_exists("tox"):
        # Check if wheel file exists
        dist_path = Path("dist")
        wheel_files = list(dist_path.glob("*.whl"))

        if wheel_files:
            wheel_file = wheel_files[0]
            print(f"Installing and testing wheel: {wheel_file}")
            try:
                run_command(
                    [
                        "tox",
                        "--installpkg",
                        str(wheel_file),
                        "--",
                        "-rFEx",
                        "--durations",
                        "10",
                        "--color",
                        "yes",
                    ]
                )
            except subprocess.CalledProcessError:
                print_error("Tests failed")
                sys.exit(1)
        else:
            print("No wheel file found, running tox normally")
            try:
                run_command(["tox"])
            except subprocess.CalledProcessError:
                print_error("Tests failed")
                sys.exit(1)
    else:
        print_warning("tox not found, running pytest directly")
        try:
            # Install dependencies
            run_command([sys.executable, "-m", "pip", "install", "-e", ".[testing]"])
            # Run pytest
            run_command(
                [
                    sys.executable,
                    "-m",
                    "pytest",
                    "-rFEx",
                    "--durations",
                    "10",
                    "--color",
                    "yes",
                ]
            )
        except subprocess.CalledProcessError:
            print_error("Tests failed")
            sys.exit(1)

    print_success("Tests completed successfully")


def generate_coverage():
    """Generate coverage report"""
    print_step("Generating coverage report")

    if command_exists("coverage"):
        try:
            run_command(["coverage", "report", "--show-missing"])
            run_command(["coverage", "html", "-d", "htmlcov"])
            print_success("Coverage report generated in htmlcov/")
        except subprocess.CalledProcessError:
            print_warning("Coverage report generation failed")
    else:
        print_warning("coverage not found, skipping coverage report")
        print_warning("Install with: pip install coverage")


def main():
    """Main function"""
    print("🚀 Starting local test execution...")
    print()

    try:
        check_environment()
        run_pre_commit()
        build_package()
        run_tests()
        generate_coverage()

        print()
        print_success("All checks completed successfully! 🎉")
        print()
        print("Summary of what was executed:")
        print("  ✅ Environment check")
        print("  ✅ Static analysis (if pre-commit available)")
        print("  ✅ Package build")
        print("  ✅ Test execution")
        print("  ✅ Coverage report (if coverage available)")
        print()
        print("This mirrors the CI pipeline defined in .github/workflows/ci.yml")

    except KeyboardInterrupt:
        print_error("Execution interrupted by user")
        sys.exit(1)
    except Exception as e:
        print_error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
