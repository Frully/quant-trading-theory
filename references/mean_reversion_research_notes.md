# 均值回归策略：理论与研究资料汇总

> 本文档整理了均值回归策略写作所需的理论基础、学术研究、实践案例和策略变体。

---

## 一、核心理论基础

### 1.1 均值回归的数学定义

**Ornstein-Uhlenbeck 过程** 是描述均值回归行为的核心数学模型：

$$dX_t = \theta(\mu - X_t)dt + \sigma dW_t$$

其中：
- $X_t$：时刻 t 的价格/价值
- $\mu$：长期均值
- $\theta$：均值回归速度（mean reversion rate）
- $\sigma$：波动率
- $dW_t$：维纳过程（布朗运动）

**关键特性**：
- OU 过程是唯一同时满足高斯、马尔可夫、时间齐次三个条件的非平凡随机过程
- 与几何布朗运动（GBM）的区别：GBM 没有回归中枢，会无限漂移
- OU 过程是离散时间 AR(1) 过程的连续时间类比

### 1.2 半衰期（Half-Life）

**定义**：价格偏离均值后，回归一半的预期时间。

**计算公式**：
$$\text{Half-life} = \frac{\ln(2)}{\theta}$$

**实践意义**：
- 提供策略持仓周期的参考
- 可作为选股筛选条件（如仅交易半衰期 < 50 天的资产）
- 用于设置策略参数（如回望期设为半衰期的倍数）

**计算方法**（Ernie Chan 方法）：
1. 对 $y_t - y_{t-1}$ 对 $y_{t-1}$ 回归
2. 获取回归系数 $\lambda$
3. 若 $\lambda < 0$，则存在均值回归；$\lambda > 0$ 则不存在

### 1.3 平稳性检验

**ADF 检验（Augmented Dickey-Fuller Test）**：
- 最常用的单位根检验方法
- 检验时间序列是否平稳
- 平稳时间序列具有均值回归特性

**Hurst 指数**：
- $H = 0.5$：随机游走
- $H < 0.5$：均值回归
- $H > 0.5$：趋势延续

### 1.4 协整（Cointegration）

**定义**：两个或多个非平稳时间序列的线性组合是平稳的。

**Engle-Granger 两步法**（1987）：
1. 对两个序列进行回归，获取残差
2. 对残差进行 ADF 检验

**Johansen 检验**：
- 优点：将每个资产作为独立变量处理
- 提供特征值统计量和迹统计量
- 比 Engle-Granger 方法更稳健

### 1.5 为什么价格会均值回归？

**学术理论基础**：

De Bondt & Thaler (1985) 提出均值回归假设，基本思想是"涨多了会跌，跌多了会涨"。Fama & French (1988) 研究了股票收益的记忆模式，发现过去价格可以预测未来价格，支持均值回归假设。

**行为金融解释**：

1. **投资者情绪波动**：
   - 市场情绪导致股票被过度喜爱或厌恶
   - 情绪创造了均值回归的条件
   - "无聊的业务可能被非理性地低估"

2. **前景理论（Prospect Theory）**：
   - Kahneman & Tversky (1979) 提出
   - 结合前景理论和均值回归可以更好地预测短期逆向行为和处置效应
   - 投资者对损失的敏感度高于收益

3. **过度反应与修正**：
   - 投资者对信息过度反应
   - 价格偏离真实价值
   - 随后回归到均衡水平

**与随机游走的争论**：

- **随机游走假说**：价格变动不可预测，冲击后不会回归
- **马尔可夫性质**：未来只取决于当前状态，与历史无关
- **市场现实**："市场保持非理性的时间可能比你保持偿付能力的时间更长"

### 1.6 参数估计的挑战

**OLS 回归法**：

将 OU 过程离散化：
$$X_{k+1} = \kappa\theta\Delta t - (\kappa\Delta t - 1)X_k + \sigma\sqrt{\Delta t}\epsilon_k$$

这类似于 AR(1) 模型，可用线性回归估计参数。

**最大似然估计（MLE）**：

当模型高度可信时，MLE 是首选方法，因为 OU 过程有显式的似然函数。

**估计难点**：

- 即使有超过 10,000 个观测值（相当于 1 分钟数据的一个多月），准确估计仍然非常困难
- 对于配对交易，均值回归速度与策略盈利能力高度相关
- 回归估计器只有在均值回归程度足够高、波动噪声影响较小时才有效
- 高频数据受市场微观结构噪声污染，需要专门处理

---

## 二、学术研究与实证证据

### 2.1 短期反转效应

**Jegadeesh (1990) & Lehmann (1990)**：
- 发现短期（1周-1个月）收益存在反转
- 1934-1987 年间，短期反转策略月均超额收益约 2%

**解释理论**：
1. **过度反应假说**：投资者对短期信息过度反应
2. **流动性供给假说**（Stefan Nagel, "Evaporating Liquidity"）：
   - 短期反转收益可视为流动性供给的补偿
   - 反转在高波动环境下更强
   - 与基本面消息无关

**实践限制**：
- 交易成本较高（频繁交易）
- 需要交易大市值股票以降低成本
- 在高经济政策不确定性（EPU）期间反转更强

### 2.2 长期反转与价值效应

**De Bondt & Thaler (1985)**：
- 过去 3-5 年的输家跑赢赢家
- 体现投资者对长期信息的过度反应

**Fama & French (1992)**：
- 价值效应：低 P/B 股票年化超额收益 5-7%
- 全球市场普遍存在

**Poterba & Summers (1988)**：
- "Mean reversion in stock prices: Evidence and implications"
- 股票价格长期存在均值回归

### 2.3 配对交易研究

**Gatev, Goetzmann & Rouwenhorst (2006)**：
- 发表于 *Review of Financial Studies*
- 1962-1997 年数据
- 配对交易年化超额收益可达 11-12%
- **重要发现：收益率在下降**
  - 1989 年前：月均超额收益 118bp
  - 1989 年后：月均超额收益 38bp（下降约 2/3）

**Do & Faff (2010)**：
- 确认配对交易收益持续下降趋势
- 但在危机期间（2001-2002、2007-2009）收益显著回升

**Caldeira & Moura (2013)**：
- 基于协整的配对交易组合
- 年化超额收益 16.38%
- 夏普比率 1.34
- 与市场低相关

### 2.4 统计套利

**Avellaneda & Lee (2010)**：
- 发表于 *Quantitative Finance*
- 使用 PCA 和 ETF 方法生成交易信号
- **PCA 策略**：1997-2007 年平均夏普比率 1.44
  - 2003 年后下降至 0.9
- **ETF 策略**：夏普比率 1.1，但 2002 年后表现下降
- 加入交易量信息后，2003-2007 年夏普比率提升至 1.51

### 2.5 ETF 均值回归

**IBS 效应**（Internal Bar Strength）：
- 可用于构建盈利的交易策略
- 与长期均值回归结合效果更好
- 添加 IBS 过滤器可提升 10 个百分点的收益，同时减少 45% 的市场暴露时间

**SPY/QQQ RSI 策略**：
- RSI(2) 策略年化收益 10.01%（买入持有 6.39%）
- 在熊市表现优异（2000-2002、2008/09、2018、2020）
- RSI(2) < 10 时入场：年化收益 12.7%，胜率 75%，夏普比率 2.85

### 2.6 交易成本的影响

**核心问题**：

均值回归策略通常需要频繁交易，交易成本可能吃掉大部分利润。

**学术研究发现**：

1. **Gatev 等 (2006)**：配对交易利润超过保守的交易成本估计，但部分利润可能来自市场微观结构效应。

2. **Leung & Li (2015)**：研究带交易成本的最优均值回归交易时机
   - 交易成本越高，最优入场价格越极端
   - 止损水平越高，投资者会在更低的止盈水平主动平仓

3. **Do & Faff (2012)**：专门研究计入交易成本后的配对交易盈利能力，发现需要仔细考虑交易成本的影响。

**交易成本的构成**：

| 成本类型 | 说明 | 典型水平 |
|---------|------|---------|
| 买卖价差 | 买价与卖价的差 | 股票 0.01-0.1%，加密货币 0.1-0.5% |
| 滑点 | 实际成交价与预期价的差 | 取决于订单大小和流动性 |
| 市场冲击 | 大单对价格的影响 | 大单可能显著移动价格 |
| 佣金手续费 | 经纪商/交易所费用 | 0.01-0.1% |

**短期反转策略的特殊挑战**：

- **Kaul & Nimalendran (1990)**：NASDAQ 股票的短期反转主要源于买卖价差误差
- **Avramov, Chordia & Goyal (2006)**：短期反转与流动性高度相关，逆向策略利润小于交易成本
- 独立的反转策略因换手率过高而不切实际

**解决方案**：

1. **聚焦大市值股票**：de Groot, Huij & Zhou 证明只交易大股票可显著降低成本
   - 经过改进的组合构建后，反转策略扣除成本后仍可获得每周 30-50bp 的收益

2. **降低换手率**：
   - 将反转筛选纳入其他策略的自然再平衡过程
   - 使用更宽的交易阈值

3. **使用限价单**：
   - 避免使用市价单
   - 利用交易算法优化执行

4. **选择流动性好的品种**：
   - 买卖价差窄
   - 市场深度足够

---

## 三、加密货币均值回归（专题）

### 3.1 比特币均值回归的特殊性

**学术研究发现**：

- 2013-2019 年数据未发现比特币存在简单的均值回归
- 使用 Gibbs 采样增强随机化方法检验，比特币表现为"均值发散"而非均值回归
- 体现了比特币在分析期间的爆发性特征

**非对称均值回归**：

Corbet & Katsiampa (2020) 发现：
- 负收益的回归比正收益更强、更快
- 使用多种数据频率（分钟、小时、日、周）都观察到这一现象
- 即使控制时变波动率（EGARCH 模型），非对称回归模式仍然存在
- 正收益的持续性高于负收益

**组合策略**：
- 趋势跟踪在局部最高点效果好（BTC 倾向于继续上涨）
- 均值回归在局部最低点效果好（BTC 倾向于反弹）
- 买入 20 日最高点（趋势）+ 买入 10 日最低点（回归）的组合表现优异

### 3.2 加密货币配对交易

**配对交易研究**：

在 Binance 交易所对 26 种流动性加密货币的研究（使用距离法和协整法）：
- 日频策略表现不佳，月均收益 -0.07%
- **高频策略表现显著更好**：5 分钟频率月均收益 11.61%
- 结果对参数设置和交易成本高度敏感

**常用交易对**：

- BTC/ETH：最常被研究的协整对
- 可构建包含 BTC、ETH、BCH、LTC 的协整组合（Nguyen & Leung, 2019）

**交易示例**：
当 BTC-ETH 价差偏离均值超过 1.5 个标准差时：
- BTC 被低估 → 做多 BTC
- ETH 被高估 → 做空 ETH
- 价差收敛（Z-score 穿越 0）时平仓
- 示例交易收益：13.6%

### 3.3 RSI 在比特币上的表现

**关键发现：传统 RSI 均值回归在比特币上效果差**

回测结果：
- RSI(14) 和 RSI(2) 的均值回归策略表现都很差
- 2019 年两种 RSI 策略都不盈利（因为价格趋势性强）
- RSI 可能长时间停留在超买/超卖区域

**什么有效：动量型 RSI**

- 入场：5 日 RSI 突破 50 向上
- 出场：5 日 RSI 跌破 50
- 年化收益 122% vs 买入持有 101%
- 最大回撤 39% vs 买入持有 83%

**改进建议**：
- RSI(2) 信号比 RSI(14) 更好
- 低时间框架比高时间框架更有利
- 必须加入趋势过滤器
- 不要将超卖视为即时反转信号

### 3.4 资金费率套利

**机制**：

永续合约没有到期日，通过资金费率机制与现货价格锚定：
- 永续价格 > 现货价格 → 资金费率为正 → 多头付给空头
- 永续价格 < 现货价格 → 资金费率为负 → 空头付给多头

**套利策略**：

当资金费率为正时：
1. 买入现货
2. 做空等量永续合约
3. 收取资金费率
4. 头寸对冲，赚取无风险收益

**收益与风险**：

- 研究表明资金费率套利可在 6 个月内产生高达 115.9% 的收益
- 最大可能损失仅 1.92%
- 年化收益可超过 10%（如 2023 年 10 月比特币资金费率飙升期间）

**均值回归特性**：

- 基差通常遵循均值回归过程
- 正常市场中基差回归的半衰期平均为 4-6 小时
- 极端条件下可能延长到数天
- 资金费率呈现"粘性"，遵循自回归过程

**风险**：
- 基差风险：现货和永续价格可能极端分化
- 流动性风险：波动时期难以平仓
- 建议杠杆不超过 2-3 倍，维持 150% 保证金缓冲

### 3.5 跨交易所套利

**机会来源**：

研究发现（Binance、Bitfinex、Bitstamp、Coinbase、Kraken）：
- 套利机会在网络拥堵和价格波动时出现
- 交易量和链上活动增加会提高交易所间相关性，减少套利机会

**AMM 与 DeFi 套利**：

去中心化交易所使用自动做市商（AMM），核心公式：x * y = k

套利机制：
- 价格偏离外部市场 → 套利者交易 → 价格回归均衡
- AMM 智能合约会激励交易者利用定价偏差
- 这种套利帮助不同市场间价格保持一致

**流动性提供者的风险**：
- 无常损失（Impermanent Loss）：代币价格变化导致的损失
- 如果价格回到初始位置，损失会消失
- 但如果在价格分化时提取流动性，损失就永久化了

---

## 四、策略类型与变体

### 4.1 技术指标类

**布林带 (Bollinger Bands)**：
- 中轨：移动平均线
- 上下轨：±N 个标准差
- 入场：价格触及下轨做多，触及上轨做空
- 出场：价格回归中轨

**RSI (Relative Strength Index)**：
- 超卖（<30）做多，超买（>70）做空
- **注意**：强趋势中 RSI 可能长期处于极端区域
- 需要结合其他指标或过滤条件

### 4.2 配对交易

**距离法**（Gatev 等）：
- 选择历史价格走势最相似的股票对
- 价差超过 2 个标准差时入场
- 价差收敛时出场

**协整法**：
- 对价格序列进行协整检验
- 构建平稳的价差序列
- 基于 Z-score 进行交易

**Z-score 阈值优化**：
- 保守阈值（±2.5 到 ±3.0）：信号少，单笔收益高
- 激进阈值（±1.5 到 ±2.0）：信号多，胜率高
- 常用组合：入场 |z|=2，出场 |z|=1

### 4.3 统计套利

**PCA 方法**（Avellaneda & Lee）：
- 使用主成分分析提取市场因子
- 交易残差的均值回归
- 本质上是交易相对于因子的特异性偏离

**ETF/成分股套利**：
- 当 ETF 价格偏离其成分股价值时交易
- 利用创建/赎回机制的摩擦

### 4.4 日历价差

**期货日历价差**：
- 做多远月合约，做空近月合约
- 利用价差的均值回归特性
- 能源市场（原油、天然气）效果较好

**研究发现**：
- WTI 原油和天然气的日历价差策略夏普比率可超过 2
- 需要考虑季节性因素（如天然气冬季/夏季）

### 4.5 波动率均值回归

**VIX 策略**：
- 波动率具有天然的均值回归特性
- VIX 期货曲线：
  - 升水（Contango）：做空 VIX 期货
  - 贴水（Backwardation）：做多 VIX 期货或现金

**风险**：
- VIX 飙升时做空损失巨大
- 需要严格的风险管理

### 4.6 市场状态识别

**隐马尔可夫模型（HMM）**：
- 识别市场状态（牛市/熊市、高波动/低波动）
- 在均值回归状态使用均值回归策略
- 在趋势状态切换到趋势跟踪策略

**研究发现**：
- HMM 在识别市场状态变化方面表现最佳
- 但存在滞后问题，可能错过拐点

---

## 五、风险与失败案例

### 5.1 LTCM 案例（1998）

**背景**：
- 由两位诺贝尔奖得主创立
- 核心策略：债券套利，基于收敛交易
- 杠杆率：约 30 倍

**策略逻辑**：
- 买入低估债券，卖空高估债券
- 相信价差会均值回归
- "Long Term" 名称来源于"长期收敛"假设

**失败原因**：
1. **俄罗斯债务违约**：1998 年 8 月，引发流动性危机
2. **价差扩大而非收敛**：几乎所有头寸都在亏损
3. **杠杆过高**：8 月单月亏损 44%
4. **流动性消失**：无法平仓

**教训**：
- "耐心资本"只有在最不需要的时候才有耐心
- 均值回归策略不能高杠杆
- 市场危机时流动性会消失
- 2008 年金融危机重现了类似问题

### 5.2 黑天鹅风险

**特征**：
- 极端市场事件可能使价格远离均值
- 均值本身可能发生漂移
- 历史关系可能失效

**具体风险**：
1. **体制转变**（Regime Shift）：市场结构性变化
2. **消息冲击**：重大新闻导致价格跳跃
3. **趋势形成**：均值回归假设失效

### 5.3 常见失败模式

**均值漂移**：
- 长期中枢发生变化
- 持续在"旧均值"附近交易导致系统性亏损

**杠杆与仓位**：
- 均值回归策略胜率高但偶尔大亏
- 高杠杆会放大单次大亏的影响
- 可能导致爆仓

**"Hold and Hope"**：
- 持有亏损头寸等待回归
- 最危险的行为之一
- 小盈利无法覆盖大亏损

---

## 六、与动量策略的关系

### 6.1 时间尺度分布

| 时间尺度 | 主导效应 |
|---------|---------|
| 极短期（1周-1月） | 反转 |
| 中期（3-12月） | 动量 |
| 长期（3-5年） | 反转 |

### 6.2 组合策略

**Menkhoff 等人的研究**（外汇市场）：
- 单独动量策略：年化 11.14%
- 结合反转信号的双排序策略：年化 20.24%

**组合优势**：
- 动量和均值回归的收益分布互补
- 均值回归：高胜率、小盈利、偶尔大亏（左偏）
- 动量：低胜率、小亏损、偶尔大盈（右偏）

### 6.3 市场状态适应

**Hurst 指数应用**：
- 判断当前市场是均值回归还是趋势延续
- 动态切换策略

---

## 七、著名机构与书籍

### 7.1 Renaissance Technologies

**创始人**：Jim Simons（数学家、密码破译专家）

**Medallion 基金**：
- 1988-2018 年：年化毛收益 66%，净收益 39%
- 2008 年金融危机：收益 98%
- 主要策略：统计套利、均值回归、市场中性

**方法论**：
- "从数据出发，不从模型出发"
- 寻找可复制数千次的模式
- "我们从别人对价格的反应中赚钱"（均值回归）

### 7.2 推荐书籍

**Ernie Chan 系列**：
1. *Quantitative Trading* (2009)
2. *Algorithmic Trading: Winning Strategies and Their Rationale* (2013)
3. *Machine Trading* (2017)

Chan 的书涵盖：
- 协整检验、Hurst 指数
- 配对交易、ETF 套利
- 日内均值回归（Gap 策略）
- Ornstein-Uhlenbeck 参数估计

**其他推荐**：
- Vidyamurthy, G. (2004). *Pairs Trading: Quantitative Methods and Analysis*
- Pole, A. (2007). *Statistical Arbitrage*

---

## 八、核心参考文献

### 8.1 奠基性论文

1. **Fama, E. F., & French, K. R. (1988)**. "Permanent and Temporary Components of Stock Prices." *Journal of Political Economy*, 96, 246-273.

2. **Poterba, J. M., & Summers, L. H. (1988)**. "Mean Reversion in Stock Prices: Evidence and Implications." *Journal of Financial Economics*, 22, 27-59.

3. **Jegadeesh, N. (1990)**. "Evidence of Predictable Behavior of Security Returns." *Journal of Finance*, 45(3), 881-898.

4. **Lehmann, B. N. (1990)**. "Fads, Martingales, and Market Efficiency." *Quarterly Journal of Economics*, 105(1), 1-28.

5. **De Bondt, W. F., & Thaler, R. (1985)**. "Does the Stock Market Overreact?" *Journal of Finance*, 40(3), 793-805.

6. **Engle, R. F., & Granger, C. W. J. (1987)**. "Co-integration and Error Correction: Representation, Estimation, and Testing." *Econometrica*, 55(2), 251-276.

### 8.2 配对交易与统计套利

7. **Gatev, E., Goetzmann, W. N., & Rouwenhorst, K. G. (2006)**. "Pairs Trading: Performance of a Relative-Value Arbitrage Rule." *Review of Financial Studies*, 19(3), 797-827.

8. **Avellaneda, M., & Lee, J. H. (2010)**. "Statistical Arbitrage in the U.S. Equities Market." *Quantitative Finance*, 10(7), 761-782.

9. **Caldeira, J., & Moura, G. V. (2013)**. "Selection of a Portfolio of Pairs Based on Cointegration: A Statistical Arbitrage Strategy." *SSRN*.

10. **Do, B., & Faff, R. (2010)**. "Does Simple Pairs Trading Still Work?" *Financial Analysts Journal*, 66(4), 83-95.

### 8.3 市场异象与因子

11. **Balvers, R., Wu, Y., & Gilliland, E. (2000)**. "Mean Reversion across National Stock Markets and Parametric Contrarian Investment Strategies." *Journal of Finance*, 55(2), 745-772.

12. **Nagel, S. (2012)**. "Evaporating Liquidity." *Review of Financial Studies*, 25(7), 2005-2039.

### 8.4 均值回归与黑天鹅

13. **Babayev, M., et al. (2020)**. "Short Term Trading Models – Mean Reversion Trading Strategies and the Black Swan Events." *SSRN*.

### 8.5 交易成本研究

14. **Leung, T., & Li, X. (2015)**. "Optimal Mean Reversion Trading with Transaction Costs and Stop-Loss Exit." *International Journal of Theoretical and Applied Finance*, 18(3).

15. **Do, B., & Faff, R. (2012)**. "Are Pairs Trading Profits Robust to Trading Costs?" *Journal of Financial Research*, 35(2), 261-287.

16. **Kaul, G., & Nimalendran, M. (1990)**. "Price Reversals: Bid-Ask Errors or Market Overreaction?" *Journal of Financial Economics*, 28(1-2), 67-93.

17. **de Groot, W., Huij, J., & Zhou, W. (2012)**. "Another Look at Trading Costs and Short-Term Reversal Profits." *Journal of Banking & Finance*, 36(2), 371-382.

### 8.6 加密货币均值回归

18. **Corbet, S., & Katsiampa, P. (2020)**. "Asymmetric Mean Reversion of Bitcoin Price Returns." *International Review of Financial Analysis*, 71.

19. **Nguyen, H., & Leung, T. (2019)**. "Constructing Cointegrated Cryptocurrency Portfolios for Statistical Arbitrage." *Studies in Economics and Finance*.

20. **Padysak, M., & Vojtko, R. (2022)**. "Seasonality, Trend-following, and Mean Reversion in Bitcoin." *SSRN*.

21. **Jung, J. (2025)**. "Statistical Arbitrage within Crypto Markets using PCA." *SSRN*.

22. **ScienceDirect (2022)**. "Exploring Sources of Statistical Arbitrage Opportunities among Bitcoin Exchanges."

---

## 九、写作大纲建议

基于收集的资料，建议文章结构如下：

```
# 均值回归策略

## 核心概念定义
- 什么是均值回归？
- 与趋势跟踪的对比（核心差异）
- 与网格交易、马丁格尔的区别

## 一、理论基础
### 1.1 数学模型
- Ornstein-Uhlenbeck 过程
- 半衰期计算与意义
- 参数估计方法（OLS、MLE）

### 1.2 检验方法
- ADF 检验
- Hurst 指数
- 协整检验（Engle-Granger、Johansen）

### 1.3 为什么会均值回归？
- 学术理论（Fama-French、Poterba-Summers）
- 行为金融解释（过度反应、前景理论）
- 与随机游走假说的争论

## 二、学术证据与收益特征
### 2.1 短期反转效应
- Jegadeesh & Lehmann 的发现
- 流动性供给假说（Nagel）

### 2.2 配对交易研究
- Gatev 等人的经典研究
- 收益率下降趋势（Do & Faff）

### 2.3 统计套利
- Avellaneda & Lee 的 PCA 方法

## 三、策略类型
### 3.1 技术指标类
- 布林带策略
- RSI 策略（注意事项）

### 3.2 配对交易
- 距离法 vs 协整法
- Z-score 阈值设定

### 3.3 跨资产策略
- 日历价差
- 波动率均值回归（VIX）

## 四、交易成本的关键影响
- 成本构成（价差、滑点、冲击、佣金）
- 学术研究发现
- 解决方案（大市值、降低换手、限价单）

## 五、加密货币应用
### 5.1 比特币的特殊性
- 非对称均值回归
- RSI 策略为何失效
- 动量 vs 回归的组合

### 5.2 加密货币配对交易
- 高频策略更有效
- BTC/ETH 协整对

### 5.3 资金费率套利
- 机制原理
- 收益与风险

## 六、风险与陷阱
### 6.1 LTCM 教训
### 6.2 黑天鹅与体制转变
### 6.3 常见失败模式
- 均值漂移
- 杠杆过高
- "Hold and Hope"

## 七、与动量的关系
- 时间尺度分布
- 收益分布互补
- 市场状态切换（HMM）

## 核心结论

## 延伸阅读
```

---

**资料整理时间**：2025 年 12 月 8 日（第二版，补充交易成本与加密货币内容）
