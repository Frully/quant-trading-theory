# 术语表 (Glossary)

> 按字母顺序排列的核心术语速查。点击术语可跳转到详细讨论的章节。

---

## A

### Alpha
超额收益，即投资收益中超出"应得收益"的部分。$\alpha = R_p - R_{expected}$
- 详见：[第零章：什么是量化交易](00_what_is_quant_trading.md)

### AMH (Adaptive Market Hypothesis)
适应性市场假说。认为市场效率是动态变化的，参与者通过试错学习和适应，类似生物进化。
- 提出者：Andrew Lo (MIT)
- 详见：[第十九章：市场结构演化](19_market_structure_evolution.md)

### APT (Arbitrage Pricing Theory)
套利定价理论。资产收益由多个因子的风险敞口决定，是多因子模型的理论基础。
- 详见：[第十二章：因子定价](12_factor_pricing.md)

### Arbitrage
套利。利用价格差异获取利润的行为。
- 详见：[第七章：套利策略](07_arbitrage_strategies.md)

---

## B

### Beta
市场敏感度。衡量资产相对于市场整体波动的敏感程度。$\beta = 1$ 表示与市场同步波动。
- 详见：[第十二章：因子定价](12_factor_pricing.md)

### Bias-Variance Tradeoff
偏差-方差权衡。模型太简单会欠拟合（高偏差），太复杂会过拟合（高方差）。
- 详见：[第十一章：机器学习与量化交易](11_machine_learning.md)

### Bid-Ask Spread
买卖价差。做市商买入价和卖出价之间的差额，是流动性成本的主要组成部分。
- 详见：[第十三章：市场微观结构](13_market_microstructure.md)

### Black-Scholes-Merton Model
BSM模型。期权定价的经典模型，假设标的资产服从几何布朗运动。
- 详见：[第十四章：衍生品定价](14_derivatives_pricing.md)

---

## C

### CAPM (Capital Asset Pricing Model)
资本资产定价模型。$E(R) = R_f + \beta \times (R_m - R_f)$，资产预期收益仅由市场风险敞口决定。
- 详见：[第十二章：因子定价](12_factor_pricing.md)

### Crowding
策略拥挤。当太多资金追逐同一策略时，收益下降且风险增加。
- 详见：[第十八章：市场生态](18_market_ecosystem.md)

### CVaR / ES (Expected Shortfall)
条件风险价值 / 预期损失。超过 VaR 时的平均损失，比 VaR 更关注尾部风险。
- 详见：[第十六章：风险理论](16_risk_theory.md)

---

## D

### Data Snooping
数据窥探。在同一数据集上测试大量假设，必然发现"显著"但虚假的结果。
- 详见：[第十一章：机器学习与量化交易](11_machine_learning.md)

### Delta
期权价格对标的资产价格变动的敏感度。看涨期权Delta为正，看跌期权Delta为负。
- 详见：[第十四章：衍生品定价](14_derivatives_pricing.md)

### Disposition Effect
处置效应。投资者倾向于过早卖出盈利股票、过晚卖出亏损股票。
- 详见：[第二章：行为金融](02_behavioral_finance.md)

---

## E

### EMH (Efficient Market Hypothesis)
有效市场假说。市场价格已充分反映所有可获得的信息。
- **弱式有效**：历史价格信息已反映（技术分析无效）
- **半强式有效**：公开信息已反映（基本面分析无效）
- **强式有效**：所有信息已反映（内幕交易也无效）
- 详见：[第一章：有效市场假说](01_efficient_market_hypothesis.md)

### Event-Driven Strategy
事件驱动策略。围绕特定公司或市场事件进行交易的策略。
- 详见：[第八章：事件驱动策略](08_event_driven.md)

---

## F

### Factor Model
因子模型。将资产收益分解为多个因子的线性组合。常见因子：市场、规模、价值、动量、质量。
- 详见：[第九章：因子与组合策略](09_factor_strategies.md)、[第十二章：因子定价](12_factor_pricing.md)

### Fat Tails
肥尾分布。极端事件发生概率远高于正态分布预测。
- 详见：[第十六章：风险理论](16_risk_theory.md)

### Framing Effect
框架效应。相同信息的不同表述方式会导致不同决策。
- 详见：[第二章：行为金融](02_behavioral_finance.md)

---

## G

### Gamma
Delta对标的资产价格的敏感度，衡量期权的凸性风险。
- 详见：[第十四章：衍生品定价](14_derivatives_pricing.md)

### Greeks
希腊字母。衡量期权价格对各种因素敏感度的指标（Delta、Gamma、Theta、Vega、Rho）。
- 详见：[第十四章：衍生品定价](14_derivatives_pricing.md)

---

## H

### HFT (High-Frequency Trading)
高频交易。利用速度优势和微观结构特征进行的超短期交易。
- 详见：[第十三章：市场微观结构](13_market_microstructure.md)

---

## I

### Implementation Shortfall
执行差额。从决策价格到实际成交价格的总成本。
- 详见：[第十七章：交易执行](17_trade_execution.md)

### Implied Volatility
隐含波动率。从期权市场价格反推的波动率，反映市场对未来波动的预期。
- 详见：[第十四章：衍生品定价](14_derivatives_pricing.md)

### Information Ratio
信息比率。超额收益与跟踪误差之比，衡量主动管理能力。
- 详见：[第九章：因子与组合策略](09_factor_strategies.md)

---

## K

### Kelly Criterion
凯利公式。$f^* = (bp - q) / b$，最大化长期财富增长率的最优下注比例。实践中常用半凯利。
- 详见：[第十五章：投资组合理论](15_portfolio_theory.md)

### Kyle Model
Kyle模型。描述知情交易者如何通过交易将信息融入价格的经典模型。
- 详见：[第十三章：市场微观结构](13_market_microstructure.md)

---

## L

### Limits to Arbitrage
限制套利。即使存在错误定价，套利者也可能因资金成本、做空限制、噪音交易者风险等无法纠正价格。
- 详见：[第三章：限制套利](03_limits_to_arbitrage.md)

### Liquidity
流动性。以合理价格快速买卖资产的能力。
- 详见：[第十三章：市场微观结构](13_market_microstructure.md)

### Loss Aversion
损失厌恶。损失带来的痛苦约为同等收益快乐的 2-2.5 倍。
- 详见：[第二章：行为金融](02_behavioral_finance.md)

---

## M

### Market Impact
市场冲击。交易对市场价格的影响。分为临时冲击和永久冲击。
- 详见：[第十七章：交易执行](17_trade_execution.md)

### Market Maker
做市商。通过持续提供买卖报价来提供流动性的交易者。
- 详见：[第十三章：市场微观结构](13_market_microstructure.md)

### Maximum Drawdown
最大回撤。从峰值到谷底的最大跌幅，衡量投资者心理承受能力。
- 详见：[第十六章：风险理论](16_risk_theory.md)

### Mean Reversion
均值回归。价格偏离后回归长期均值的倾向。
- 详见：[第六章：价值与反转策略](06_value_and_reversal.md)

### Momentum
动量效应。过去表现好的资产未来继续表现好的现象。
- 详见：[第五章：趋势与动量策略](05_trend_and_momentum.md)

### MPT (Modern Portfolio Theory)
现代投资组合理论。通过分散化在不降低预期收益的情况下降低风险。
- 提出者：Harry Markowitz (1952)
- 详见：[第十五章：投资组合理论](15_portfolio_theory.md)

---

## O

### Overconfidence
过度自信。投资者高估自己判断准确性的倾向。
- 详见：[第二章：行为金融](02_behavioral_finance.md)

### Overfitting
过拟合。模型在历史数据上表现好，但无法泛化到新数据。
- 详见：[第十一章：机器学习与量化交易](11_machine_learning.md)

---

## P

### Price Discovery
价格发现。市场参与者交易形成均衡价格的过程。
- 详见：[第十三章：市场微观结构](13_market_microstructure.md)

### Price Impact
价格冲击。大单交易对市场价格的影响。
- 详见：[第十七章：交易执行](17_trade_execution.md)

### Prospect Theory
前景理论。描述人们在不确定性下如何做决策，包含损失厌恶、参考点依赖等。
- 提出者：Kahneman & Tversky
- 详见：[第二章：行为金融](02_behavioral_finance.md)

### Put-Call Parity
看涨-看跌平价。$C - P = S - Ke^{-rT}$，期权价格必须满足的无套利关系。
- 详见：[第十四章：衍生品定价](14_derivatives_pricing.md)

---

## R

### Random Walk
随机游走。价格变动不可预测，像掷骰子一样随机。EMH 的核心推论。
- 详见：[第一章：有效市场假说](01_efficient_market_hypothesis.md)

### Risk Parity
风险平价。按风险贡献而非资金权重配置资产。
- 详见：[第十五章：投资组合理论](15_portfolio_theory.md)

---

## S

### Sharpe Ratio
夏普比率。$(R_p - R_f) / \sigma_p$，单位风险的超额收益，衡量风险调整后表现。
- 详见：[第九章：因子与组合策略](09_factor_strategies.md)

### Smart Beta
聪明贝塔。系统性地获取特定因子溢价的被动策略。
- 详见：[第九章：因子与组合策略](09_factor_strategies.md)

### Statistical Arbitrage
统计套利。基于统计关系的相对价值策略，承担一定风险。
- 详见：[第七章：套利策略](07_arbitrage_strategies.md)

### Survivorship Bias
幸存者偏差。只看到成功案例，忽略失败案例导致的统计偏差。
- 详见：[第十一章：机器学习与量化交易](11_machine_learning.md)

---

## T

### t-statistic
t 统计量。衡量结果偶然出现的可能性。t > 2 意味着偶然概率 < 5%；t > 3 意味着 < 0.3%。

### TCA (Transaction Cost Analysis)
交易成本分析。分解和量化交易的显性成本（佣金）和隐性成本（价差、冲击）。
- 详见：[第十七章：交易执行](17_trade_execution.md)

### Theta
时间价值衰减。期权价格随时间流逝而减少的速度。
- 详见：[第十四章：衍生品定价](14_derivatives_pricing.md)

### Tracking Error
跟踪误差。投资组合收益与基准收益的标准差。
- 详见：[第九章：因子与组合策略](09_factor_strategies.md)

### TWAP / VWAP
时间加权 / 成交量加权平均价格。常用的执行算法基准。
- 详见：[第十七章：交易执行](17_trade_execution.md)

---

## V

### Value Effect
价值效应。低估值股票长期跑赢高估值股票的现象。
- 详见：[第六章：价值与反转策略](06_value_and_reversal.md)

### VaR (Value at Risk)
风险价值。在给定置信水平下，未来一段时间内的最大可能损失。
- 详见：[第十六章：风险理论](16_risk_theory.md)

### Vega
期权价格对波动率变动的敏感度。
- 详见：[第十四章：衍生品定价](14_derivatives_pricing.md)

### VIX
波动率指数。芝加哥期权交易所编制的标普500期权隐含波动率指数，被称为"恐慌指数"。
- 详见：[第十章：波动率策略](10_volatility_strategies.md)

### Volatility
波动率。收益率的标准差，最基础的风险度量。
- 详见：[第十六章：风险理论](16_risk_theory.md)

### Volatility Risk Premium (VRP)
波动率风险溢价。隐含波动率与实现波动率之差，是卖出波动率策略的收益来源。
- 详见：[第十章：波动率策略](10_volatility_strategies.md)

### Volatility Surface
波动率曲面。隐含波动率作为执行价和到期时间函数的三维表示。
- 详见：[第十四章：衍生品定价](14_derivatives_pricing.md)

---

## 符号说明

| 符号 | 含义 |
|-----|------|
| $R_p$ | 投资组合收益 |
| $R_f$ | 无风险收益率 |
| $R_m$ | 市场收益率 |
| $\alpha$ | 超额收益 |
| $\beta$ | 市场敏感度 |
| $\sigma$ | 标准差/波动率 |
| $\Delta$ | Delta（期权） |
| $\Gamma$ | Gamma（期权） |
| $\Theta$ | Theta（期权） |
| $\nu$ | Vega（期权） |
| $K$ | 执行价（期权） |
| $T$ | 到期时间 |
| $N(\cdot)$ | 标准正态分布累积函数 |

---

## 章节索引

| 章节 | 主题 | 核心术语 |
|-----|------|---------|
| 00 | 什么是量化交易 | Alpha, Beta, 量化交易 |
| 01 | 有效市场假说 | EMH, Random Walk |
| 02 | 行为金融 | Prospect Theory, Loss Aversion, Disposition Effect |
| 03 | 限制套利 | Limits to Arbitrage |
| 04 | 信息与价格 | Information Asymmetry |
| 05 | 趋势与动量 | Momentum |
| 06 | 价值与反转 | Value Effect, Mean Reversion |
| 07 | 套利策略 | Arbitrage, Statistical Arbitrage |
| 08 | 事件驱动 | Event-Driven |
| 09 | 因子策略 | Factor Model, Smart Beta, Sharpe Ratio |
| 10 | 波动率策略 | VIX, VRP |
| 11 | 机器学习 | Overfitting, Bias-Variance |
| 12 | 因子定价 | CAPM, APT, Beta |
| 13 | 市场微观结构 | Liquidity, Bid-Ask Spread, HFT |
| 14 | 衍生品定价 | BSM, Greeks, Implied Volatility |
| 15 | 投资组合理论 | MPT, Risk Parity, Kelly |
| 16 | 风险理论 | VaR, CVaR, Fat Tails |
| 17 | 交易执行 | Market Impact, TCA, TWAP/VWAP |
| 18 | 市场生态 | Crowding, Liquidity |
| 19 | 市场结构演化 | AMH |
