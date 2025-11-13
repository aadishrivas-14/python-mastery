# Project 1: Options Pricer

Build a complete options pricing library with Greeks and implied volatility.

## Features
- Black-Scholes pricing (calls/puts)
- Greeks calculation (Delta, Gamma, Vega, Theta, Rho)
- Implied volatility solver (Newton-Raphson)
- Binomial tree pricing
- American options support

## Usage
```python
pricer = OptionsPricer()
call_price = pricer.black_scholes(S=100, K=100, T=1, r=0.05, sigma=0.2, option_type='call')
greeks = pricer.calculate_greeks(S=100, K=100, T=1, r=0.05, sigma=0.2)
iv = pricer.implied_volatility(market_price=10, S=100, K=100, T=1, r=0.05)
```

## Implementation
- Black-Scholes formula with N(d1), N(d2)
- Numerical differentiation for Greeks
- Newton-Raphson for IV
- Binomial tree with early exercise
- Vectorized calculations with NumPy

## Interview Focus
- Pricing models
- Greeks interpretation
- Volatility smile
- Put-call parity
