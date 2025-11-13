# Project 4: Backtesting Engine

Build a strategy backtesting framework with performance analytics.

## Features
- Strategy backtesting framework
- Performance metrics (Sharpe, Sortino, Calmar)
- Transaction costs and slippage
- Position sizing
- Equity curve generation

## Usage
```python
strategy = MomentumStrategy(lookback=20)
backtest = Backtester(data, strategy, initial_capital=100000)
results = backtest.run()
metrics = backtest.calculate_metrics()
```

## Implementation
- Event-driven architecture
- Signal generation
- Position management
- PnL calculation
- Performance attribution

## Interview Focus
- Strategy evaluation
- Performance metrics
- Transaction costs
- Overfitting prevention
