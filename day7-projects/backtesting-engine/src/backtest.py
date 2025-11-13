"""Backtesting Engine - TODO Implementation"""
import numpy as np
import pandas as pd

class Strategy:
    """TODO: Base strategy class"""
    
    def generate_signals(self, data):
        """TODO: Generate buy/sell signals
        Hint: Return 1 (buy), -1 (sell), 0 (hold)"""
        pass

class MomentumStrategy(Strategy):
    """TODO: Simple momentum strategy"""
    
    def __init__(self, lookback=20):
        """TODO: Initialize with lookback period"""
        pass
    
    def generate_signals(self, data):
        """TODO: Buy if price > MA, sell if price < MA"""
        pass

class MeanReversionStrategy(Strategy):
    """TODO: Mean reversion strategy"""
    
    def __init__(self, lookback=20, std_dev=2):
        """TODO: Initialize with lookback and std dev"""
        pass
    
    def generate_signals(self, data):
        """TODO: Buy if price < lower_band, sell if price > upper_band"""
        pass

class Backtester:
    """TODO: Backtesting engine"""
    
    def __init__(self, data, strategy, initial_capital=100000, commission=0.001):
        """TODO: Initialize backtester"""
        pass
    
    def run(self):
        """TODO: Run backtest
        Hint: Iterate through data, generate signals, execute trades"""
        pass
    
    def calculate_returns(self):
        """TODO: Calculate strategy returns"""
        pass
    
    def calculate_sharpe_ratio(self, risk_free_rate=0.02):
        """TODO: Sharpe ratio = (mean_return - rf) / std_return * √252"""
        pass
    
    def calculate_sortino_ratio(self, risk_free_rate=0.02):
        """TODO: Sortino = (mean_return - rf) / downside_std * √252"""
        pass
    
    def calculate_max_drawdown(self):
        """TODO: Maximum drawdown from peak"""
        pass
    
    def calculate_calmar_ratio(self):
        """TODO: Calmar = annual_return / max_drawdown"""
        pass
    
    def calculate_win_rate(self):
        """TODO: Percentage of winning trades"""
        pass
    
    def calculate_profit_factor(self):
        """TODO: Gross profit / gross loss"""
        pass
    
    def generate_equity_curve(self):
        """TODO: Generate equity curve over time"""
        pass
    
    def calculate_metrics(self):
        """TODO: Return dict of all metrics"""
        pass
