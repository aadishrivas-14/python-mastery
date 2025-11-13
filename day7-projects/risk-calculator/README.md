# Project 3: Risk Calculator

Build a comprehensive risk management system.

## Features
- Value at Risk (VaR) - Historical, Parametric, Monte Carlo
- Conditional VaR (CVaR/Expected Shortfall)
- Portfolio risk metrics
- Stress testing
- Correlation analysis

## Usage
```python
risk = RiskCalculator(returns)
var_95 = risk.calculate_var(confidence=0.95, method='historical')
cvar_95 = risk.calculate_cvar(confidence=0.95)
stress = risk.stress_test(scenarios={'crash': -0.20, 'rally': 0.15})
```

## Implementation
- Historical simulation
- Variance-covariance method
- Monte Carlo simulation
- Cornish-Fisher expansion
- Portfolio decomposition

## Interview Focus
- Risk measures
- VaR methodologies
- Tail risk
- Stress testing
