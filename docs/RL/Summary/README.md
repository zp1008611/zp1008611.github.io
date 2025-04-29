# 总结


## 概率论



$$
E(X)=\sum_{x}x\cdot P(X = x)
$$

对于联合分布的离散型随机变量  $X$  和  $Y$  ，  $P(X = x)=\sum_{y}P(X = x,Y = y)$  

$$
\begin{align*}
E(X)&=\sum_{x}x\cdot\sum_{y}P(X = x,Y = y)\\
&=\sum_{y}\sum_{x}x\cdot P(X = x,Y = y)\\
&=\sum_{y}\sum_{x}x\cdot P(X = x|Y = y)P(Y = y)\\
&=\sum_{y}\left(\sum_{x}x\cdot P(X = x|Y = y)\right)P(Y = y)\\
&=\sum_{y}E(X|Y = y)P(Y = y)
\end{align*}
$$



## 贝尔曼方程

- 设$t \in \mathbb{N}_{\geq0}$为时间步（智能体 - 环境循环的迭代次数）. 
- 设$S_t$为时间$t$时环境的状态. 
- 设$A_t$为智能体在时间$t$采取的动作. 
- 设$R_t \in \mathbb{R}$为智能体在时间$t$获得的奖励. 也就是说，当环境状态为$S_t$，智能体采取动作$A_t$，环境转移到状态$S_{t + 1}$时，智能体获得奖励$R_t$.

- 奖励函数$R(s,a)$：
$$
R: \mathcal{S} \times \mathcal{A} \to \mathbb{R}, 
$$

并且

$$
R(s, a) := \mathbb{E}[R_t | S_t = s, A_t = a], 
$$

对于所有的$s$、$a$和$t$都成立.

- 
$$
p(s, a, s') := \text{Pr}(S_{t + 1} = s' | S_t = s, A_t = a). 
$$

- 策略$\pi$是一个函数：

$$
\pi: \mathcal{S} \times \mathcal{A} \to [0, 1], 
$$

并且对于所有的$s \in \mathcal{S}$，$a \in \mathcal{A}$和$t \in \mathbb{N}_{\geq0}$，有

$$
\pi(s, a) := \text{Pr}(A_t = a | S_t = s). 
$$

- 目标函数 $J$ 为：

$$
J(\pi) := \mathbb{E}\left[\sum_{t = 0}^{\infty} \gamma^{t} R_{t} | \pi\right],
$$

- 最优策略：最优策略 $\pi^{*}$ 是满足以下条件的任何策略（$\Pi=\mathcal{S}\times \mathcal{A}$）：

$$
\pi^{*} \in \underset{\pi \in \Pi}{\text{arg max}}\ J(\pi).
$$

- 状态价值函数，$G_t=\sum_{k=0}^{\infty} \gamma^{k} R_{t+k}$

$$
v^{\pi}(s):=E\left[G_{t} | S_{t}=s, \pi\right] 
$$

$$
\begin{align*}
v^{\pi}(s) &:= \mathbb{E}\left[\sum_{k = 0}^{\infty} \gamma^{k} R_{t + k} \Bigg| S_{t} = s, \pi\right]  \\
&= \mathbb{E}\left[R_{t} + \sum_{k = 1}^{\infty} \gamma^{k} R_{t + k} \Bigg| S_{t} = s, \pi\right]  \\
&= \mathbb{E}\left[R_{t} + \gamma\sum_{k = 1}^{\infty} \gamma^{k - 1} R_{t + k} \Bigg| S_{t} = s, \pi\right]  \\
&= \mathbb{E}\left[R_{t}| S_{t} = s, \pi\right]  + \mathbb{E}\left[\gamma\sum_{k = 1}^{\infty} \gamma^{k - 1} R_{t + k} \Bigg| S_{t} = s, \pi\right]  \\
&=\sum\limits_{a}\text{Pr}(A_t = a | S_t = s)\mathbb{E}[R_t | S_t = s, A_t = a]+ \mathbb{E}\left[\gamma\sum_{k = 1}^{\infty} \gamma^{k - 1} R_{t + k} \Bigg| S_{t} = s, \pi\right]\\
&= \sum_{a \in \mathcal{A}} \pi(s, a)R(s, a) + \mathbb{E}\left[\gamma\sum_{k = 0}^{\infty} \gamma^{k} R_{t + k + 1} \Bigg| S_{t} = s, \pi\right]  \\
&= \sum_{a \in \mathcal{A}} \pi(s, a)R(s, a) + \sum\limits_{a}\text{Pr}(A_t = a | S_t = s)\mathbb{E}\left[\gamma\sum_{k = 0}^{\infty} \gamma^{k} R_{t + k + 1} \Bigg| S_t = s, A_t = a\right]\\
&=\sum_{a \in \mathcal{A}} \pi(s, a)R(s, a) + \\ &\quad\quad\sum\limits_{a}\pi(s,a)\left(\sum\limits_{s'\in S}\text{Pr}(S_{t + 1} = s' | S_t = s, A_t = a)\mathbb{E}\left[\gamma\sum_{k = 0}^{\infty} \gamma^{k} R_{t + k + 1} \Bigg| S_t = s, A_t = a, S_{t+1}=s'\right]\right)\\
&= \sum_{a \in \mathcal{A}} \pi(s, a)R(s, a) + \sum_{a \in \mathcal{A}} \pi(s, a) \left(\sum_{s' \in \mathcal{S}} p(s, a, s') \mathbb{E}\left[\gamma\sum_{k = 0}^{\infty} \gamma^{k} R_{t + k + 1} \Bigg| S_{t} = s, A_{t} = a, S_{t + 1} = s', \pi\right]\right)  \\
&\stackrel{\text{Markov property}}{=} \sum_{a \in \mathcal{A}} \pi(s, a)R(s, a) + \sum_{a \in \mathcal{A}} \pi(s, a) \left(\sum_{s' \in \mathcal{S}} p(s, a, s')\gamma\mathbb{E}\left[\sum_{k = 0}^{\infty} \gamma^{k} R_{t + k + 1} \Bigg| S_{t + 1} = s', \pi\right]\right)  \\
&= \sum_{a \in \mathcal{A}} \pi(s, a)R(s, a) + \sum_{a \in \mathcal{A}} \pi(s, a) \sum_{s' \in \mathcal{S}} p(s, a, s')\gamma v^{\pi}(s')  \\
&= \sum_{a \in \mathcal{A}} \pi(s, a) \sum_{s' \in \mathcal{S}} p(s, a, s') \left(R(s, a) + \gamma v^{\pi}(s')\right) 
\end{align*}
$$


- $v^{\pi}$ 的贝尔曼方程, 看作将预期回报分解为两部分：下一个时间步获得的奖励，以及最终到达的下一个状态的价值. 即：

$$
v^{\pi}(s)=E[\underbrace{R\left(s, A_{t}\right)}_{即时奖励}+\gamma \underbrace{v^{\pi}\left(S_{t+1}\right)}_{下一状态的价值}|S_{t}=s, \pi] 
$$



- 如果一个策略$\pi$对于所有状态$s\in S$都满足

$$
v^{\pi}(s)=\max_{a\in\mathcal{A}}\sum_{s'\in\mathcal{S}}p(s,a,s')[R(s,a)+\gamma v^{\pi}(s')]
$$

我们就说策略$\pi$满足贝尔曼最优性方程. 

- **1）如果一个策略$\pi$满足贝尔曼最优性方程，那么它就是一个最优策略；2）如果状态集和动作集是有限的，奖励是有界的，并且 $\gamma\lt1$，那么存在一个策略 $\pi$ 满足贝尔曼最优性方程**. 