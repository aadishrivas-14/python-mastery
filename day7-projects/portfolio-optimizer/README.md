# Project 5: Portfolio Optimizer

Build a portfolio optimization system with multiple strategies.

## Features
- Mean-variance optimization (Markowitz)
- Efficient frontier calculation
- Risk parity allocation
- Black-Litterman model
- Constraint handling

## Usage
```python
optimizer = PortfolioOptimizer(returns, cov_matrix)
weights = optimizer.max_sharpe_ratio()
frontier = optimizer.efficient_frontier(n_points=100)
rp_weights = optimizer.risk_parity()
```

## Implementation
- Quadratic programming (scipy.optimize)
- Efficient frontier generation
- Risk budgeting
- Black-Litterman views
- Rebalancing strategies

## Interview Focus
- Portfolio theory
- Optimization methods
- Risk-return tradeoff
- Constraints handling
