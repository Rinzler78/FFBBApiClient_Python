#!/bin/bash

# Quick test script - simplified version for rapid testing
# Run this for quick validation during development

set -e

echo "🏃‍♂️ Quick test execution..."

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

print_step() {
    echo -e "${BLUE}=== $1 ===${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

# Check if we're in the right directory
if [[ ! -f "setup.cfg" ]]; then
    echo "❌ Run this from the project root"
    exit 1
fi

# Quick install and test
print_step "Installing package in development mode"
pip install -e .[testing]

print_step "Running tests"
pytest tests/ -v --tb=short

print_success "Quick tests completed!"
echo ""
echo "For full CI-like testing, run: ./run_tests.sh or python run_tests.py"
