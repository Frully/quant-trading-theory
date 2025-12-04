# 术语表 (Glossary)

> 按字母顺序排列的核心术语速查。点击术语可跳转到详细讨论的文章。

---

## A

### Alpha
超额收益，即投资收益中超出"应得收益"的部分。$\alpha = R_p - R_{expected}$
- 详见：[01. 为什么存在超额收益](01_why_alpha_exists.md)

### AMH (Adaptive Market Hypothesis)
适应性市场假说。认为市场效率是动态变化的，参与者通过试错学习和适应，类似生物进化。
- 提出者：Andrew Lo (MIT)
- 详见：[01. 为什么存在超额收益](01_why_alpha_exists.md)

### APT (Arbitrage Pricing Theory)
套利定价理论。资产收益由多个因子的风险敞口决定，是多因子模型的理论基础。

### Arbitrage
套利。利用价格差异获取无风险利润的行为。

---

## B

### Beta
市场敏感度。衡量资产相对于市场整体波动的敏感程度。$\beta = 1$ 表示与市场同步波动。

### Bias-Variance Tradeoff
偏差-方差权衡。模型太简单会欠拟合（高偏差），太复杂会过拟合（高方差）。

---

## C

### CAPM (Capital Asset Pricing Model)
资本资产定价模型。$E(R) = R_f + \beta \times (R_m - R_f)$，资产预期收益仅由市场风险敞口决定。

### CVaR / ES (Expected Shortfall)
条件风险价值 / 预期损失。超过 VaR 时的平均损失，比 VaR 更关注尾部风险。

---

## D

### Data Snooping
数据窥探。在同一数据集上测试大量假设，必然发现"显著"但虚假的结果。

### Disposition Effect
处置效应。投资者倾向于过早卖出盈利股票、过晚卖出亏损股票。

---

## E

### EMH (Efficient Market Hypothesis)
有效市场假说。市场价格已充分反映所有可获得的信息。
- **弱式有效**：历史价格信息已反映（技术分析无效）
- **半强式有效**：公开信息已反映（基本面分析无效）
- **强式有效**：所有信息已反映（内幕交易也无效）
- 详见：[01. 为什么存在超额收益](01_why_alpha_exists.md)

---

## F

### Factor Model
因子模型。将资产收益分解为多个因子的线性组合。常见因子：市场、规模、价值、动量、质量。

### Fat Tails
肥尾分布。极端事件发生概率远高于正态分布预测。

---

## K

### Kelly Criterion
凯利公式。$f^* = (bp - q) / b$，最大化长期财富增长率的最优下注比例。实践中常用半凯利。

---

## L

### Limits to Arbitrage
限制套利。即使存在错误定价，套利者也可能因资金成本、做空限制、噪音交易者风险等无法纠正价格。
- 详见：[01. 为什么存在超额收益](01_why_alpha_exists.md)

### Loss Aversion
损失厌恶。损失带来的痛苦约为同等收益快乐的 2-2.5 倍。

---

## M

### Maximum Drawdown
最大回撤。从峰值到谷底的最大跌幅，衡量投资者心理承受能力。

### Momentum
动量效应。过去表现好的资产未来继续表现好的现象。

### MPT (Modern Portfolio Theory)
现代投资组合理论。通过分散化在不降低预期收益的情况下降低风险。
- 提出者：Harry Markowitz (1952)

---

## O

### Overconfidence
过度自信。投资者高估自己判断准确性的倾向。

### Overfitting
过拟合。模型在历史数据上表现好，但无法泛化到新数据。

---

## P

### Price Impact
价格冲击。大单交易对市场价格的影响。

### Prospect Theory
前景理论。描述人们在不确定性下如何做决策，包含损失厌恶、参考点依赖等。
- 提出者：Kahneman & Tversky

---

## R

### Random Walk
随机游走。价格变动不可预测，像掷骰子一样随机。EMH 的核心推论。

### Risk Parity
风险平价。按风险贡献而非资金权重配置资产。

---

## S

### Sharpe Ratio
夏普比率。$(R_p - R_f) / \sigma_p$，单位风险的超额收益，衡量风险调整后表现。

### Survivorship Bias
幸存者偏差。只看到成功案例，忽略失败案例导致的统计偏差。

---

## T

### t-statistic
t 统计量。衡量结果偶然出现的可能性。t > 2 意味着偶然概率 < 5%；t > 3 意味着 < 0.3%。

### TCA (Transaction Cost Analysis)
交易成本分析。分解和量化交易的显性成本（佣金）和隐性成本（价差、冲击）。

### TWAP / VWAP
时间加权 / 成交量加权平均价格。常用的执行算法基准。

---

## V

### Value Effect
价值效应。低估值股票长期跑赢高估值股票的现象。

### VaR (Value at Risk)
风险价值。在给定置信水平下，未来一段时间内的最大可能损失。

### Volatility
波动率。收益率的标准差，最基础的风险度量。

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
