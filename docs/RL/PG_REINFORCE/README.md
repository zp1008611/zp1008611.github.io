# 策略梯度

## Reference

- https://www.cs.mcgill.ca/~dprecup/courses/Winter2023/Lectures/12-polgrad-2023.pdf
- https://web.stanford.edu/class/cme241/lecture_slides/PolicyGradient.pdf
- https://rl-vs.github.io/rlvs2021/pg.html


在本章中，我们将探讨一些新内容. 到目前为止，学习的所有方法都是动作价值方法：这些方法学习动作的价值，然后基于估计的动作价值来选择动作. 如果没有动作价值估计，它们的策略甚至都不存在. 在本章中，我们考虑的方法则是学习一个参数化的策略，该策略可以在不参考价值函数的情况下选择动作. 价值函数可能仍用于学习策略参数，但并非动作选择所必需. 我们用符号 $\theta \in \mathbb{R}^{d'}$ 表示策略的参数向量. 因此，我们将 $\pi(a|s, \theta) := \Pr\{A_t = a | S_t = s, \theta_t = \theta\}$  记为在时刻 $t$ ，环境处于状态 $s$ 且参数为 $\theta$ 时采取动作 $a$ 的概率. 如果一种方法也学习近似价值函数，那么像往常一样，价值函数的权重向量记为 $w \in \mathbb{R}^{d}$  . 

在本章中，我们考虑基于某个标量性能度量 $J(\theta)$ 关于策略参数的梯度来学习策略参数的方法. 这些方法旨在最大化性能，因此它们的更新近似于梯度上升：
$$\theta_{t + 1} = \theta_t + \alpha \widehat{\nabla J(\theta_t)},\tag{13.1}$$
其中 $\widehat{\nabla J(\theta_t)} \in \mathbb{R}^{d'}$  是一个随机估计量，其期望近似于性能度量关于其自变量 $\theta_t$  的梯度. 所有遵循这种通用框架的方法，我们都称之为策略梯度方法 ，无论它们是否也学习近似价值函数. 同时学习策略和价值函数近似的方法通常被称为演员 - 评论家方法，其中“演员”指学习到的策略，“评论家”指学习到的价值函数，通常是状态价值函数. 

首先，我们处理情节式情况，其中性能被定义为起始状态的值. 在处理完情节式情况后，我们考虑持续式情况，其中性能被定义为平均奖励率. 最后，我们能够用非常相似的形式来表述这两种情况的算法. 


## 1 策略近似及其优势

在策略梯度方法中，策略可以通过任何方式进行参数化，只要 $\pi(a|s,\theta)$ 关于其参数是可微的，也就是说，只要 $\nabla\pi(a|s,\theta)$ （ $\pi(a|s,\theta)$ 关于 $\theta$ 各分量的偏导数组成的列向量）对于所有的 $s\in S$ 、 $a\in A(s)$ 和 $\theta\in\mathbb{R}^{d'}$ 都存在且有限. 在实践中，为了确保探索性，我们通常要求策略永远不会变成确定性的（即对于所有的 $s$ 、 $a$ 和 $\theta$ ， $\pi(a|s,\theta)\in(0,1)$ ）. 在本节中，我们将介绍离散动作空间最常见的参数化方式，并指出它相对于动作价值方法的优势. 基于策略的方法也为处理连续动作空间提供了有效的途径，我们将在13.7节中进行介绍. 

如果动作空间是离散的且规模不大，那么一种自然且常见的参数化方式是为每个状态 - 动作对构建参数化的数值偏好 $h(s,a,\theta)\in\mathbb{R}$ . 在每个状态中，具有最高偏好的动作被赋予最高的选择概率，例如，根据指数soft - max分布：

$$
\pi(a|s,\theta)\doteq\frac{e^{h(s,a,\theta)}}{\sum_{b}e^{h(s,b,\theta)}}
$$

其中 $e\approx2.71828$ 是自然对数的底数. 注意，这里的分母是为了确保每个状态下的动作概率之和为1. 我们将这种策略参数化方式称为基于动作偏好的soft - max. 

动作偏好本身可以任意参数化. 例如，它们可以由深度人工神经网络（ANN）计算，其中 $\theta$ 是网络所有连接权重组成的向量（如16.6节中描述的AlphaGo系统）. 或者偏好可以简单地是特征的线性函数：
$$h(s,a,\theta)=\theta^{\top}x(s,a)$$
使用通过9.5节中描述的任何方法构建的特征向量 $x(s,a)\in\mathbb{R}^{d'}$ . 

根据基于动作偏好的soft - max对策略进行参数化的一个优势是，近似策略可以接近确定性策略，而在基于动作价值的 $\epsilon$  - 贪婪动作选择中，总是有 $\epsilon$ 的概率选择随机动作. 当然，可以根据基于动作价值的soft - max分布进行选择，但仅此一点并不能使策略接近确定性策略. 相反，动作价值估计会收敛到它们相应的真实值，这些真实值会有一定的差异，转化为除0和1之外的特定概率. 如果soft - max分布包含一个温度参数，那么可以随着时间降低温度以接近确定性，但在实践中，如果没有比我们希望假设的更多关于真实动作价值的先验知识，很难选择降温策略，甚至难以确定初始温度. 动作偏好则不同，因为它们不会趋近于特定的值；相反，它们被驱动产生最优随机策略. 如果最优策略是确定性的，那么最优动作的偏好将被驱动到比所有次优动作无限高（如果参数化允许的话）. 

基于动作偏好的soft - max对策略进行参数化的第二个优势是，它能够以任意概率选择动作. 在具有显著函数近似的问题中，最佳近似策略可能是随机的. 例如，在信息不完美的纸牌游戏中，最优玩法通常是按照特定概率执行两种不同的操作，比如在扑克游戏中的诈唬. 动作价值方法没有自然的方式来找到随机最优策略，而策略近似方法可以，如示例13.1所示. 

最后，我们注意到，策略参数化的选择有时是将关于期望策略形式的先验知识注入强化学习系统的一种好方法. 这通常是使用基于策略的学习方法的最重要原因. 


## 2 策略梯度定理

除了策略参数化相对于 $\epsilon$  - 贪婪动作选择的实际优势之外，还有一个重要的理论优势. 在连续的策略参数化中，动作概率随着学习到的参数平滑变化，而在 $\epsilon$  - 贪婪选择中，如果估计的动作价值发生任意小的变化，导致具有最大值的动作发生改变，那么动作概率可能会发生巨大变化. 很大程度上由于这个原因，与动作价值方法相比，策略梯度方法具有更强的收敛保证. 特别地，正是策略对参数的连续依赖性使得策略梯度方法能够近似梯度上升（13.1）. 

情节式和持续式情况对性能度量 $J(\theta)$ 的定义不同，因此在某种程度上必须分别处理. 尽管如此，我们将尝试统一地介绍这两种情况，并开发一种符号表示，以便用一组方程描述主要的理论结果. 

在本节中，我们处理情节式情况，将性能度量定义为情节起始状态的值. 通过假设每个情节都从某个特定的（非随机）状态 $s_{0}$ 开始，我们可以在不损失任何有意义的一般性的情况下简化符号. 那么，在情节式情况下，我们将性能定义为：

$$
J(\theta)\doteq v_{\pi_{\theta}}(s_{0})
$$
其中 $v_{\pi_{\theta}}$ 是 $\pi_{\theta}$ （由 $\theta$ 确定的策略）的真实价值函数. 在我们接下来的讨论中，对于情节式情况，我们将假设不进行折扣（ $\gamma = 1$ ），尽管为了完整性，我们在框中的算法中确实考虑了折扣的可能性. 

在函数近似的情况下，以确保性能提升的方式改变策略参数似乎具有挑战性. 问题在于性能既取决于动作选择，也取决于进行这些选择的状态分布，而这两者都受策略参数的影响. 给定一个状态，从参数化的知识中可以相对直接地计算出策略参数对动作的影响，进而对奖励的影响. 但是策略对状态分布的影响是环境的函数，通常是未知的. 当梯度取决于策略变化对状态分布的未知影响时，我们如何估计性能相对于策略参数的梯度呢？

幸运的是，策略梯度定理为这个挑战提供了一个出色的理论答案，它给出了性能相对于策略参数的梯度的解析表达式（这正是我们为了进行梯度上升（13.1）所需要近似的），该表达式不涉及状态分布的导数. 情节式情况下的策略梯度定理表明：
$$\nabla J(\theta)\propto\sum_{s}\mu(s)\sum_{a}q_{\pi}(s,a)\nabla\pi(a|s,\theta)$$
其中梯度是关于 $\theta$ 各分量的偏导数组成的列向量， $\pi$ 表示与参数向量 $\theta$ 对应的策略. 这里的符号 $\propto$ 表示“与……成比例”. 在情节式情况下，比例常数是情节的平均长度，在持续式情况下它是1，因此这种关系实际上是相等的. 这里的分布 $\mu$ （如第9章和第10章中）是在策略 $\pi$ 下的在线策略分布（见第199页）. 上一页框中给出了情节式情况下策略梯度定理的证明. 
### 策略梯度定理（情节式情况）的证明
仅使用基础微积分和项的重新排列，我们就可以从基本原理证明策略梯度定理. 为了简化符号，在所有情况下我们都隐含地认为 $\pi$ 是 $\theta$ 的函数，并且所有梯度也隐含地是关于 $\theta$ 的. 首先注意到，状态价值函数的梯度可以用动作价值函数表示为：
$$\begin{aligned}\nabla v_{\pi}(s)&=\nabla\left[\sum_{a}\pi(a|s)q_{\pi}(s,a)\right],\quad\forall s\in\mathcal{S}\quad(练习3.18)\\&=\sum_{a}\left[\nabla\pi(a|s)q_{\pi}(s,a)+\pi(a|s)\nabla q_{\pi}(s,a)\right]\quad(微积分乘积法则)\\&=\sum_{a}\left[\nabla\pi(a|s)q_{\pi}(s,a)+\pi(a|s)\nabla\sum_{s',r}p(s',r|s,a)(r + v_{\pi}(s'))\right]\\&=\sum_{a}\left[\nabla\pi(a|s)q_{\pi}(s,a)+\pi(a|s)\sum_{s'}p(s'|s,a)\nabla v_{\pi}(s')\right]\quad(公式3.4)\\&=\sum_{a}\left[\nabla\pi(a|s)q_{\pi}(s,a)+\pi(a|s)\sum_{s'}p(s'|s,a)\sum_{a'}\left[\nabla\pi(a'|s')q_{\pi}(s',a')+\pi(a'|s')\sum_{s''}p(s''|s',a')\nabla v_{\pi}(s'')\right]\right]\end{aligned}$$
经过反复展开，其中 $Pr(s\to x,k,\pi)$ 是在策略 $\pi$ 下从状态 $s$ 经过 $k$ 步转移到状态 $x$ 的概率. 那么立即有：
$$\begin{array}{rlrl}\nabla J(\theta)&=\nabla v_{\pi}(s_{0})\\&=\sum_{s}\left(\sum_{k = 0}^{\infty}Pr(s_{0}\to s,k,\pi)\right)\sum_{a}\nabla\pi(a|s)q_{\pi}(s,a)\\&=\sum_{s}\eta(s)\sum_{a}\nabla\pi(a|s)q_{\pi}(s,a)\quad(第199页框中内容)\\&=\sum_{s'}\eta(s')\sum_{s}\frac{\eta(s)}{\sum_{s'}\eta(s')}\sum_{a}\nabla\pi(a|s)q_{\pi}(s,a)\\&=\sum_{s'}\eta(s')\sum_{s}\mu(s)\sum_{a}\nabla\pi(a|s)q_{\pi}(s,a)\quad(公式9.3)\\&\propto\sum_{s}\mu(s)\sum_{a}\nabla\pi(a|s)q_{\pi}(s,a)\quad(证毕)\end{array}$$

## 13.3 REINFORCE：蒙特卡罗策略梯度
现在我们准备推导第一个策略梯度学习算法. 回想一下我们随机梯度上升的总体策略（13.1），它需要一种获取样本的方法，使得样本梯度的期望与性能度量关于参数的实际梯度成比例. 样本梯度只需要与梯度成比例，因为任何比例常数都可以被吸收到步长 $\alpha$ 中，而步长在其他方面是任意的. 策略梯度定理给出了一个与梯度成比例的精确表达式；所需要的只是某种采样方法，其期望等于或近似这个表达式. 注意，策略梯度定理的右边是对状态的求和，权重是目标策略 $\pi$ 下状态出现的频率；如果遵循策略 $\pi$ ，那么将以这些比例遇到状态. 因此：
$$\begin{aligned}\nabla J(\theta)&\propto\sum_{s}\mu(s)\sum_{a}q_{\pi}(s,a)\nabla\pi(a|s,\theta)\\&=\mathbb{E}_{\pi}\left[\sum_{a}q_{\pi}(S_{t},a)\nabla\pi(a|S_{t},\theta)\right]\end{aligned}$$

我们可以在此处停下来，将随机梯度上升算法（13.1）实例化为：
$$\theta_{t + 1}\doteq\theta_{t}+\alpha\sum_{a}\hat{q}(S_{t},a,w)\nabla\pi(a|S_{t},\theta)$$
其中 $\hat{q}$ 是对 $q_{\pi}$ 的某种学习到的近似. 这个算法被称为全动作方法，因为它的更新涉及所有动作，它很有前景，值得进一步研究，但我们目前感兴趣的是经典的REINFORCE算法（Williams, 1992），其在时间 $t$ 的更新只涉及 $A_{t}$ ，即时间 $t$ 实际采取的那个动作. 

我们通过与在（13.6）中引入 $S_{t}$ 相同的方式引入 $A_{t}$ 来继续推导REINFORCE算法——将对随机变量可能值的求和替换为在策略 $\pi$ 下的期望，然后对期望进行采样. 方程（13.6）涉及对动作的适当求和，但每一项并没有像在策略 $\pi$ 下的期望所需要的那样，由 $\pi(a|S_{t},\theta)$ 加权. 所以我们通过对求和项进行乘除 $\pi(a|S_{t},\theta)$ 来引入这样的加权，而不改变等式. 从（13.6）继续推导，我们有：

$$
\begin{array}{rlrl}\nabla J(\theta)&=\mathbb{E}_{\pi}\left[\sum_{a}\pi(a|S_{t},\theta)q_{\pi}(S_{t},a)\frac{\nabla\pi(a|S_{t},\theta)}{\pi(a|S_{t},\theta)}\right]\\&=\mathbb{E}_{\pi}\left[q_{\pi}(S_{t},A_{t})\frac{\nabla\pi(A_{t}|S_{t},\theta)}{\pi(A_{t}|S_{t},\theta)}\right]\quad(用样本 A_{t}\sim\pi 替换 a )\\&=\mathbb{E}_{\pi}\left[G_{t}\frac{\nabla\pi(A_{t}|S_{t},\theta)}{\pi(A_{t}|S_{t},\theta)}\right]\quad(因为 \mathbb{E}_{\pi}[G_{t}|S_{t},A_{t}]=q_{\pi}(S_{t},A_{t}) )\end{array}
$$

其中 $G_{t}$ 是通常的回报. 最后括号中的表达式正是我们所需要的，它是一个可以在每个时间步进行采样的量，其期望等于梯度. 使用这个样本实例化我们的通用随机梯度上升算法（13.1），得到REINFORCE更新：
$$\theta_{t + 1}\doteq\theta_{t}+\alpha G_{t}\frac{\nabla\pi(A_{t}|S_{t},\theta_{t})}{\pi(A_{t}|S_{t},\theta_{t})}$$

这个更新具有直观的吸引力. 每次增量都与回报 $G_{t}$ 和一个向量的乘积成比例，这个向量是实际采取动作的概率的梯度除以采取该动作的概率. 这个向量是参数空间中使未来访问状态 $S_{t}$ 时重复动作 $A_{t}$ 的概率增加最大的方向. 更新会使参数向量在这个方向上按与回报成比例、与动作概率成反比的量增加. 前者是有意义的，因为它使参数朝着有利于产生最高回报的动作的方向移动得最多. 后者也是有意义的，因为否则频繁被选择的动作会具有优势（更新会更频繁地朝着它们的方向进行），即使它们不会产生最高回报，也可能胜出. 

注意，REINFORCE使用从时间 $t$ 开始的完整回报，其中包括直到情节结束的所有未来奖励. 从这个意义上说，REINFORCE是一种蒙特卡罗算法，并且仅在情节式情况下有明确的定义，所有更新都是在情节完成后回顾性地进行（就像第5章中的蒙特卡罗算法一样）. 下一页框中的算法明确展示了这一点. 

注意，伪代码最后一行的更新与REINFORCE更新规则（13.8）看起来有很大不同. 一个区别是，伪代码使用紧凑表达式 $\nabla\ln\pi(A_{t}|S_{t},\theta_{t})$ 来表示（13.8）中的分数向量 $\frac{\nabla\pi(A_{t}|S_{t},\theta_{t})}{\pi(A_{t}|S_{t},\theta_{t})}$ . 这两个向量表达式是等价的，这可以从恒等式 $\frac{\nabla x}{x}$推导得出. 在文献中，这个向量有多种名称和表示方法；我们简单地称它为资格向量. 注意，它是算法中唯一出现策略参数化的地方. 
### REINFORCE：蒙特卡罗策略梯度控制（情节式）求 $\pi_*$
输入：可微的策略参数化 $\pi(a|s, \theta)$
算法参数：步长 $\alpha > 0$
初始化策略参数 $\theta \in \mathbb{R}^{d'}$（例如，初始化为0）
无限循环（对于每个情节）：
 - 按照策略 $\pi(·|·, \theta)$ 生成一个情节 $S_0, A_0, R_1, \ldots, S_{T - 1}, A_{T - 1}, R_T$
 - 对于情节中的每个时间步 $t = 0, 1, \ldots, T - 1$：
    - $G \leftarrow \sum_{k=t + 1}^{T} \gamma^{k - t - 1}R_k$（计算 $G_t$）
    - $\theta \leftarrow \theta + \alpha \gamma^{t}G \nabla \ln \pi(A_t|S_t, \theta)$

伪代码中的更新和REINFORCE更新公式（13.8）的第二个区别在于，前者包含一个 $\gamma^{t}$ 因子. 这是因为，如前所述，在正文中我们处理的是无折扣情况（$\gamma = 1$），而在框中的算法中我们给出的是一般折扣情况下的算法. 在折扣情况下，所有的思路经过适当调整后仍然适用（包括对第199页内容的调整），但会涉及额外的复杂性，分散对主要思想的关注. 
### 练习13.2
推广第199页的内容、策略梯度定理（13.5）、策略梯度定理的证明（第325页），以及推导REINFORCE更新公式（13.8）的步骤，使得（13.8）最终包含一个 $\gamma^{t}$ 因子，从而与伪代码中给出的一般算法保持一致. 

图13.1展示了REINFORCE在示例13.1的短走廊网格世界中的性能. 
[此处插入图13.1：短走廊网格世界上的REINFORCE（示例13.1）. 在合适的步长下，每情节的总奖励接近起始状态的最优值]

## 13.4 带基线的REINFORCE
作为一种随机梯度方法，REINFORCE具有良好的理论收敛性. 从构造上看，一个情节内的期望更新方向与性能梯度方向一致. 这确保了对于足够小的 $\alpha$，期望性能会有所提升，并且在标准随机逼近条件下，随着 $\alpha$ 逐渐减小，算法会收敛到局部最优解 . 然而，作为一种蒙特卡罗方法，REINFORCE的方差可能较高，因此学习速度较慢. 
### 练习13.3
在13.1节中，我们考虑了使用基于动作偏好的soft - max（13.2）和线性动作偏好（13.3）的策略参数化. 对于这种参数化，利用定义和基础微积分证明资格向量为：
$$\nabla \ln \pi(a | s, \theta)=x(s, a)-\sum_{b} \pi(b | s, \theta) x(s, b)$$
### 带基线的REINFORCE
策略梯度定理（13.5）可以推广，将动作价值与任意基线 $b(s)$ 进行比较：
$$\nabla J(\theta) \propto \sum_{s} \mu(s) \sum_{a}\left(q_{\pi}(s, a)-b(s)\right) \nabla \pi(a | s, \theta)$$
基线可以是任何函数，甚至是随机变量，只要它不随动作 $a$ 变化；该等式仍然成立，因为被减去的量为零：
$$\sum_{a} b(s) \nabla \pi(a | s, \theta)=b(s) \nabla \sum_{a} \pi(a | s, \theta)=b(s) \nabla 1=0$$
带基线的策略梯度定理（13.10）可以用于推导更新规则，其步骤与上一节类似. 我们最终得到的更新规则是一个包含一般基线的REINFORCE新版本：
$$\theta_{t + 1} \doteq \theta_{t}+\alpha\left(G_{t}-b\left(S_{t}\right)\right) \frac{\nabla \pi\left(A_{t} | S_{t}, \theta_{t}\right)}{\pi\left(A_{t} | S_{t}, \theta_{t}\right)}$$
因为基线可以恒为零，所以这个更新是REINFORCE的严格推广. 一般来说，基线不会改变更新的期望值，但它对更新的方差可能有很大影响. 例如，我们在2.8节中看到，类似的基线可以显著降低梯度老虎机算法的方差（从而加快学习速度）. 在老虎机算法中，基线只是一个数字（到目前为止观察到的奖励的平均值），但对于马尔可夫决策过程（MDP），基线应该随状态变化. 在某些状态下，所有动作的价值都很高，我们需要一个较高的基线来区分价值较高的动作和价值较低的动作；在其他状态下，所有动作的价值都很低，较低的基线才合适. 

一个自然的基线选择是状态价值的估计值 $\hat{v}(S_{t}, w)$，其中 $w \in \mathbb{R}^{d}$ 是通过前面章节介绍的方法之一学习得到的权重向量. 由于REINFORCE是一种用于学习策略参数 $\theta$ 的蒙特卡罗方法，使用蒙特卡罗方法来学习状态价值权重 $w$ 似乎也很自然. 下面的框中给出了使用这样一个学习到的状态价值函数作为基线的带基线REINFORCE的完整伪代码算法. 
### 带基线的REINFORCE（情节式），用于估计 $\pi_{\theta} \approx \pi_{*}$
输入：可微的策略参数化 $\pi(a | s, \theta)$
输入：可微的状态价值函数参数化 $\hat{v}(s, w)$
算法参数：步长 $\alpha^{\theta} > 0$，$\alpha^{w} > 0$
初始化策略参数 $\theta \in \mathbb{R}^{d'}$ 和状态价值权重 $w \in \mathbb{R}^{d}$（例如，初始化为0）
无限循环（对于每个情节）：
 - 按照策略 $\pi(·|·, \theta)$ 生成一个情节 $S_0, A_0, R_1, \ldots, S_{T - 1}, A_{T - 1}, R_T$
 - 对于情节中的每个时间步 $t = 0, 1, \ldots, T - 1$：
    - $G \leftarrow \sum_{k=t + 1}^{T} \gamma^{k - t - 1}R_k$（计算 $G_t$）
    - $\delta \leftarrow G - \hat{v}(S_{t}, w)$
    - $w \leftarrow w + \alpha^{w} \delta \nabla \hat{v}(S_{t}, w)$
    - $\theta \leftarrow \theta + \alpha^{\theta} \gamma^{t} \delta \nabla \ln \pi(A_{t} | S_{t}, \theta)$

这个算法有两个步长，分别表示为 $\alpha^{\theta}$ 和 $\alpha^{w}$（其中 $\alpha^{\theta}$ 是（13.11）中的 $\alpha$）. 选择价值的步长（这里是 $\alpha^{w}$）相对容易；在线性情况下，我们有设置它的经验法则，例如 $\alpha^{w} = 0.1 / \mathbb{E}[\|\nabla \hat{v}(S_{t}, w)\|_{\mu}^{2}]$（见9.6节）. 而如何设置策略参数的步长 $\alpha^{\theta}$ 则不太明确，其最佳值取决于奖励的变化范围和策略参数化方式. 
[此处插入图13.2：添加基线可以使REINFORCE学习速度更快，如在短走廊网格世界（示例13.1）中所示. 这里普通REINFORCE使用的步长是其表现最佳的步长（最接近2的幂次方；见图13.1）]

图13.2比较了带基线和不带基线的REINFORCE在短走廊网格世界（示例13.1）中的表现. 这里基线中使用的近似状态价值函数是 $\hat{v}(s, w) = w$，也就是说，$w$ 是一个单分量的变量. 

## 13.5 演员 - 评论家方法
尽管带基线的REINFORCE方法同时学习策略和状态价值函数，但我们不认为它是一种演员 - 评论家方法，因为它的状态价值函数仅用作基线，而不是作为评论家. 也就是说，它不用于自举（从后续状态的估计值更新一个状态的价值估计），而仅作为正在更新估计值的状态的基线. 这是一个有用的区分，因为只有通过自举，我们才会引入偏差，并且渐近地依赖于函数近似的质量. 正如我们所看到的，通过自举和依赖状态表示引入的偏差通常是有益的，因为它减少了方差并加速了学习. 带基线的REINFORCE是无偏的，并且会渐近地收敛到局部最小值，但与所有蒙特卡罗方法一样，它往往学习缓慢（产生高方差的估计），并且在在线实现或处理持续问题时不太方便 . 正如我们在本书前面所看到的，使用时间差分方法可以消除这些不便，并且通过多步方法，我们可以灵活地选择自举的程度. 为了在策略梯度方法中获得这些优势，我们使用带有自举评论家的演员 - 评论家方法. 

首先考虑单步演员 - 评论家方法，它类似于第6章中介绍的时间差分（TD）方法，如TD(0)、Sarsa(0)和Q学习. 单步方法的主要吸引力在于它们是完全在线和增量式的，同时避免了资格迹的复杂性. 它们是资格迹方法的一种特殊情况，虽然通用性稍差，但更易于理解. 单步演员 - 评论家方法用单步回报替换REINFORCE（13.11）中的完整回报（并使用学习到的状态价值函数作为基线），如下所示：
$$\begin{aligned} \theta_{t + 1} & \doteq \theta_{t}+\alpha\left(G_{t:t + 1}-\hat{v}\left(S_{t}, w\right)\right) \frac{\nabla \pi\left(A_{t} | S_{t}, \theta_{t}\right)}{\pi\left(A_{t} | S_{t}, \theta_{t}\right)} \\ & =\theta_{t}+\alpha\left(R_{t + 1}+\gamma \hat{v}\left(S_{t + 1}, w\right)-\hat{v}\left(S_{t}, w\right)\right) \frac{\nabla \pi\left(A_{t} | S_{t}, \theta_{t}\right)}{\pi\left(A_{t} | S_{t}, \theta_{t}\right)} \\ & =\theta_{t}+\alpha \delta_{t} \frac{\nabla \pi\left(A_{t} | S_{t}, \theta_{t}\right)}{\pi\left(A_{t} | S_{t}, \theta_{t}\right)} \end{aligned}$$
与之自然配对的状态价值函数学习方法是半梯度TD(0). 下一页顶部的框中给出了完整算法的伪代码. 注意，它现在是一个完全在线、增量式的算法，状态、动作和奖励在出现时进行处理，之后不再访问. 
### 单步演员 - 评论家（情节式），用于估计 $\pi_{\theta} \approx \pi_{*}$
输入：可微的策略参数化 $\pi(a|s, \theta)$
输入：可微的状态价值函数参数化 $\hat{v}(s,w)$
参数：步长 $\alpha^{\theta} > 0$，$\alpha^{w} > 0$
初始化策略参数 $\theta \in \mathbb{R}^{d'}$ 和状态价值权重 $w \in \mathbb{R}^{d}$（例如，初始化为0）
无限循环（对于每个情节）：
 - 初始化 $S$（情节的第一个状态），$I \leftarrow 1$
 - 当 $S$ 不是终止状态时循环（对于每个时间步）：
    - 采取动作 $A$，观察 $S'$，$R$：$A \sim \pi(·|S, \theta)$
    - $\delta \leftarrow R + \gamma \hat{v}(S',w) - \hat{v}(S,w)$（如果 $S'$ 是终止状态，则 $\hat{v}(S',w) = 0$）
    - $w \leftarrow w + \alpha^{w}\delta\nabla\hat{v}(S,w)$
    - $\theta \leftarrow \theta + \alpha^{\theta}I\delta\nabla\ln \pi(A|S, \theta)$
    - $I \leftarrow \gamma I$，$S \leftarrow S'$

向n步方法的前向视图以及 $\lambda$ - 回报算法的推广很直接. （13.12）中的单步回报分别简单地被 $G_{t:t + n}$ 或 $G_{t}^{\lambda}$ 替代. $\lambda$ - 回报算法的后向视图也很直接，为演员和评论家分别使用单独的资格迹，每个都遵循第12章中的模式. 下面的框中给出了完整算法的伪代码. 
### 带资格迹的演员 - 评论家（情节式），用于估计 $\pi_{\theta} \approx \pi_{*}$
输入：可微的策略参数化 $\pi(a|s, \theta)$
输入：可微的状态价值函数参数化 $\hat{v}(s,w)$
参数：迹衰减率 $\lambda^{\theta} \in [0, 1]$，$\lambda^{w} \in [0, 1]$；步长 $\alpha^{\theta} > 0$，$\alpha^{w} > 0$
初始化策略参数 $\theta \in \mathbb{R}^{d'}$ 和状态价值权重 $w \in \mathbb{R}^{d}$（例如，初始化为0）
无限循环（对于每个情节）：
 - 初始化 $S$（情节的第一个状态）
 - $z^{\theta} \leftarrow 0$（$d'$ 分量资格迹向量）
 - $z^{w} \leftarrow 0$（$d$ 分量资格迹向量）
 - $I \leftarrow 1$
 - 当 $S$ 不是终止状态时循环（对于每个时间步）：
    - 采取动作 $A$，观察 $S'$，$R$：$A \sim \pi(·|S, \theta)$
    - $\delta \leftarrow R + \gamma \hat{v}(S',w) - \hat{v}(S,w)$（如果 $S'$ 是终止状态，则 $\hat{v}(S',w) = 0$）
    - $z^{w} \leftarrow \gamma\lambda^{w}z^{w} + \nabla\hat{v}(S,w)$
    - $z^{\theta} \leftarrow \gamma\lambda^{\theta}z^{\theta} + I\nabla\ln \pi(A|S, \theta)$
    - $w \leftarrow w + \alpha^{w}\delta z^{w}$
    - $\theta \leftarrow \theta + \alpha^{\theta}\delta z^{\theta}$
    - $I \leftarrow \gamma I$
    - $S \leftarrow S'$

## 13.6 持续问题的策略梯度
如10.3节所讨论的，对于没有情节边界的持续问题，我们需要根据每时间步的平均奖励率来定义性能：
$$\begin{aligned} J(\theta) \doteq r(\pi) & \doteq \lim_{h \to \infty} \frac{1}{h} \sum_{t = 1}^{h} \mathbb{E}[R_{t} | S_{0}, A_{0:t - 1} \sim \pi] \\ & = \lim_{t \to \infty} \mathbb{E}[R_{t} | S_{0}, A_{0:t - 1} \sim \pi] \\ & = \sum_{s} \mu(s) \sum_{a} \pi(a | s) \sum_{s', r} p(s', r | s, a) r \end{aligned}$$
其中 $\mu$ 是在策略 $\pi$ 下的稳态分布，$\mu(s) \doteq \lim_{t \to \infty} Pr\{S_{t} = s | A_{0:t} \sim \pi\}$，假设其存在且与 $S_{0}$ 无关（遍历性假设）. 请记住，这是一种特殊的分布，在这种分布下，如果你按照策略 $\pi$ 选择动作，你将保持在相同的分布中：
$$\sum_{s} \mu(s) \sum_{a} \pi(a | s, \theta) p(s' | s, a)=\mu(s'), \quad \forall s' \in \mathcal{S}$$

下面的框中给出了持续情况下（后向视图）演员 - 评论家算法的完整伪代码. 
### 带资格迹的演员 - 评论家（持续式），用于估计 $\pi_{\theta} \approx \pi_{*}$
输入：可微的策略参数化 $\pi(a|s, \theta)$
输入：可微的状态价值函数参数化 $\hat{v}(s,w)$
算法参数：$\lambda^{w} \in [0, 1]$，$\lambda^{\theta} \in [0, 1]$，$\alpha^{w} > 0$，$\alpha^{\theta} > 0$，$\alpha_{\bar{R}} > 0$
初始化 $\bar{R} \in \mathbb{R}$（例如，初始化为0）
初始化状态价值权重 $w \in \mathbb{R}^{d

和策略参数 $\theta\in\mathbb{R}^{d'}$ （例如，初始化为0）
初始化 $S\in\mathcal{S}$ （例如，初始化为 $s_0$ ）
 $z^w\leftarrow0$ （ $d$ 分量资格迹向量）
 $z^\theta\leftarrow0$ （ $d'$ 分量资格迹向量）
无限循环（对于每个时间步）：
 -  $A\sim\pi(\cdot|S,\theta)$ ，采取动作 $A$ ，观察 $S'$ ， $R$ 
 -  $\delta\leftarrow R-\bar{R}+\hat{v}(S',w)-\hat{v}(S,w)$ 
 -  $\bar{R}\leftarrow\bar{R}+\alpha_{\bar{R}}\delta$ 
 -  $z^w\leftarrow\lambda^wz^w+\nabla\hat{v}(S,w)$ 
 -  $z^\theta\leftarrow\lambda^\theta z^\theta+\nabla\ln\pi(A|S,\theta)$ 
 -  $w\leftarrow w+\alpha^w\delta z^w$ 
 -  $\theta\leftarrow\theta+\alpha^\theta\delta z^\theta$ 
 -  $S\leftarrow S'$ 

自然地，在持续情况下，我们根据微分回报定义价值 $v_{\pi}(s)\doteq\mathbb{E}_{\pi}[G_{t}|S_{t}=s]$ 和 $q_{\pi}(s,a)\doteq\mathbb{E}_{\pi}[G_{t}|S_{t}=s,A_{t}=a]$ ：
$$G_{t}\doteq R_{t + 1}-r(\pi)+R_{t + 2}-r(\pi)+R_{t + 3}-r(\pi)+\cdots$$

有了这些替代定义，情节式情况下给出的策略梯度定理（13.5）对于持续情况仍然成立. 下一页框中给出了证明. 前向和后向视图方程也保持不变. 
### 策略梯度定理（持续情况）的证明
持续情况下策略梯度定理的证明与情节式情况类似. 同样，在所有情况下我们都隐含地认为 $\pi$ 是 $\theta$ 的函数，并且梯度是关于 $\theta$ 的. 回想在持续情况下 $J(\theta)=r(\pi)$ （13.15），并且 $v_{\pi}$ 和 $q_{\pi}$ 表示关于微分回报的价值（13.17）. 对于任何 $s\in\mathcal{S}$ ，状态价值函数的梯度可以写为：
$$\begin{aligned}
\nabla v_{\pi}(s)&=\nabla\left[\sum_{a}\pi(a|s)q_{\pi}(s,a)\right]\\
&=\sum_{a}\left[\nabla\pi(a|s)q_{\pi}(s,a)+\pi(a|s)\nabla q_{\pi}(s,a)\right]（微积分乘积法则）\\
&=\sum_{a}\left[\nabla\pi(a|s)q_{\pi}(s,a)+\pi(a|s)\nabla\sum_{s',r}p(s',r|s,a)(r - r(\theta)+v_{\pi}(s'))\right]\\
&=\sum_{a}\left[\nabla\pi(a|s)q_{\pi}(s,a)+\pi(a|s)\left[-\nabla r(\theta)+\sum_{s'}p(s'|s,a)\nabla v_{\pi}(s')\right]\right]
\end{aligned}$$

经过重新整理项，我们得到：
$$\nabla r(\theta)=\sum_{a}\left[\nabla\pi(a|s)q_{\pi}(s,a)+\pi(a|s)\sum_{s'}p(s'|s,a)\nabla v_{\pi}(s')\right]-\nabla v_{\pi}(s)$$

注意，左边可以写为 $\nabla J(\theta)$ ，并且它不依赖于 $s$ . 因此右边也不依赖于 $s$ ，我们可以安全地对所有 $s\in\mathcal{S}$ 进行求和，并用 $\mu(s)$ 加权，而不改变它（因为 $\sum_{s}\mu(s)=1$ ）. 
$$\begin{aligned}
\nabla J(\theta)&=\sum_{s}\mu(s)\left(\sum_{a}\left[\nabla\pi(a|s)q_{\pi}(s,a)+\pi(a|s)\sum_{s'}p(s'|s,a)\nabla v_{\pi}(s')\right]-\nabla v_{\pi}(s)\right)\\
&=\sum_{s}\mu(s)\sum_{a}\nabla\pi(a|s)q_{\pi}(s,a)\\
&\quad+\sum_{s}\mu(s)\sum_{a}\pi(a|s)\sum_{s'}p(s'|s,a)\nabla v_{\pi}(s')-\sum_{s}\mu(s)\nabla v_{\pi}(s)\\
&=\sum_{s}\mu(s)\sum_{a}\nabla\pi(a|s)q_{\pi}(s,a)\\
&\quad+\sum_{s'}\underbrace{\sum_{s}\mu(s)\sum_{a}\pi(a|s)p(s'|s,a)}_{\mu(s') \text{ 由(13.16)}}\nabla v_{\pi}(s')-\sum_{s}\mu(s)\nabla v_{\pi}(s)\\
&=\sum_{s}\mu(s)\sum_{a}\nabla\pi(a|s)q_{\pi}(s,a)+\sum_{s'}\mu(s')\nabla v_{\pi}(s')-\sum_{s}\mu(s)\nabla v_{\pi}(s)\\
&=\sum_{s}\mu(s)\sum_{a}\nabla\pi(a|s)q_{\pi}(s,a) . 证毕
\end{aligned}$$

## 13.7 连续动作的策略参数化
基于策略的方法为处理大型动作空间提供了实用的方式，甚至对于具有无限个动作的连续空间也适用. 我们不是为众多动作中的每一个计算学习到的概率，而是学习概率分布的统计信息. 例如，动作集可能是实数集，动作从正态（高斯）分布中选取. 

正态分布的概率密度函数通常写为：
$$p(x)\doteq\frac{1}{\sigma\sqrt{2\pi}}\exp\left(-\frac{(x - \mu)^2}{2\sigma^2}\right)$$
[此处插入正态分布概率密度函数图像，展示不同均值和标准差的情况]

图中展示了几种不同均值和标准差的概率密度函数. 这里 $p(x)$ 是 $x$ 处的概率密度，而不是概率，它可以大于1；是 $p(x)$ 下方的总面积必须为1. 一般来说，可以对 $p(x)$ 在任何 $x$ 值范围内进行积分，以得到 $x$ 落在该范围内的概率. 

为了生成策略参数化，可以将策略定义为实值标量动作上的正态概率密度，其均值和标准差由依赖于状态的参数化函数逼近器给出. 即：
$$\pi(a|s,\theta)\doteq\frac{1}{\sigma(s,\theta)\sqrt{2\pi}}\exp\left(-\frac{(a - \mu(s,\theta))^2}{2\sigma(s,\theta)^2}\right)$$
其中 $\mu:S\times\mathbb{R}^{d'}\to\mathbb{R}$ 和 $\sigma:S\times\mathbb{R}^{d'}\to\mathbb{R}^{+}$ 是两个参数化函数逼近器. 

为了完成这个例子，我们只需要给出这些逼近器的形式. 为此，我们将策略的参数向量 $\theta$ 分为两部分， $\theta=[\theta_{\mu},\theta_{\sigma}]^{\top}$ ，一部分用于逼近均值，另一部分用于逼近标准差 . 均值可以用线性函数逼近，标准差必须始终为正，用线性函数的指数形式逼近更好. 因此：
$$\mu(s,\theta)\doteq\theta_{\mu}^{\top}x_{\mu}(s) \quad\text{且}\quad \sigma(s,\theta)\doteq\exp\left(\theta_{\sigma}^{\top}x_{\sigma}(s)\right)$$
其中 $x_{\mu}(s)$ 和 $x_{\sigma}(s)$ 是状态特征向量，可能通过9.5节中描述的方法之一构建. 有了这些定义，本章其余部分描述的所有算法都可以应用于学习选择实值动作. 
### 练习13.4
证明对于高斯策略参数化（13.19），资格向量有以下两部分：
$$\nabla\ln\pi(a|s,\theta_{\mu})=\frac{\nabla\pi(a|s,\theta_{\mu})}{\pi(a|s,\theta)}=\frac{1}{\sigma(s,\theta)^2}(a - \mu(s,\theta))x_{\mu}(s)$$
$$\nabla\ln\pi(a|s,\theta_{\sigma})=\frac{\nabla\pi(a|s,\theta_{\sigma})}{\pi(a|s,\theta)}=\left(\frac{(a - \mu(s,\theta))^2}{\sigma(s,\theta)^2}-1\right)x_{\sigma}(s)$$
### 练习13.5
伯努利 - 逻辑单元是一种在某些人工神经网络（9.6节）中使用的随机神经元样单元. 它在时间 $t$ 的输入是特征向量 $x(S_{t})$ ；其输出 $A_{t}$ 是一个随机变量，有两个值0和1， $Pr\{A_{t}=1\}=P_{t}$ 且 $Pr\{A_{t}=0\}=1 - P_{t}$ （伯努利分布）. 设 $h(s,0,\theta)$ 和 $h(s,1,\theta)$ 是在状态 $s$ 下该单元两个动作的偏好，给定策略参数 $\theta$ . 假设动作偏好之间的差异由单元输入向量的加权和给出，即假设 $h(s,1,\theta)-h(s,0,\theta)=\theta^{\top}x(s)$ ，其中 $\theta$ 是单元的权重向量. 
 - （a）证明如果使用指数soft - max分布（13.2）将动作偏好转换为策略，那么 $P_{t}=\pi(1|S_{t},\theta_{t})=\frac{1}{1+\exp(-\theta_{t}^{\top}x(S_{t}))}$ （逻辑函数）. 
 - （b）在收到回报 $G_{t}$ 时， $\theta_{t}$ 到 $\theta_{t + 1}$ 的蒙特卡罗REINFORCE更新是什么？
 - （c）通过计算梯度，用 $a$ 、 $x(s)$ 和 $\pi(a|s,\theta)$ 表示伯努利 - 逻辑单元的资格 $\nabla\ln\pi(a|s,\theta)$ . 
提示（c部分）：定义 $P = \pi(1|s,\theta)$ ，对每个动作使用关于 $P$ 的链式法则计算对数的导数. 将两个结果合并为一个依赖于 $a$ 和 $P$ 的表达式，然后再次使用链式法则，这次是关于 $\theta^{\top}x(s)$ ，注意逻辑函数 $f(x)=\frac{1}{1 + e^{-x}}$ 的导数是 $f(x)(1 - f(x))$  . 

## 13.8 总结
在本章之前，本书主要关注动作价值方法，即学习动作价值并利用它们来确定动作选择的方法. 另一方面，在本章中，我们考虑了学习参数化策略的方法，这些策略使得在不参考动作价值估计的情况下就能采取行动. 特别地，我们研究了策略梯度方法，即在每一步朝着性能关于策略参数的梯度估计方向更新策略参数的方法. 

学习并存储策略参数的方法具有许多优势. 它们可以学习采取动作的特定概率，能够学习适当的探索水平并渐近地接近确定性策略，还可以自然地处理连续动作空间. 所有这些对于基于策略的方法来说都很容易，但对于 $\epsilon$  - 贪婪方法和一般的动作价值方法来说则很棘手甚至无法实现. 此外，在某些问题中，用参数表示策略比表示价值函数更简单；这些问题更适合使用参数化策略方法. 

参数化策略方法相对于动作价值方法还有一个重要的理论优势，即策略梯度定理. 该定理给出了一个精确的公式，说明性能如何受策略参数的影响，且不涉及状态分布的导数. 这个定理为所有策略梯度方法提供了理论基础. 

REINFORCE方法直接源于策略梯度定理. 添加状态价值函数作为基线可以在不引入偏差的情况下降低REINFORCE的方差. 将状态价值函数用于自举会引入偏差，但通常是可取的，原因与自举的时间差分方法通常优于蒙特卡罗方法相同（大幅降低方差）. 状态价值函数对策略的动作选择进行“评价”（批评），因此前者被称为评论家，后者被称为演员，这些方法整体被称为演员 - 评论家方法. 

总体而言，策略梯度方法与动作价值方法相比，具有明显不同的优缺点. 如今，在某些方面它们还没有被完全理解，但它们是一个令人兴奋且正在进行研究的领域. 
## 文献和历史注释
我们现在视为与策略梯度相关的方法，实际上是强化学习（Witten, 1977; Barto, Sutton, and Anderson, 1983; Sutton, 1984; Williams, 1987, 1992）及相关前身领域（见Phansalkar and Thathachar, 1995）中最早研究的一些方法. 在20世纪90年代，它们在很大程度上被本书其他章节重点介绍的动作价值方法所取代. 然而近年来，人们的注意力又回到了演员 - 评论家方法以及一般的策略梯度方法上. 除了我们在这里介绍的内容之外，进一步的发展还包括自然梯度方法（Amari, 1998; Kakade, 2002; Peters, Vijayakumar and Schaal, 2005; Peters and Schaal, 2008; Park, Kim and Kang, 2005; Bhatnagar, Sutton, Ghavamzadeh and Lee, 2009; 见Grondman, Busoniu, Lopes and Babuska, 2012）、确定性策略梯度方法 .  