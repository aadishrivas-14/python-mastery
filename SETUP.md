# Setup Guide

## Quick Setup

### 1. Create Virtual Environment
```bash
cd python-mastery
python3 -m venv venv
```

### 2. Activate Virtual Environment

**Linux/Mac:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Verify Installation
```bash
pytest --version
python -c "import numpy, scipy, pandas; print('All packages installed!')"
```

## Running Tests

### All tests
```bash
pytest --tb=no -q
```

### Specific day
```bash
cd day1-basics
pytest tests/ -v
```

### Single test
```bash
pytest day1-basics/tests/test_basics.py::test_hello_world -v
```

## Deactivate Virtual Environment
```bash
deactivate
```

## Troubleshooting

### Python version
Requires Python 3.8+
```bash
python3 --version
```

### Reinstall dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Clear cache
```bash
find . -type d -name __pycache__ -exec rm -rf {} +
find . -type d -name .pytest_cache -exec rm -rf {} +
```
