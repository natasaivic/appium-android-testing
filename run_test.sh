#!/bin/bash

# Activate virtual environment
source venv/bin/activate

# Run the specific accessibility test
pytest test_cases/test_accessibility.py -v

# Alternative: Run all tests
# pytest test_cases/ -v