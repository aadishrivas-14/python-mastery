# Project 4: Data Analyzer

Build a data analysis tool using Pandas and visualization libraries.

## Features
- Load CSV/Excel files
- Data cleaning and preprocessing
- Statistical analysis
- Visualizations (charts, plots)
- Export reports

## Usage
```bash
python analyzer.py --file data.csv --analyze
python analyzer.py --file data.csv --visualize
```

## Implementation
- Pandas for data manipulation
- Matplotlib/Seaborn for visualization
- NumPy for calculations
- Handle missing data
- Generate summary statistics

## Run
```bash
pip install -r requirements.txt
python src/analyzer.py --help
pytest tests/ -v
```
