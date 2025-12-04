# 如何避免伪 Alpha？(How to Avoid False Alpha?)

> 核心问题：如何区分真实的预测能力与统计噪声、数据挖掘的产物？

---

## 问题的本质

这是量化交易中最危险的问题。伪 Alpha 在回测中表现完美，在实盘中迅速失效。

**不解决会怎样？**
- 回测收益无法兑现
- 资金亏损
- 对方法论失去信心

---

## 理论视角

### 视角 A：过拟合理论

*TODO: 深入分析*

- 偏差-方差权衡
- 模型复杂度与泛化
- 正则化方法

### 视角 B：多重检验问题

*TODO: 深入分析*

- 数据窥探偏差
- 发表偏差
- 多重检验校正 (Bonferroni, FDR)

### 视角 C：因果推断

*TODO: 深入分析*

- 相关性 vs 因果性
- 虚假相关
- 反事实推理

### 视角 D：样本外验证

*TODO: 深入分析*

- 时间序列交叉验证
- Walk-forward 分析
- 跨市场验证

### 各视角的整合

*TODO: 综合分析*

---

## 实践框架

*TODO: 从理论推导出的可操作方法*

- 回测陷阱清单
- 验证流程标准
- 红旗信号识别

---

## 常见陷阱

*TODO: 这个问题上容易犯的错误*

1. 过度优化参数
2. 幸存者偏差
3. 前视偏差 (Look-ahead bias)
4. 忽视交易成本
5. ...

---

## 延伸阅读

### 经典论文
- [ ] Bailey, D. & López de Prado, M. (2014). The Deflated Sharpe Ratio.
- [ ] Harvey, C. & Liu, Y. (2015). Backtesting.
- [ ] McLean, R. D. & Pontiff, J. (2016). Does Academic Research Destroy Stock Return Predictability?

### 书籍
- [ ] López de Prado, M. *Advances in Financial Machine Learning*
