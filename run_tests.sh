#!/bin/bash

# Script to run tests locally similar to CI pipeline
# Based on .github/workflows/ci.yml

set -e  # Exit on any error

echo "🚀 Starting local test execution..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_step() {
    echo -e "${BLUE}==== $1 ====${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

# Check if we're in the project root
if [[ ! -f "setup.cfg" ]] || [[ ! -f "pyproject.toml" ]]; then
    print_error "This script must be run from the project root directory"
    exit 1
fi

# Check Python version
PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}' | cut -d. -f1-2)
echo "Python version: $PYTHON_VERSION"

# Check if required environment variables are set
if [[ -z "$FFBB_BASIC_AUTH_USER" ]] || [[ -z "$FFBB_BASIC_AUTH_PASS" ]]; then
    print_warning "Environment variables FFBB_BASIC_AUTH_USER and FFBB_BASIC_AUTH_PASS are not set"
    print_warning "Some integration tests may fail"
    echo "You can set them by:"
    echo "  export FFBB_BASIC_AUTH_USER=your_username"
    echo "  export FFBB_BASIC_AUTH_PASS=your_password"
    echo ""
    exit 1
fi

# Step 1: Check if pre-commit is available and run static analysis
print_step "Running static analysis and format checkers"
if command -v pre-commit &> /dev/null; then
    pre-commit run --all-files --show-diff-on-failure || {
        print_error "Pre-commit checks failed"
        exit 1
    }
    print_success "Pre-commit checks passed"
else
    print_warning "pre-commit not found, skipping static analysis"
    print_warning "Install with: pip install pre-commit"
fi

# Step 2: Clean and build package
print_step "Building package distribution files"
if command -v tox &> /dev/null; then
    tox -e clean,build || {
        print_error "Package build failed"
        exit 1
    }
    print_success "Package built successfully"
else
    print_warning "tox not found, attempting to build with pip"
    python3 -m pip install build
    python3 -m build
fi

# Step 3: Run tests
print_step "Running tests"
if command -v tox &> /dev/null; then
    # Run tox similar to CI
    if [[ -f "dist/"*.whl ]]; then
        WHEEL_FILE=$(ls dist/*.whl | head -1)
        echo "Installing and testing wheel: $WHEEL_FILE"
        tox --installpkg "$WHEEL_FILE" -- -rFEx --durations 10 --color yes
    else
        echo "No wheel file found, running tox normally"
        tox
    fi
else
    print_warning "tox not found, running pytest directly"
    # Install dependencies and run pytest
    python3 -m pip install -e .[testing]
    python3 -m pytest -rFEx --durations 10 --color yes
fi

print_success "Tests completed successfully"

# Step 4: Generate coverage report (optional)
print_step "Generating coverage report"
if command -v coverage &> /dev/null; then
    coverage report --show-missing
    coverage html -d htmlcov
    print_success "Coverage report generated in htmlcov/"
else
    print_warning "coverage not found, skipping coverage report"
    print_warning "Install with: pip install coverage"
fi

echo ""
print_success "All checks completed successfully! 🎉"
echo ""
echo "Summary of what was executed:"
echo "  ✅ Static analysis (if pre-commit available)"
echo "  ✅ Package build"
echo "  ✅ Test execution"
echo "  ✅ Coverage report (if coverage available)"
echo ""
echo "This mirrors the CI pipeline defined in .github/workflows/ci.yml"
