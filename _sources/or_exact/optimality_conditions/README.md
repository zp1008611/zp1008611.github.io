# 最优性条件

## 1 凸集与凸函数
### 1.1 凸集
**定义1.1（凸集）**：$\mathbb{R}^{n}$的子集$C$被称为凸集，当且仅当对于所有的$x, y \in C$和所有的$\lambda \in [0, 1]$，都有
$$\lambda x+(1-\lambda) y \in C$$
**定义1.2（凸组合）**：给定$x_{1}, \ldots, x_{m} \in \mathbb{R}^{n}$，形如$x = \sum_{i = 1}^{m} \lambda_{i} x_{i}$的元素，其中$\sum_{i = 1}^{m} \lambda_{i} = 1$且$\lambda_{i} \geq 0$，被称为$x_{1}, \ldots, x_{m}$的凸组合。
**命题1.3**：$\mathbb{R}^{n}$的子集$C$是凸集，当且仅当它包含其元素的所有凸组合。
### 1.2 凸函数
在本小节中，我们将考虑扩展实值函数，其取值范围为$\overline{\mathbb{R}} := (-\infty, \infty]$，并遵循以下约定：对于所有的$a \in \mathbb{R}$，$a + \infty = \infty$；$\infty + \infty = \infty$；对于所有的$t > 0$，$t \cdot \infty = \infty$。
**定义1.4（凸函数）**：设$C$是$\mathbb{R}^{n}$的凸子集。函数$f: C \mapsto \overline{\mathbb{R}}$在$C$上被称为凸函数，当且仅当对于所有的$x, y \in C$和所有的$\lambda \in [0, 1]$，都有
$$f(\lambda x+(1-\lambda) y) \leq \lambda f(x)+(1-\lambda) f(y)$$
**定义1.5（上境图和有效定义域）**：函数$f: X \to [-\infty, \infty]$（其中$X \subset \mathbb{R}^{n}$）的上境图为
$$epi f=\left\{(x, w) | x \in X, w \in \mathbb{R}, f(x) \leq w\right\}$$
$f$的有效定义域为
$$dom f=\{x | f(x)<\infty\}$$
**定义1.6（严格凸函数）**：（文档未给出具体定义内容）
**定义1.7（强凸函数）**：（文档未给出具体定义内容）
**定义1.8（正常函数）**：函数$f$是正常的，如果至少存在一个$x \in X$，使得$f(x) < \infty$。从考虑上境图$epi f$的角度来看，这意味着$epi f$非空且不包含任何垂直线。如果$f$不是正常函数，则称其为非正常函数。
**定理1.9（詹森不等式）**：函数$f: \mathbb{R}^{n} \to \overline{\mathbb{R}}$是凸函数，当且仅当对于任意的$\lambda_{i} \geq 0$（满足$\sum \lambda_{i} = 1$）和任意的元素$x_{i} \in \mathbb{R}^{n}$，都有
$$f\left(\sum \lambda_{i} x_{i}\right) \leq \sum \lambda_{i} f\left(x_{i}\right)$$
**命题1.10**：函数$f: \mathbb{R}^{n} \to \overline{\mathbb{R}}$是凸函数，当且仅当$epi f \subset \mathbb{R}^{n + 1}$是凸集。
**定义1.11（闭函数）**：如果函数$f: X \to \overline{\mathbb{R}}$的上境图是闭集，我们称$f$是闭函数。

现在，我们给出一些可微或二阶可微函数的凸性特征。
**命题1.12**：设$C$是一个非空的凸开集。设$f: \mathbb{R}^{n} \to \mathbb{R}$在包含$C$的开集上可微，那么$f$是凸函数，当且仅当对于所有的$x, z \in C$，都有
$$f(z) \geq f(x)+\langle \nabla f(x), z - x\rangle$$
**命题1.13**：设$C$是$\mathbb{R}^{n}$中的非空凸集，且$f: \mathbb{R}^{n} \to \mathbb{R}$在包含$C$的开集上二阶可微。如果对于所有的$x \in C$，$\nabla^{2} f(x)$都是半正定的，那么$f$在$C$上是凸函数。
### 1.3 投影到凸集
给定一个集合$C \subseteq \mathbb{R}^{n}$，点$x$到$C$的距离定义为
$$d(x ; C):=\inf \{\| x - y\| : y \in C\}$$
对于闭凸集，有一个重要的投影性质如下。
**命题1.14（投影性质）**：设$C$是$\mathbb{R}^{n}$的非空闭凸子集。对于每个$x \in \mathbb{R}^{n}$，存在唯一的$w \in C$，使得
$$\| x - w\| =d(x ; C)$$
$w$被称为$x$到$C$的投影，记为$P_{C}(x)$。
**命题1.15**：设$C$是一个非空闭凸集，那么$w = P_{C}(x)$当且仅当对于所有的$u \in C$，都有
$$\langle x - w, u - w\rangle \leq 0$$
## 2 凸集的法锥和切锥
**定义2.1（锥）**：集合$C$是一个锥，如果对于任意的$x \in C$和$0 < \lambda \in \mathbb{R}$，都有$\lambda x \in C$。锥$C$的极锥（记为$C^{\circ}$）定义为
$$C^{\circ}=\{\sigma:\langle\sigma, x\rangle \leq 0 \text{ 对于所有的 } x \in C\}$$
假设$\Omega \subseteq \mathbb{R}^{n}$是一个凸集。那么对于$x \in \Omega$，我们可以定义$\Omega$在$x$处的法锥为
$$N_{\Omega}(x)=\{z \in \mathbb{R}^{n}:\langle z, y - x\rangle \leq 0 \text{ 对于所有的 } y \in \Omega\}$$
对于凸集，我们可以定义$\Omega$在$x$处的切锥$T_{\Omega}(x)$为$N_{\Omega}(x)^{\circ}$。

**定理2.2**：对于问题$\min_{\Omega} f(x)$，如果$f$是光滑且凸的，$\Omega$是闭凸集，那么$-\nabla f(x^{*}) \in N_{\Omega}(x^{*})$意味着$x^{*}$是全局最优解。

## 3 次微分计算
### 3.1 凸函数的次梯度
在本小节中，我们引入凸函数次梯度这一关键概念。它作为非光滑函数的广义导数，在优化理论中有许多应用。

**定义3.1（次梯度）**：设$f: \mathbb{R}^{n} \to \overline{\mathbb{R}}$是一个凸函数，且$\bar{x} \in dom f$。元素$g \in \mathbb{R}^{n}$被称为$f$在$\bar{x}$处的次梯度，如果……（文档此处定义不完整）
凸函数$f$的所有次梯度的集合称为次微分。

**定理3.2（$f$的次梯度是$epi f$的支撑超平面）**：设$f$是一个凸函数，且$x \in dom f$。$g \in \partial f(x)$当且仅当$\begin{pmatrix} g \\ -1 \end{pmatrix}$定义了$epi f$在点$\begin{pmatrix} x \\ f(x) \end{pmatrix}$处的支撑超平面。

**命题3.3**：设$f$是一个凸函数，且$x \in int(dom f)$，那么$\partial f(x)$是非空且紧致的。

**命题3.4**：设$f: \mathbb{R}^{n} \to \overline{\mathbb{R}}$是凸函数，且在$x \in int(dom f)$处可微。那么$\partial f(x)=\{\nabla f(x)\}$。

**例3.5（$f(x) = |x|$的次梯度）**：$f(x) = |x|$在$\mathbb{R}$上是凸函数。当$x > 0$时，$f(x) = x$在$x$处可微，且$\nabla f(x) = 1$，所以$\partial f(x)=\{1\}$。当$x < 0$时，$f(x) = -x$在$x$处可微，且$\nabla f(x) = -1$，所以$\partial f(x)=\{-1\}$。当$x = 0$时，我们需要找到$g \in \mathbb{R}$，使得对于所有的$y \in \mathbb{R}$，都有$f(y) - f(0) \geq \langle g, y\rangle$。即对于所有的$y \in \mathbb{R}$，$|y| \geq gy \Rightarrow \frac{|y|}{y} \geq g \Rightarrow -1 \leq g \leq 1$，所以$\partial f(0)=[-1, 1]$。

**定理3.6（丹斯金定理）**：设$f$是凸函数，$Z$是一个紧致集，使得……（文档此处定理内容不完整）其中$\phi: int(dom f) \times Z \to \mathbb{R} \cup \{-\infty, +\infty\}$对于每个$z \in Z$都是一个扩展实值、闭、正常的凸函数。如果……（文档此处定理条件不完整）

### 3.2 方向导数
**定义3.7（方向导数）**：设$f: \mathbb{R}^{n} \to \overline{\mathbb{R}}$是一个函数，且$x \in dom f$。$f$在$x$处沿方向$d$的方向导数定义为……（文档此处定义不完整）
**定理3.8**：对于凸函数$f$和$x^{*} \in dom f$，$x^{*}$是极小值点当且仅当对于所有的$d$，都有$f'(x^{*} ; d) \geq 0$。
**命题3.9**：设$f$是凸函数且在$x$处可微，那么$f'(x ; d)=\langle \nabla f(x), d\rangle$。
**定理3.10（方向导数与次梯度的关系）**：对于凸函数$f$和$x \in int(dom f)$，对于任意的$d$，都有
$$f'(x ; d)=\sup _{g \in \partial f(x)}\langle g, d\rangle$$
### 3.3 次微分的计算
**定理3.11**：对于一个凸集$\Omega$，我们可以定义$\Omega$的无穷指示函数为
$$I_{\Omega}(x):=\begin{cases}0, & x \in \Omega \\+\infty, & x \notin \Omega\end{cases}$$
对于$x$在闭凸集$\Omega$中，$N_{\Omega}(x)=\partial I_{\Omega}(x)$。
## 4 最优性条件
我们关注求解如下问题：
$$\min _{x \in \Omega} f(x)$$
其中$f$是凸函数，$C$是凸集。
**最优性条件**：
1. **无约束情况**：如果$\Omega=\mathbb{R}^{n}$且$dom f=\mathbb{R}^{n}$，那么$x^{*}$是最优解当且仅当$0 \in \partial f(x^{*})$。
2. **有约束且可微情况**：现在假设$\Omega \subset \mathbb{R}^{n}$且$f$在$\Omega$中可微。可行点$x^{*}$是最优解当且仅当对于所有的$y \in \Omega$，都有$\langle \nabla f(x^{*}), y - x^{*}\rangle \geq 0$，这等价于$-\nabla f(x^{*}) \in N_{\Omega}(x^{*})$。
3. **一般有约束情况**：如果函数不可微，可行点$x^{*}$是最优解当且仅当$0 \in \partial f(x^{*})+N_{\Omega}(x^{*})$。 
