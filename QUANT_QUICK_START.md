# Quant Projects - Quick Start Guide

## 🚀 Getting Started

### Prerequisites
```bash
pip install numpy scipy pandas pytest
```

### Project Structure
```
day7-projects/
├── options-pricer/          # Black-Scholes, Greeks, IV
├── market-simulator/        # Order book, matching engine
├── risk-calculator/         # VaR, CVaR, stress testing
├── backtesting-engine/      # Strategy backtesting
└── portfolio-optimizer/     # Mean-variance, efficient frontier
```

## 📝 Quick Implementation Guide

### 1. Options Pricer
```python
# Key formulas to implement:
# d1 = (ln(S/K) + (r + σ²/2)T) / (σ√T)
# d2 = d1 - σ√T
# Call = S*N(d1) - K*e^(-rT)*N(d2)
# Delta = N(d1)
# Gamma = N'(d1) / (S*σ*√T)
# Vega = S*N'(d1)*√T
```

**Test:**
```bash
cd day7-projects/options-pricer
pytest tests/ -v
```

### 2. Market Simulator
```python
# Key components:
# - Sorted dict for price levels
# - Price-time priority queue
# - Match when best_bid >= best_ask
# - Execute trades at best price
```

**Test:**
```bash
cd day7-projects/market-simulator
pytest tests/ -v
```

### 3. Risk Calculator
```python
# VaR methods:
# Historical: percentile of returns
# Parametric: μ - z_α * σ
# Monte Carlo: simulate, calculate percentile
# CVaR: mean of returns below VaR
```

**Test:**
```bash
cd day7-projects/risk-calculator
pytest tests/ -v
```

### 4. Backtesting Engine
```python
# Performance metrics:
# Sharpe = (r - rf) / σ * √252
# Sortino = (r - rf) / σ_downside * √252
# Calmar = annual_return / max_drawdown
# Max DD = max(peak - trough) / peak
```

**Test:**
```bash
cd day7-projects/backtesting-engine
pytest tests/ -v
```

### 5. Portfolio Optimizer
```python
# Optimization:
# Minimize: σ_p = √(w'Σw)
# Subject to: w'μ = target_return
#            Σw_i = 1
#            w_i >= 0 (no short selling)
```

**Test:**
```bash
cd day7-projects/portfolio-optimizer
pytest tests/ -v
```

## 🎯 Day 8: Quant DSA

### Quick Start
```bash
cd day8-quant-dsa
pytest tests/ -v
```

### Problem Categories

**Array/String (5 problems)**
- Moving average with sliding window
- Max profit with k transactions
- Longest consecutive sequence
- Merge intervals
- Trapping rain water

**Math/Probability (5 problems)**
- Random sampling (Fisher-Yates)
- Reservoir sampling
- Shuffle array
- Expected value calculation
- Monte Carlo π estimation

**Dynamic Programming (5 problems)**
- Optimal trading with fees
- Max profit with cooldown
- Stock with transaction limit
- Arbitrage detection

**Graph/Tree (5 problems)**
- Shortest path in DAG
- Topological sort
- Cycle detection
- Minimum spanning tree
- Lowest common ancestor

**System Design (5 problems)**
- LRU Cache (O(1) operations)
- Time Series Database
- Order Book Snapshot
- Rate Limiter
- Circular Buffer

## 💡 Interview Tips

### For Each Project
1. **Understand the math** - Don't just code, know why
2. **Start simple** - Basic version first
3. **Test edge cases** - σ=0, T=0, negative prices
4. **Optimize** - O(1) operations where possible
5. **Explain tradeoffs** - Memory vs speed

### Common Interview Questions

**Options Pricer:**
- "Implement Black-Scholes from scratch"
- "Calculate implied volatility"
- "What happens when volatility → 0?"
- "Explain put-call parity"

**Market Simulator:**
- "Design a limit order book"
- "How do you match orders efficiently?"
- "What's the time complexity of your matching?"
- "How do you handle market orders?"

**Risk Calculator:**
- "Compare VaR methodologies"
- "What's the difference between VaR and CVaR?"
- "How do you stress test a portfolio?"
- "Calculate portfolio VaR from individual VaRs"

**Backtesting:**
- "What's the difference between Sharpe and Sortino?"
- "How do you avoid overfitting?"
- "Calculate maximum drawdown"
- "What are transaction costs?"

**Portfolio Optimizer:**
- "Explain mean-variance optimization"
- "What is the efficient frontier?"
- "How does Black-Litterman work?"
- "What is risk parity?"

## 📚 Key Formulas Reference

### Black-Scholes
```
d1 = (ln(S/K) + (r + σ²/2)T) / (σ√T)
d2 = d1 - σ√T
Call = S*N(d1) - K*e^(-rT)*N(d2)
Put = K*e^(-rT)*N(-d2) - S*N(-d1)
```

### Greeks
```
Delta_call = N(d1)
Delta_put = N(d1) - 1
Gamma = N'(d1) / (S*σ*√T)
Vega = S*N'(d1)*√T
Theta_call = -S*N'(d1)*σ/(2√T) - r*K*e^(-rT)*N(d2)
Rho_call = K*T*e^(-rT)*N(d2)
```

### Risk Metrics
```
VaR_parametric = μ - z_α * σ
CVaR = E[X | X < VaR]
Sharpe = (r - rf) / σ * √252
Sortino = (r - rf) / σ_downside * √252
```

### Portfolio
```
r_p = w'μ
σ_p = √(w'Σw)
Sharpe_p = (r_p - rf) / σ_p
```

## 🏆 Success Checklist

### Week 1: Foundation
- [ ] Complete Days 1-4 (75 exercises)
- [ ] Master Python basics and OOP
- [ ] Understand decorators and generators

### Week 2: Advanced
- [ ] Complete Days 5-6 (40 exercises)
- [ ] Implement design patterns
- [ ] Solve algorithm problems

### Week 3: Quant Focus
- [ ] Build Options Pricer
- [ ] Build Market Simulator
- [ ] Build Risk Calculator
- [ ] Build Backtesting Engine
- [ ] Build Portfolio Optimizer
- [ ] Solve 25 Quant DSA problems

### Week 4: Interview Prep
- [ ] Review all projects
- [ ] Practice explaining code
- [ ] Mock interviews
- [ ] Optimize solutions
- [ ] Ready for interviews!

## 🎓 Next Steps

After completing this curriculum:
1. Apply to quant roles
2. Practice on LeetCode (company-specific)
3. Read "Options, Futures, and Other Derivatives"
4. Contribute to QuantLib
5. Build your own trading strategies

---

**Good luck with your quant interviews!** 🚀
