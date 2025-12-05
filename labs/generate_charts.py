import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from scipy.stats import norm, t

# Set style
sns.set_theme(style="whitegrid")
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_plot(filename):
    ensure_dir('assets/charts')
    filepath = os.path.join('assets/charts', filename)
    plt.savefig(filepath, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Generated {filepath}")

def plot_efficient_market_hypothesis():
    """01_efficient_market_hypothesis.md: Random Walk vs Trend"""
    np.random.seed(42)
    steps = 100
    
    # Random Walk
    random_walk = np.cumsum(np.random.normal(0, 1, steps))
    
    # Trend
    trend = np.linspace(0, 20, steps) + np.random.normal(0, 1, steps)
    
    plt.figure(figsize=(10, 6))
    plt.plot(random_walk, label='随机游走 (有效市场)', linewidth=2)
    plt.plot(trend, label='趋势 (无效市场)', linewidth=2, linestyle='--')
    
    plt.title('随机游走 vs. 可预测趋势', fontsize=14)
    plt.xlabel('时间', fontsize=12)
    plt.ylabel('价格', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('emh_random_walk.png')

def plot_prospect_theory():
    """02_behavioral_finance.md: Prospect Theory Value Function"""
    x = np.linspace(-100, 100, 200)
    
    def value_function(x):
        alpha = 0.88
        beta = 0.88
        lam = 2.25
        y = np.zeros_like(x)
        mask_pos = x >= 0
        mask_neg = x < 0
        y[mask_pos] = x[mask_pos] ** alpha
        y[mask_neg] = -lam * ((-x[mask_neg]) ** beta)
        return y

    y = value_function(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, linewidth=3, color='#1f77b4')
    plt.axhline(0, color='black', linewidth=1, alpha=0.5)
    plt.axvline(0, color='black', linewidth=1, alpha=0.5)
    
    plt.annotate('损失厌恶\n(斜率更陡)', xy=(-50, -100), xytext=(-80, -50),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('敏感度递减\n(凹函数)', xy=(50, 30), xytext=(20, 80),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    
    plt.title('前景理论价值函数', fontsize=14)
    plt.xlabel('收益 / 损失', fontsize=12)
    plt.ylabel('心理价值', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    save_plot('prospect_theory_value.png')

def plot_probability_weighting():
    """02_behavioral_finance.md: Probability Weighting Function"""
    p = np.linspace(0, 1, 100)
    
    def weighting_function(p):
        gamma = 0.65
        return (p ** gamma) / ((p ** gamma + (1 - p) ** gamma) ** (1 / gamma))
    
    w = weighting_function(p)
    
    plt.figure(figsize=(8, 8))
    plt.plot(p, w, linewidth=3, label='主观权重', color='#d62728')
    plt.plot(p, p, linestyle='--', color='gray', label='客观概率')
    
    plt.title('概率加权函数', fontsize=14)
    plt.xlabel('客观概率 (p)', fontsize=12)
    plt.ylabel('决策权重 w(p)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('probability_weighting.png')

def plot_reaction_modes():
    """02_behavioral_finance.md: Underreaction and Overreaction"""
    t = np.arange(0, 50)
    
    # Fundamental value jump at t=20
    value = np.zeros_like(t, dtype=float)
    value[20:] = 10
    
    # Underreaction: Slow adjustment
    under = np.zeros_like(t, dtype=float)
    under[:20] = 0
    for i in range(20, 50):
        under[i] = 10 * (1 - np.exp(-0.2 * (i - 20)))
        
    # Overreaction: Overshoot and revert
    over = np.zeros_like(t, dtype=float)
    over[:20] = 0
    for i in range(20, 50):
        over[i] = 10 + 5 * np.exp(-0.3 * (i - 20)) * np.sin(0.5 * (i - 20))
        
    plt.figure(figsize=(10, 6))
    plt.plot(t, value, 'k--', label='基本面价值', linewidth=2)
    plt.plot(t, under, 'b-', label='反应不足', linewidth=2)
    plt.plot(t, over, 'r-', label='反应过度', linewidth=2)
    
    plt.axvline(20, color='gray', linestyle=':', alpha=0.5)
    plt.text(21, 5, '新闻事件', rotation=90)
    
    plt.title('市场对新闻的反应模式', fontsize=14)
    plt.xlabel('时间', fontsize=12)
    plt.ylabel('价格', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('reaction_modes.png')

def plot_noise_trader_risk():
    """03_limits_to_arbitrage.md: Divergence due to Noise Trader Risk"""
    t = np.arange(100)
    fundamental = np.full_like(t, 100)
    
    # Price diverges then converges
    divergence = 10 * np.sin(t / 10) * np.exp(-t / 100) # Initial divergence
    # Add a shock that widens divergence before convergence
    shock = np.zeros_like(t, dtype=float)
    shock[30:60] = -15 * np.sin((t[30:60]-30)/10)
    
    price = fundamental + divergence + shock
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, fundamental, 'k--', label='基本面价值', linewidth=2)
    plt.plot(t, price, 'r-', label='市场价格', linewidth=2)
    
    plt.annotate('套利机会', xy=(15, 110), xytext=(15, 120),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.annotate('价差扩大\n(追加保证金风险)', xy=(45, 85), xytext=(45, 70),
                 arrowprops=dict(facecolor='red', shrink=0.05))
    
    plt.title('套利限制：噪音交易者风险', fontsize=14)
    plt.xlabel('时间', fontsize=12)
    plt.ylabel('价格', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('noise_trader_risk.png')

def plot_information_decay():
    """04_information_theory.md: Information Value Decay"""
    t = np.linspace(0, 10, 100)
    
    # Different decay rates
    hft = np.exp(-5 * t)
    daily = np.exp(-0.5 * t)
    fundamental = np.exp(-0.1 * t)
    
    plt.figure(figsize=(10, 6))
    plt.plot(t, hft, label='高频交易 / 新闻 (秒级)', linewidth=2)
    plt.plot(t, daily, label='盈余惊喜 (天级)', linewidth=2)
    plt.plot(t, fundamental, label='结构性变化 (月级)', linewidth=2)
    
    plt.title('信息价值衰减 (半衰期)', fontsize=14)
    plt.xlabel('经过时间', fontsize=12)
    plt.ylabel('信息价值 / Alpha', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('information_decay.png')

def plot_momentum_crash():
    """05_trend_and_momentum.md: Momentum Crash during Reversal"""
    np.random.seed(42)
    t_steps = np.arange(100)
    
    # Market recovery with noise
    market = np.zeros_like(t_steps, dtype=float)
    # Bear market
    market[:50] = np.linspace(0, -20, 50) + np.random.normal(0, 0.5, 50)
    # Bull market rebound
    market[50:] = np.linspace(-20, 0, 50) + np.random.normal(0, 0.5, 50)
    
    # Momentum portfolio
    mom_return = np.zeros_like(t_steps, dtype=float)
    
    # Bull market (pre-crash) / Bear market (momentum works)
    mom_return[:50] = np.random.normal(0.2, 0.5, 50) 
    
    # Crash: High negative beta to market rebound
    market_returns = np.diff(market, prepend=0)
    # During rebound (t>=50), momentum suffers
    mom_return[50:] = -1.5 * market_returns[50:] + np.random.normal(0, 0.5, 50)
    
    mom_cum = np.cumsum(mom_return)
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    ax1.plot(t_steps, market, 'b--', label='市场指数', alpha=0.5)
    ax1.set_xlabel('时间')
    ax1.set_ylabel('市场水平', color='b')
    
    ax2 = ax1.twinx()
    ax2.plot(t_steps, mom_cum, 'r-', label='动量策略', linewidth=2)
    ax2.set_ylabel('动量累积收益', color='r')
    
    plt.title('动量崩溃剖析', fontsize=14)
    plt.axvline(50, color='k', linestyle=':', alpha=0.5)
    plt.text(51, mom_cum[50], '市场反弹', rotation=90)
    
    save_plot('momentum_crash.png')

def plot_martingale_risk():
    """06_value_and_reversal.md: Martingale Strategy Wealth Path"""
    np.random.seed(42)
    steps = 1000
    
    # Simulation of Martingale betting
    wealth = [100]
    bet = 1
    
    for i in range(steps):
        win = np.random.rand() > 0.5
        if win:
            wealth.append(wealth[-1] + bet)
            bet = 1 # Reset bet
        else:
            wealth.append(wealth[-1] - bet)
            bet *= 2 # Double bet
            
        if wealth[-1] <= 0:
            break
            
    plt.figure(figsize=(10, 6))
    plt.plot(wealth, color='purple', linewidth=1.5)
    plt.axhline(100, color='gray', linestyle='--')
    
    plt.title('马丁格尔策略：安全的幻觉', fontsize=14)
    plt.xlabel('下注次数', fontsize=12)
    plt.ylabel('财富', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    save_plot('martingale_risk.png')

def plot_pairs_trading():
    """07_arbitrage_strategies.md: Pairs Trading Spread"""
    np.random.seed(123)
    t = np.arange(200)
    
    # Cointegrated pair
    common_factor = np.cumsum(np.random.normal(0, 1, 200))
    stock_a = common_factor + np.random.normal(0, 0.5, 200)
    stock_b = common_factor + np.random.normal(0, 0.5, 200) + 5
    
    spread = stock_a - stock_b
    mean_spread = np.mean(spread)
    std_spread = np.std(spread)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    
    ax1.plot(t, stock_a, label='股票 A')
    ax1.plot(t, stock_b, label='股票 B')
    ax1.set_title('协整资产价格')
    ax1.legend()
    
    ax2.plot(t, spread, color='green', label='价差 (A - B)')
    ax2.axhline(mean_spread, color='black', linestyle='--')
    ax2.axhline(mean_spread + 2*std_spread, color='red', linestyle=':', label='上轨 (+2std)')
    ax2.axhline(mean_spread - 2*std_spread, color='red', linestyle=':', label='下轨 (-2std)')
    ax2.set_title('价差均值回归')
    ax2.legend()
    
    save_plot('pairs_trading_spread.png')

def plot_pead():
    """08_event_driven.md: Post-Earnings Announcement Drift (PEAD)"""
    days = np.arange(-10, 61)
    
    # Cumulative Abnormal Returns
    good_news = np.zeros_like(days, dtype=float)
    bad_news = np.zeros_like(days, dtype=float)
    
    # Jump at t=0
    good_news[10:] = 5 # Initial jump
    bad_news[10:] = -5
    
    # Drift
    for i in range(11, len(days)):
        good_news[i] = good_news[i-1] + 0.05 * np.exp(-0.05 * (i-10))
        bad_news[i] = bad_news[i-1] - 0.05 * np.exp(-0.05 * (i-10))
        
    plt.figure(figsize=(10, 6))
    plt.plot(days, good_news, 'g-', label='正向惊喜 (最高十分位)', linewidth=2)
    plt.plot(days, bad_news, 'r-', label='负向惊喜 (最低十分位)', linewidth=2)
    
    plt.axvline(0, color='black', linestyle='-')
    plt.axhline(0, color='gray', linestyle='--')
    
    plt.title('盈余公告后漂移 (PEAD)', fontsize=14)
    plt.xlabel('公告后天数', fontsize=12)
    plt.ylabel('累积超额收益 (%)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('pead_drift.png')

def plot_factor_heatmap():
    """09_factor_strategies.md: Factor Correlation Heatmap"""
    factors = ['MKT', 'SMB', 'HML', 'RMW', 'CMA', 'WML']
    
    # Stylized correlation matrix based on academic literature
    corr = np.array([
        [1.00, 0.30, 0.20, -0.10, -0.10, -0.10], # MKT
        [0.30, 1.00, 0.10, -0.20, -0.10, 0.05],  # SMB
        [0.20, 0.10, 1.00, 0.00, 0.60, -0.40],   # HML (Value)
        [-0.10, -0.20, 0.00, 1.00, 0.10, 0.10],  # RMW (Quality)
        [-0.10, -0.10, 0.60, 0.10, 1.00, -0.20], # CMA (Investment)
        [-0.10, 0.05, -0.40, 0.10, -0.20, 1.00]  # WML (Momentum)
    ])
    
    plt.figure(figsize=(8, 7))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1,
                xticklabels=factors, yticklabels=factors)
    
    plt.title('因子相关性矩阵', fontsize=14)
    save_plot('factor_correlation.png')

def plot_volatility_smile():
    """10_volatility_strategies.md & 15_derivatives_pricing.md: Volatility Smile"""
    strikes = np.linspace(80, 120, 100)
    atm = 100
    
    # Skew: IV is higher for lower strikes (put skew)
    iv = 0.2 + 0.0005 * (strikes - atm)**2 - 0.002 * (strikes - atm)
    
    plt.figure(figsize=(10, 6))
    plt.plot(strikes, iv, linewidth=2, color='purple')
    plt.axvline(atm, color='gray', linestyle='--', label='平值 (ATM)')
    
    plt.title('波动率微笑 / 偏斜', fontsize=14)
    plt.xlabel('行权价', fontsize=12)
    plt.ylabel('隐含波动率', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('volatility_smile.png')

def plot_efficient_frontier():
    """16_portfolio_theory.md: Efficient Frontier"""
    np.random.seed(42)
    n_assets = 5
    n_portfolios = 1000
    
    mean_returns = np.array([0.05, 0.1, 0.12, 0.15, 0.08])
    cov_matrix = np.array([
        [0.04, 0.02, 0.01, 0.01, 0.02],
        [0.02, 0.09, 0.03, 0.02, 0.03],
        [0.01, 0.03, 0.12, 0.04, 0.02],
        [0.01, 0.02, 0.04, 0.16, 0.03],
        [0.02, 0.03, 0.02, 0.03, 0.06]
    ])
    
    results = np.zeros((2, n_portfolios))
    
    for i in range(n_portfolios):
        weights = np.random.random(n_assets)
        weights /= np.sum(weights)
        
        p_return = np.sum(weights * mean_returns)
        p_std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        
        results[0,i] = p_std
        results[1,i] = p_return
        
    plt.figure(figsize=(10, 6))
    plt.scatter(results[0,:], results[1,:], c=results[1,:]/results[0,:], marker='o', cmap='viridis', s=10)
    plt.colorbar(label='夏普比率 (Sharpe Ratio)')
    
    plt.title('有效前沿模拟', fontsize=14)
    plt.xlabel('波动率 (风险)', fontsize=12)
    plt.ylabel('预期收益', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    save_plot('efficient_frontier.png')

def plot_tail_risk():
    """17_risk_theory.md: Fat Tails vs Normal Distribution"""
    x = np.linspace(-5, 5, 1000)
    
    # Normal Distribution
    y_norm = norm.pdf(x, 0, 1)
    
    # Student-t Distribution (Fat Tails)
    y_t = t.pdf(x, df=3) # Degrees of freedom = 3 for fat tails
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_norm, 'b-', label='正态分布', linewidth=2, alpha=0.6)
    plt.plot(x, y_t, 'r-', label='肥尾分布 (Student-t)', linewidth=2)
    
    # Highlight tail
    plt.fill_between(x, y_t, where=(x < -2), color='red', alpha=0.2, label='尾部风险')
    
    plt.title('尾部风险：正态分布 vs. 肥尾分布', fontsize=14)
    plt.xlabel('收益 (标准差)', fontsize=12)
    plt.ylabel('概率密度', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('tail_risk.png')

def plot_market_impact():
    """18_trade_execution.md: Market Impact Models"""
    size = np.linspace(0, 10000, 100)
    
    # Square Root Law: Impact ~ sigma * sqrt(size / volume)
    impact_sqrt = 0.5 * np.sqrt(size)
    
    # Linear Impact (for comparison)
    impact_linear = 0.005 * size
    
    plt.figure(figsize=(10, 6))
    plt.plot(size, impact_sqrt, label='平方根法则 (凹函数)', linewidth=2)
    plt.plot(size, impact_linear, label='线性冲击', linestyle='--', linewidth=2)
    
    plt.title('市场冲击模型', fontsize=14)
    plt.xlabel('交易规模 / 成交量', fontsize=12)
    plt.ylabel('价格冲击 (bps)', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('market_impact.png')

def plot_bias_variance():
    """11_machine_learning.md: Bias-Variance Tradeoff"""
    complexity = np.linspace(0, 10, 100)
    
    bias = (complexity - 10)**2 / 10
    variance = np.exp(complexity / 2.5) - 1
    total_error = bias + variance + 1
    
    plt.figure(figsize=(10, 6))
    plt.plot(complexity, bias, label='偏差 (Bias)', linewidth=2)
    plt.plot(complexity, variance, label='方差 (Variance)', linewidth=2)
    plt.plot(complexity, total_error, label='总误差', linewidth=3, color='black', linestyle='--')
    
    # Optimal point
    min_idx = np.argmin(total_error)
    plt.axvline(complexity[min_idx], color='gray', linestyle=':', label='最优复杂度')
    
    plt.title('偏差-方差权衡', fontsize=14)
    plt.xlabel('模型复杂度', fontsize=12)
    plt.ylabel('误差', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('bias_variance_tradeoff.png')

def plot_momentum_volatility():
    """11_machine_learning.md: Momentum vs Volatility Interaction"""
    volatility = np.linspace(0.1, 0.5, 100)
    
    # Momentum performance decays as volatility increases
    mom_return = 0.15 - 0.4 * (volatility - 0.1)
    
    plt.figure(figsize=(10, 6))
    plt.plot(volatility, mom_return, linewidth=2, color='green')
    plt.axhline(0, color='black', linewidth=1)
    
    plt.title('动量策略表现 vs. 市场波动率', fontsize=14)
    plt.xlabel('市场波动率 (Volatility)', fontsize=12)
    plt.ylabel('动量策略预期收益', fontsize=12)
    plt.grid(True, alpha=0.3)
    
    save_plot('momentum_volatility_interaction.png')

def plot_sharpe_decay():
    """11_machine_learning.md: Sharpe Ratio Decay"""
    years = np.arange(0, 6)
    sharpe = 2.0 * np.exp(-0.3 * years)
    
    plt.figure(figsize=(10, 6))
    plt.bar(years, sharpe, color='skyblue', alpha=0.8)
    plt.plot(years, sharpe, 'r--', marker='o', linewidth=2)
    
    plt.title('策略夏普比率衰减', fontsize=14)
    plt.xlabel('年份', fontsize=12)
    plt.ylabel('夏普比率 (Sharpe Ratio)', fontsize=12)
    plt.grid(True, alpha=0.3, axis='y')
    
    save_plot('sharpe_decay.png')

def plot_order_book():
    """14_market_microstructure.md: Limit Order Book Depth"""
    mid_price = 100
    
    # Bids
    bid_prices = np.linspace(95, 100, 50)
    bid_volumes = np.exp((bid_prices - 95)/2)
    
    # Asks
    ask_prices = np.linspace(100, 105, 50)
    ask_volumes = np.exp((105 - ask_prices)/2)
    
    plt.figure(figsize=(10, 6))
    
    # Plot area
    plt.fill_between(bid_prices, bid_volumes, color='green', alpha=0.5, label='买单 (Bids)')
    plt.fill_between(ask_prices, ask_volumes, color='red', alpha=0.5, label='卖单 (Asks)')
    
    plt.axvline(mid_price, color='black', linestyle='--', label='中间价 (Mid Price)')
    
    plt.title('限价订单簿 (LOB) 深度', fontsize=14)
    plt.xlabel('价格', fontsize=12)
    plt.ylabel('累积挂单量', fontsize=12)
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    save_plot('order_book_depth.png')

def main():
    print("Generating charts...")
    plot_efficient_market_hypothesis()
    plot_prospect_theory()
    plot_probability_weighting()
    plot_reaction_modes()
    plot_noise_trader_risk()
    plot_information_decay()
    plot_momentum_crash()
    plot_martingale_risk()
    plot_pairs_trading()
    plot_pead()
    plot_factor_heatmap()
    plot_volatility_smile()
    plot_efficient_frontier()
    plot_tail_risk()
    plot_market_impact()
    plot_bias_variance()
    plot_momentum_volatility()
    plot_sharpe_decay()
    plot_order_book()
    print("All charts generated successfully.")

if __name__ == "__main__":
    main()
