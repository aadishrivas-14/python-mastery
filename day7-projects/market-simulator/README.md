# Project 2: Market Simulator

Build a limit order book and matching engine simulator.

## Features
- Limit order book (LOB) with price-time priority
- Order matching engine
- Market maker simulation
- Order types: market, limit, stop
- Trade execution and fills

## Usage
```python
lob = OrderBook()
lob.add_order(Order(id=1, side='buy', price=100, quantity=10, type='limit'))
lob.add_order(Order(id=2, side='sell', price=100, quantity=5, type='limit'))
trades = lob.match_orders()
```

## Implementation
- Sorted dict for bid/ask levels
- Price-time priority queue
- Matching algorithm
- Market impact calculation
- Order book depth visualization

## Interview Focus
- Order book mechanics
- Matching algorithms
- Market microstructure
- Latency optimization
