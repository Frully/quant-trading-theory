# 量化交易理论研究 (Quantitative Trading Theory)

## 项目简介

本项目致力于量化金融基础理论的系统性研究与整理。以**问题驱动**的方式，深入探讨量化交易的核心理论问题。

## 核心内容

### 入门篇

- **[00. 什么是量化交易？](core/00_what_is_quant_trading.md)** — 定义、与传统投资的区别、核心要素

### 七个核心问题

| # | 问题 | 状态 |
|---|------|------|
| 1 | [为什么存在超额收益？](core/01_why_alpha_exists.md) | ✓ 完成 |
| 2 | [如何发现 Alpha？](core/02_how_to_find_alpha.md) | 待写 |
| 3 | [如何避免伪 Alpha？](core/03_how_to_avoid_false_alpha.md) | 待写 |
| 4 | [如何确定仓位？](core/04_how_to_size_positions.md) | 待写 |
| 5 | [如何高效执行？](core/05_how_to_execute.md) | 待写 |
| 6 | [如何长期生存？](core/06_how_to_survive.md) | 待写 |
| 7 | [为什么 Alpha 会衰减？](core/07_why_alpha_decays.md) | 待写 |

### 参考资料

- **[理论速查手册](core/foundational_theories.md)** — 所有理论的简明索引
- **[术语表](core/glossary.md)** — 核心术语的快速查阅

## 如何使用

| 目标 | 路径 |
|-----|------|
| **入门** | 先读 [00. 什么是量化交易](core/00_what_is_quant_trading.md) |
| **深入** | 按 7 个核心问题逐篇研究 |
| **查阅** | 遇到术语时查看[术语表](core/glossary.md)或[速查手册](core/foundational_theories.md) |

## 目录结构

```
quant-trading-theory/
├── core/                   # 核心文档
│   ├── 00-07_*.md          # 入门篇 + 7 个核心问题
│   ├── foundational_theories.md  # 理论速查手册
│   └── glossary.md         # 术语表
└── CLAUDE.md               # 写作规范
```
