# Dynamic Grid Trading Strategy: From Zero Expectation to Market Outperformance

> **Authors**: Kai-Yuan Chen, Kai-Hsin Chen, Jyh-Shing Roger Jang
> **Institution**: National Taiwan University
> **Source**: [arXiv:2506.11921](https://arxiv.org/abs/2506.11921)

---

## Abstract

In this paper, we propose a profitable strategy for the cryptocurrency market through grid trading. We start by analyzing the expected value of the traditional grid trading strategy. Based on our findings, we introduce an improved approach, the *Dynamic Grid-based Trading (DGT)* strategy, which demonstrates superior performance compared to conventional methods.

---

## 1 Introduction

Cryptocurrencies are digital assets secured by cryptography, operating on decentralized blockchain networks. In recent years, the use of cryptocurrencies for transactions has significantly increased. As of *August 17, 2024*, the daily trading volume of Bitcoin had reached approximately *$37 billion*. Furthermore, compared to traditional stock markets, cryptocurrencies exhibit substantial volatility.

To capitalize on this volatility, many traders employ grid trading strategies in their transactions. We began by proposing mathematical hypotheses and conducting proofs, which informed the design of our strategy based on the *traditional grid trading model*. Following this, we developed a backtesting system to assess its effectiveness through programming.

### 1.1 Traditional Grid Trading Strategy

We will provide a brief introduction to the *spot grid trading strategy* applied in our research. The grid type used in this study is the *geometric grid*, which places orders at price intervals that adjust proportionally. This method enables a more efficient capture of market movements across different levels of volatility.

#### 1.1.1 Initial Setup

Assume there are $n$ grids, resulting in $n+1$ grid levels. Given that the grid intervals have equal ratios, let the grid size be $k$. The current grid level is represented in black, while the other grid levels are shown in gray. Starting the grid at price $P$, if there are $m$ gray grid levels above and $n-m$ gray grid levels below the current price, the corresponding grid levels are:

| Grid Levels | Prices |
|-------------|--------|
| Top | $P \times (1+k)^m$ |
| ... | ... |
| Above | $P \times (1+k)$ |
| Reference | $P$ |
| Below | $P \times (1+k)^{-1}$ |
| ... | ... |
| Bottom | $P \times (1+k)^{-(n-m)}$ |

**Table 1**: Structure of geometric grid

If we invest *M USDT* in total, the instant starting the grid, we spend $M \times \frac{m}{n}$ *USDT* to buy cryptocurrency and leave $M \times \frac{n-m}{n}$ as *USDT*.

#### 1.1.2 Algorithm

After initiating the grid strategy, a transaction is triggered only when the price crosses a gray grid level. If the price rises and crosses the $G_i^{th}$ gray grid level, counted from the upper limit, we will sell $\frac{1}{G_i}$ of the cryptocurrency we currently hold. The original black grid level is then marked gray, and the crossed gray level is marked black. Conversely, if the price falls and crosses the $G_j^{th}$ gray grid level, counted from the lower limit, we will spend $\frac{1}{G_j}$ of the *USDT* we hold to purchase cryptocurrency. Similarly, the original black level is marked gray, and the crossed gray level is marked black. This dynamic adjustment of grid levels ensures that the strategy continually adapts to market movements without manual intervention.

#### 1.1.3 Termination

Once the price exceeds the upper limit or falls below the lower limit of the grid, the strategy terminates. According to the algorithm's logic, if the price surpasses the upper limit, we will retain the original *USDT* invested, the additional *USDT* earned from grid trading, and no cryptocurrency. Conversely, if the price drops below the lower limit, all the *USDT* initially invested will be converted into cryptocurrency, and we will still retain the bonus *USDT* earned from grid trading.

### 1.2 Data Resources

We obtained the spot data from *Binance* using the API: https://api.binance.com/api/v3/klines. The data spans from *January 2021 to July 2024*, with a time interval of *1 minute*, representing the highest frequency candlestick data available. Given this interval, we assume that the grid strategy executes no more than one transaction per minute. Additionally, we account for transaction fees, applying a fee of *0.0008*, which corresponds to the *Level 1* maker fee on OKX.

---

## 2 Observations

In the initial phase of our research, we identified several market patterns and conditions that guided the development of a series of hypotheses and mathematical derivations. These insights inspired the design of a novel grid trading strategy.

### 2.1 Claim 1: Infinite Resources

The first claim posits that if we have infinite capital and time, the grid trading strategy is inherently profitable. With unlimited funds, the strategy can capitalize on every price movement, as orders are consistently placed at regular intervals above and below the current price. This guarantees continuous buying at low prices and selling at higher ones, profiting from each market fluctuation. Infinite capital allows the strategy to endure even the most challenging market conditions without depleting funds. Similarly, infinite time ensures the ability to wait out any downturns or periods of stagnation, eventually profiting as the price moves. Therefore, with infinite resources, the grid trading strategy would always yield positive returns over time.

### 2.2 Claim 2: Zero Expected Value

We assume that the price either increases or decreases by $k$ with equal probability (50-50), which is a reasonable hypothesis for a basic investor model. Additionally, we do not consider transaction fees and assume that all cryptocurrency is sold if the price falls below our grid. Under these conditions, we can assert that the expected value of a grid trading strategy with grid size $k$ and a finite number of grid levels is zero. The proof is as follows:

#### 2.2.1 Required Number of Arbitrage Times

To determine when a grid trading strategy has a positive expected value, consider investing $M$ USDT in the grid strategy with $n$ grids, resulting in $n+1$ grid levels. Since this is a spot grid trading strategy, if the price rises linearly and surpasses the highest grid level, we can earn $P_u$ USDT, where

$$P_u = \frac{M}{n} \sum_{i=1}^{\frac{n}{2}} i \tag{1}$$

Conversely, if the price falls linearly and drops below the lowest grid level, we incur a loss of $L_l$ *USDT*, where

$$L_l = \frac{M}{n} \left[ \left(\frac{n}{2}\right)^2 + \sum_{i=1}^{\frac{n}{2}-1} i \right] \tag{2}$$

Thus, without accounting for profits from arbitrage, the expected value of the grid strategy is $E(G)$ *USDT*.

$$E(G) = \frac{1}{2} \times (P_u - L_l) = -\frac{M}{n} \left( \frac{n^2}{8} - \frac{n}{4} \right) \tag{3}$$

Since the grid strategy realizes profits before the price reaches the upper limit and buys more when the price falls, it results in a negative expected value if the price moves linearly. According to the derivation above, if the strategy can achieve more than $\frac{n^2}{8} - \frac{n}{4}$ arbitrage opportunities, it will yield a positive arbitrage value.

#### 2.2.2 Expected Value of Grid Trading

To calculate the expected value of transactions executed by a grid strategy, given that the probability of the price rising or falling by $k$ is equal, we can reframe the problem as follows: *What is the expected number of coin tosses required to achieve either $\frac{n}{2}$ more heads than tails or $\frac{n}{2}$ more tails than heads?*

To address this, we model the problem using a finite automaton. Here, $q_i$ represents the state where the difference between the number of heads and tails is $i$, and $E_i$ denotes the expected value starting from state $q_i$. The initial state is $q_0$, and the terminal state is $q_{\frac{n}{2}}$.

**Proof:**

The following equations represent the expected value relationships:

$$E_1 = E_0 - 1$$
$$E_2 = 2E_1 - E_0 - 2$$
$$E_3 = 2E_2 - E_1 - 2$$
$$E_i = 2E_{i-1} - E_{i-2} - 2 \tag{4}$$

From these observations, we conjecture that the recursive relationship for the expected value is $E_m = E_0 - m^2$. We will prove this conjecture using mathematical induction.

**Base Case:** For $m = 1, 2$:
- $E_1 = E_0 - 1$
- $E_2 = E_0 - 4$

The base case holds for $m = 1, 2$.

**Inductive Hypothesis:** Suppose the result holds for $m = k, k+1, k \in \mathbf{N}$:
- $E_k = E_0 - k^2$
- $E_{k+1} = E_0 - (k+1)^2$

**Inductive Step:** For $m = k + 2$:

$$E_{k+2} = 2E_{k+1} - E_k - 2$$
$$E_{k+2} = 2[E_0 - (k+1)^2] - (E_0 - k^2) - 2$$
$$E_{k+2} = E_0 - (k+2)^2$$

**Conclusion:** Since the base case holds and the inductive step has been proven, by mathematical induction, the statement is true for all $n \geq 1$.

By the proof we conducted, if the terminate state is $q_{\frac{n}{2}}$, the expected value follows the relationship given below, where $E_{\frac{n}{2}} = 0$:

$$E_{\frac{n}{2}} = E_0 - \left(\frac{n}{2}\right)^2$$
$$E_0 = \frac{n^2}{4}$$

Therefore, the expected value of transactions is $\frac{n^2}{4}$. Subtracting the transaction costs due to the price difference of $\frac{n}{2}$ and then dividing by 2—since each pair of buy and sell transactions constitutes one arbitrage opportunity—yields:

$$\frac{\frac{n^2}{4} - \frac{n}{2}}{2} = \frac{n^2}{8} - \frac{n}{4} \tag{5}$$

We obtain a result of $\frac{n^2}{8} - \frac{n}{4}$, which matches the required number of arbitrage opportunities. Therefore, we can conclude that the expected value of a grid strategy is zero under our assumptions.

$$E(\text{grid strategy}) = 0 \tag{6}$$

---

## 3 Dynamic Grid-Based Trading Strategy

Based on our observations, we have found that a grid strategy with infinite capital and time can generate a positive return, while a grid strategy that stops once the price exceeds its boundaries cannot. The key difference is that the former continues to capitalize on arbitrage opportunities, whereas the latter does not. Therefore, even though we lack infinite capital, it is unwise to stop the strategy when the price surpasses our upper or lower limits. This reasoning is straightforward, as the fundamental concept of grid trading is to buy more when the price falls. Selling all cryptocurrency when the price drops below the grid contradicts this core principle. Building on these insights, we developed a novel approach, the ***Dynamic Grid-based Trading (DGT)*** strategy, which continues to operate regardless of price movements.

### 3.1 DGT Algorithm

We selected two mainstream cryptocurrencies, *Bitcoin* and *Ethereum*, as the assets for backtesting our strategy. As previously mentioned, we utilized *1-minute candlestick data* for the testing. The algorithm for our ***DGT*** strategy is outlined as follows:

The strategy resets the grid whenever the price breaks above the upper limit or falls below the lower limit, with the current price becoming the new center. If the price breaks above the upper limit, the initial capital is fully recovered and reinvested in the next grid. Conversely, if the price falls below the lower limit, the strategy holds the cryptocurrency, using the arbitrage profits gained as the principal for the new grid.

**Algorithm 1: DGT Strategy**

```
1: Set Strategy Parameters: grid sizes, levels, transaction fee
2: Define Grid Calculation: Compute grid levels around start price
3: Prepare Results Storage: Initialize empty list for results
4: for each combination of grid parameters do
5:   Initialize variables: wallet, input money, grid count setup
6:   for each price data point do
7:     if price moves up then
8:       Execute sell if crossing grid level
9:     else if price moves down then
10:      Execute buy if crossing grid level
11:    end if
12:    if price exceeds grid boundaries then
13:      Calculate profit, Reset grid
14:      Update wallet
15:    end if
16:   end for
17:   Calculate final performance metrics
18: end for
```

The **wallet** tracks the cumulative profits earned from grid arbitrage, while **input money** represents the total invested capital. These variables are updated each time the grid is reset.

### 3.2 Backtesting Results

We used *Python* to construct the entire backtesting framework. The performance of the ***DGT*** in terms of *annualized return (IRR)* across various parameter combinations for two major cryptocurrencies, *BTC* and *ETH*, over the backtesting period from *January 2021 to July 2024*.

The **grid size** represents the ratio of each step in the geometric grid, while **grid numbers half** refers to the number of grids established above and below the central price when the grid is activated.

Key conclusions:
1. The *IRR* of our strategy remains consistently positive throughout the backtesting period, reaching as high as **60-70%**
2. This strong performance is largely due to the significant rise in cryptocurrency prices in recent years, which is highly favorable for spot grid trading
3. *ETH* demonstrates a higher *IRR* than *BTC*, likely because *ETH*'s smaller market volume leads to greater price volatility, which benefits grid trading
4. A small *grid size* results in lower profits due to the high proportion of transaction fees within the arbitrage profit
5. A large *grid size* and *grid numbers half* lead to poor *IRR* performance, as the infrequent activation of the grid results in lower cryptocurrency holdings
6. Optimizing the balance between grid size and grid numbers half is crucial for maximizing profits while minimizing costs and maintaining an active trading frequency

---

## 4 Discussion

### 4.1 Comparison with Buy-and-Hold

We evaluated two key metrics: *IRR (Internal Rate of Return)* and *MDD (Maximum Drawdown)*. By testing how different ***DGT*** parameters affect these metrics and comparing the results to the *buy-and-hold strategy*:

For *BTC*, we observe that the *IRR* of the ***DGT*** strategy is higher than that of the *buy-and-hold strategy*, while the *MDD* is significantly lower. This shows that the ***DGT*** strategy not only outperforms the *buy-and-hold strategy* in terms of returns but also manages risk more effectively. Even during market downturns, the strategy ensures relative stability of assets.

In the case of *ETH*, although the *IRR* of the ***DGT*** strategy is not substantially higher than that of the *buy-and-hold strategy*—likely due to *ETH*'s stronger upward trend during the backtesting period—the *MDD* is still much better controlled. When the market experienced a maximum decline of around **80%**, the *DGT strategy* limited the drawdown to approximately **50%**.

### 4.2 Comparison with Grid Trading Strategy

We also compare our ***DGT*** strategy with the traditional grid trading strategy, demonstrating how the adjustments we made improve overall performance. For *BTC*, the upper limit is $80,000, and the lower limit is $10,000. For *ETH*, the upper limit is $5,000, and the lower limit is $500.

Several conclusions:
1. Transaction fees significantly impact the overall trading results
2. Without considering fees, the *IRR* fluctuates at a consistent level, aligning with our earlier calculation that the expected value of the grid strategy is zero
3. After considering fees, a smaller *grid size* experiences lower volatility but is more susceptible to transaction fees, while a larger *grid size* exhibits higher volatility due to greater differences in arbitrage levels
4. The ***DGT*** strategy outperforms the *traditional grid trading strategy*, even when applied to a grid with predefined cryptocurrency price boundaries
5. This is expected, as the ***DGT*** strategy allows for the reinvestment of profits and more efficient use of capital

---

## 5 Conclusions and Future Work

Grid trading has become a widely used trading technique in recent years. However, our research reveals that without any insight into market trends, the expected value of grid trading is effectively zero. This means that investors face a high risk of losing money after taking transaction fees into consideration.

To address this, we developed a modified version of the grid trading strategy, known as the ***DGT*** strategy. **While it may seem like a blend of the *buy-and-hold strategy* and the *traditional grid trading strategy***, the ***DGT*** strategy has significantly outperformed both from *2021 to July 2024*. We hope that our research provides valuable insights for those considering grid trading strategies in the cryptocurrency market.

In this paper, we demonstrated through backtesting that the ***DGT*** strategy outperforms both the buy and hold strategy and the grid trading strategy. In the future, we will attempt to use mathematical theory to derive the probability of profit and the expected returns of the ***DGT*** strategy.

---

## Acknowledgments

We would like to extend our heartfelt gratitude to *Yu-Chen Hung* from the *Department of Economics at National Taiwan University (NTU)* and *Po-Chung Hsieh* from the *Department of Electrical Engineering at NTU* for their valuable insights and thoughtful discussions.

---

## References

1. Francesco Rundo, Francesca Trenta, Agatino Luigi di Stallo, and Sebastiano Battiato. 2019. Grid trading system robot (gtsbot): A novel mathematical algorithm for trading fx market. *Applied Sciences*, 9(9):1796.

2. Ruixin Jia. 2022. [The feasibility of grid trading approach for bitcoin based on backtesting](https://doi.org/10.4108/eai.18-11-2022.2327164). In *Proceedings of the 4th International Conference on Economic Management and Model Engineering, ICEMME 2022*.

3. Sirapop Kamrat, Napasorn Suesangiamsakul, and Rangsipan Marukatat. 2018. Technical analysis for cryptocurrency trading on mobile phones. In *The 2018 Technology Innovation Management and Engineering Science International Conference (TIMES-iCON2018)*, pages 1–4.

4. Jia Xu, Kun Hu, Guang Yang, Jian Zhang, and Jianxing Ye. 2019. Using machine learning for cryptocurrency trading. In *2019 IEEE International Conference on Industrial Cyber Physical Systems (ICPS)*, pages 647–652.

---

## Appendix A: Code Availability

The code used in this paper is available on GitHub: [https://github.com/colachenkc/Dynamic-Grid-Trading](https://github.com/colachenkc/Dynamic-Grid-Trading)
