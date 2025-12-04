# 10. 交易执行：如何最小化成本？

> **状态**：待写
> **核心问题**：市场冲击、执行算法、TCA

---

## 大纲

### 一、核心概念定义

- 什么是交易执行？
- 执行成本的重要性
- Alpha 与执行的关系

### 二、交易成本的分解

- 显性成本（佣金、费用）
- 隐性成本（价差、冲击、时机）
- Implementation Shortfall

### 三、市场冲击

- 临时冲击 vs 永久冲击
- 冲击的影响因素
- 冲击模型（Almgren-Chriss）

### 四、执行算法

- TWAP / VWAP
- Implementation Shortfall 算法
- 自适应算法
- 算法选择的考量

### 五、最优执行理论

- 执行问题的数学框架
- 风险-成本权衡
- Almgren-Chriss 模型

### 六、TCA（交易成本分析）

- TCA 的目的与方法
- 基准选择
- 执行质量评估

### 七、对量化交易的启示

- 策略容量的限制
- 执行作为竞争优势

---

## 延伸阅读

- Almgren, R., & Chriss, N. (2000). *Optimal Execution of Portfolio Transactions*
- Kissell, R. (2013). *The Science of Algorithmic Trading and Portfolio Management*
