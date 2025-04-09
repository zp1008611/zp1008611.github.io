最优性条件
==========



1 凸集与凸函数

--------------



1.1 凸集

~~~~~~~~



**定义1.1（凸集）**\ ：\ :math:`\mathbb{R}^{n}`\ 的子集\ :math:`C`\ 被称为凸集，当且仅当对于所有的\ :math:`x, y \in C`\ 和所有的\ :math:`\lambda \in [0, 1]`\ ，都有



.. math:: \lambda x+(1-\lambda) y \in C



**定义1.2（凸组合）**\ ：给定\ :math:`x_{1}, \ldots, x_{m} \in \mathbb{R}^{n}`\ ，形如\ :math:`x = \sum_{i = 1}^{m} \lambda_{i} x_{i}`\ 的元素，其中\ :math:`\sum_{i = 1}^{m} \lambda_{i} = 1`\ 且\ :math:`\lambda_{i} \geq 0`\ ，被称为\ :math:`x_{1}, \ldots, x_{m}`\ 的凸组合。

**命题1.3**\ ：\ :math:`\mathbb{R}^{n}`\ 的子集\ :math:`C`\ 是凸集，当且仅当它包含其元素的所有凸组合。

### 1.2 凸函数

在本小节中，我们将考虑扩展实值函数，其取值范围为\ :math:`\overline{\mathbb{R}} := (-\infty, \infty]`\ ，并遵循以下约定：对于所有的\ :math:`a \in \mathbb{R}`\ ，\ :math:`a + \infty = \infty`\ ；\ :math:`\infty + \infty = \infty`\ ；对于所有的\ :math:`t > 0`\ ，\ :math:`t \cdot \infty = \infty`\ 。

**定义1.4（凸函数）**\ ：设\ :math:`C`\ 是\ :math:`\mathbb{R}^{n}`\ 的凸子集。函数\ :math:`f: C \mapsto \overline{\mathbb{R}}`\ 在\ :math:`C`\ 上被称为凸函数，当且仅当对于所有的\ :math:`x, y \in C`\ 和所有的\ :math:`\lambda \in [0, 1]`\ ，都有



.. math:: f(\lambda x+(1-\lambda) y) \leq \lambda f(x)+(1-\lambda) f(y)



**定义1.5（上境图和有效定义域）**\ ：函数\ :math:`f: X \to [-\infty, \infty]`\ （其中\ :math:`X \subset \mathbb{R}^{n}`\ ）的上境图为



.. math:: epi f=\left\{(x, w) | x \in X, w \in \mathbb{R}, f(x) \leq w\right\}



:math:`f`\ 的有效定义域为



.. math:: dom f=\{x | f(x)<\infty\}



**定义1.6（严格凸函数）**\ ：（文档未给出具体定义内容）

**定义1.7（强凸函数）**\ ：（文档未给出具体定义内容）

**定义1.8（正常函数）**\ ：函数\ :math:`f`\ 是正常的，如果至少存在一个\ :math:`x \in X`\ ，使得\ :math:`f(x) < \infty`\ 。从考虑上境图\ :math:`epi f`\ 的角度来看，这意味着\ :math:`epi f`\ 非空且不包含任何垂直线。如果\ :math:`f`\ 不是正常函数，则称其为非正常函数。

**定理1.9（詹森不等式）**\ ：函数\ :math:`f: \mathbb{R}^{n} \to \overline{\mathbb{R}}`\ 是凸函数，当且仅当对于任意的\ :math:`\lambda_{i} \geq 0`\ （满足\ :math:`\sum \lambda_{i} = 1`\ ）和任意的元素\ :math:`x_{i} \in \mathbb{R}^{n}`\ ，都有



.. math:: f\left(\sum \lambda_{i} x_{i}\right) \leq \sum \lambda_{i} f\left(x_{i}\right)



**命题1.10**\ ：函数\ :math:`f: \mathbb{R}^{n} \to \overline{\mathbb{R}}`\ 是凸函数，当且仅当\ :math:`epi f \subset \mathbb{R}^{n + 1}`\ 是凸集。

**定义1.11（闭函数）**\ ：如果函数\ :math:`f: X \to \overline{\mathbb{R}}`\ 的上境图是闭集，我们称\ :math:`f`\ 是闭函数。



现在，我们给出一些可微或二阶可微函数的凸性特征。

**命题1.12**\ ：设\ :math:`C`\ 是一个非空的凸开集。设\ :math:`f: \mathbb{R}^{n} \to \mathbb{R}`\ 在包含\ :math:`C`\ 的开集上可微，那么\ :math:`f`\ 是凸函数，当且仅当对于所有的\ :math:`x, z \in C`\ ，都有



.. math:: f(z) \geq f(x)+\langle \nabla f(x), z - x\rangle



**命题1.13**\ ：设\ :math:`C`\ 是\ :math:`\mathbb{R}^{n}`\ 中的非空凸集，且\ :math:`f: \mathbb{R}^{n} \to \mathbb{R}`\ 在包含\ :math:`C`\ 的开集上二阶可微。如果对于所有的\ :math:`x \in C`\ ，\ :math:`\nabla^{2} f(x)`\ 都是半正定的，那么\ :math:`f`\ 在\ :math:`C`\ 上是凸函数。

### 1.3 投影到凸集

给定一个集合\ :math:`C \subseteq \mathbb{R}^{n}`\ ，点\ :math:`x`\ 到\ :math:`C`\ 的距离定义为



.. math:: d(x ; C):=\inf \{\| x - y\| : y \in C\}



对于闭凸集，有一个重要的投影性质如下。

**命题1.14（投影性质）**\ ：设\ :math:`C`\ 是\ :math:`\mathbb{R}^{n}`\ 的非空闭凸子集。对于每个\ :math:`x \in \mathbb{R}^{n}`\ ，存在唯一的\ :math:`w \in C`\ ，使得



.. math:: \| x - w\| =d(x ; C)



:math:`w`\ 被称为\ :math:`x`\ 到\ :math:`C`\ 的投影，记为\ :math:`P_{C}(x)`\ 。

**命题1.15**\ ：设\ :math:`C`\ 是一个非空闭凸集，那么\ :math:`w = P_{C}(x)`\ 当且仅当对于所有的\ :math:`u \in C`\ ，都有



.. math:: \langle x - w, u - w\rangle \leq 0



## 2 凸集的法锥和切锥

**定义2.1（锥）**\ ：集合\ :math:`C`\ 是一个锥，如果对于任意的\ :math:`x \in C`\ 和\ :math:`0 < \lambda \in \mathbb{R}`\ ，都有\ :math:`\lambda x \in C`\ 。锥\ :math:`C`\ 的极锥（记为\ :math:`C^{\circ}`\ ）定义为



.. math:: C^{\circ}=\{\sigma:\langle\sigma, x\rangle \leq 0 \text{ 对于所有的 } x \in C\}



假设\ :math:`\Omega \subseteq \mathbb{R}^{n}`\ 是一个凸集。那么对于\ :math:`x \in \Omega`\ ，我们可以定义\ :math:`\Omega`\ 在\ :math:`x`\ 处的法锥为



.. math:: N_{\Omega}(x)=\{z \in \mathbb{R}^{n}:\langle z, y - x\rangle \leq 0 \text{ 对于所有的 } y \in \Omega\}



对于凸集，我们可以定义\ :math:`\Omega`\ 在\ :math:`x`\ 处的切锥\ :math:`T_{\Omega}(x)`\ 为\ :math:`N_{\Omega}(x)^{\circ}`\ 。



**定理2.2**\ ：对于问题\ :math:`\min_{\Omega} f(x)`\ ，如果\ :math:`f`\ 是光滑且凸的，\ :math:`\Omega`\ 是闭凸集，那么\ :math:`-\nabla f(x^{*}) \in N_{\Omega}(x^{*})`\ 意味着\ :math:`x^{*}`\ 是全局最优解。



3 次微分计算

------------



3.1 凸函数的次梯度

~~~~~~~~~~~~~~~~~~



在本小节中，我们引入凸函数次梯度这一关键概念。它作为非光滑函数的广义导数，在优化理论中有许多应用。



**定义3.1（次梯度）**\ ：设\ :math:`f: \mathbb{R}^{n} \to \overline{\mathbb{R}}`\ 是一个凸函数，且\ :math:`\bar{x} \in dom f`\ 。元素\ :math:`g \in \mathbb{R}^{n}`\ 被称为\ :math:`f`\ 在\ :math:`\bar{x}`\ 处的次梯度，如果……（文档此处定义不完整）

凸函数\ :math:`f`\ 的所有次梯度的集合称为次微分。



**定理3.2（\ :math:`f`\ 的次梯度是\ :math:`epi f`\ 的支撑超平面）**\ ：设\ :math:`f`\ 是一个凸函数，且\ :math:`x \in dom f`\ 。\ :math:`g \in \partial f(x)`\ 当且仅当\ :math:`\begin{pmatrix} g \\ -1 \end{pmatrix}`\ 定义了\ :math:`epi f`\ 在点\ :math:`\begin{pmatrix} x \\ f(x) \end{pmatrix}`\ 处的支撑超平面。



**命题3.3**\ ：设\ :math:`f`\ 是一个凸函数，且\ :math:`x \in int(dom f)`\ ，那么\ :math:`\partial f(x)`\ 是非空且紧致的。



**命题3.4**\ ：设\ :math:`f: \mathbb{R}^{n} \to \overline{\mathbb{R}}`\ 是凸函数，且在\ :math:`x \in int(dom f)`\ 处可微。那么\ :math:`\partial f(x)=\{\nabla f(x)\}`\ 。



**例3.5（\ :math:`f(x) = |x|`\ 的次梯度）**\ ：\ :math:`f(x) = |x|`\ 在\ :math:`\mathbb{R}`\ 上是凸函数。当\ :math:`x > 0`\ 时，\ :math:`f(x) = x`\ 在\ :math:`x`\ 处可微，且\ :math:`\nabla f(x) = 1`\ ，所以\ :math:`\partial f(x)=\{1\}`\ 。当\ :math:`x < 0`\ 时，\ :math:`f(x) = -x`\ 在\ :math:`x`\ 处可微，且\ :math:`\nabla f(x) = -1`\ ，所以\ :math:`\partial f(x)=\{-1\}`\ 。当\ :math:`x = 0`\ 时，我们需要找到\ :math:`g \in \mathbb{R}`\ ，使得对于所有的\ :math:`y \in \mathbb{R}`\ ，都有\ :math:`f(y) - f(0) \geq \langle g, y\rangle`\ 。即对于所有的\ :math:`y \in \mathbb{R}`\ ，\ :math:`|y| \geq gy \Rightarrow \frac{|y|}{y} \geq g \Rightarrow -1 \leq g \leq 1`\ ，所以\ :math:`\partial f(0)=[-1, 1]`\ 。



**定理3.6（丹斯金定理）**\ ：设\ :math:`f`\ 是凸函数，\ :math:`Z`\ 是一个紧致集，使得……（文档此处定理内容不完整）其中\ :math:`\phi: int(dom f) \times Z \to \mathbb{R} \cup \{-\infty, +\infty\}`\ 对于每个\ :math:`z \in Z`\ 都是一个扩展实值、闭、正常的凸函数。如果……（文档此处定理条件不完整）



3.2 方向导数

~~~~~~~~~~~~



**定义3.7（方向导数）**\ ：设\ :math:`f: \mathbb{R}^{n} \to \overline{\mathbb{R}}`\ 是一个函数，且\ :math:`x \in dom f`\ 。\ :math:`f`\ 在\ :math:`x`\ 处沿方向\ :math:`d`\ 的方向导数定义为……（文档此处定义不完整）

**定理3.8**\ ：对于凸函数\ :math:`f`\ 和\ :math:`x^{*} \in dom f`\ ，\ :math:`x^{*}`\ 是极小值点当且仅当对于所有的\ :math:`d`\ ，都有\ :math:`f'(x^{*} ; d) \geq 0`\ 。

**命题3.9**\ ：设\ :math:`f`\ 是凸函数且在\ :math:`x`\ 处可微，那么\ :math:`f'(x ; d)=\langle \nabla f(x), d\rangle`\ 。

**定理3.10（方向导数与次梯度的关系）**\ ：对于凸函数\ :math:`f`\ 和\ :math:`x \in int(dom f)`\ ，对于任意的\ :math:`d`\ ，都有



.. math:: f'(x ; d)=\sup _{g \in \partial f(x)}\langle g, d\rangle



### 3.3 次微分的计算

**定理3.11**\ ：对于一个凸集\ :math:`\Omega`\ ，我们可以定义\ :math:`\Omega`\ 的无穷指示函数为



.. math:: I_{\Omega}(x):=\begin{cases}0, & x \in \Omega \\+\infty, & x \notin \Omega\end{cases}



对于\ :math:`x`\ 在闭凸集\ :math:`\Omega`\ 中，\ :math:`N_{\Omega}(x)=\partial I_{\Omega}(x)`\ 。

## 4 最优性条件 我们关注求解如下问题：



.. math:: \min _{x \in \Omega} f(x)



其中\ :math:`f`\ 是凸函数，\ :math:`C`\ 是凸集。 **最优性条件**\ ： 1.

**无约束情况**\ ：如果\ :math:`\Omega=\mathbb{R}^{n}`\ 且\ :math:`dom f=\mathbb{R}^{n}`\ ，那么\ :math:`x^{*}`\ 是最优解当且仅当\ :math:`0 \in \partial f(x^{*})`\ 。

2.

**有约束且可微情况**\ ：现在假设\ :math:`\Omega \subset \mathbb{R}^{n}`\ 且\ :math:`f`\ 在\ :math:`\Omega`\ 中可微。可行点\ :math:`x^{*}`\ 是最优解当且仅当对于所有的\ :math:`y \in \Omega`\ ，都有\ :math:`\langle \nabla f(x^{*}), y - x^{*}\rangle \geq 0`\ ，这等价于\ :math:`-\nabla f(x^{*}) \in N_{\Omega}(x^{*})`\ 。

3.

**一般有约束情况**\ ：如果函数不可微，可行点\ :math:`x^{*}`\ 是最优解当且仅当\ :math:`0 \in \partial f(x^{*})+N_{\Omega}(x^{*})`\ 。

