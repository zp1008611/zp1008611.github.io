线性规划介绍
============



-  https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15859-f11/www/notes/lecture05.pdf

-  https://people.math.carleton.ca/~kcheung/math/notes/MATH5801/02/2_2_farkas_lemma.html



线性规划概述

------------



线性规划（Linear Programming,

LP）是一种数学优化方法，用于在给定的线性约束条件下，寻找线性目标函数的最优解（最大值或最小值）.

它广泛应用于资源分配、生产调度、物流规划等领域，是运筹学和管理科学的重要基础工具.



**核心组成部分**

~~~~~~~~~~~~~~~~



1. | **决策变量**

   | 表示需要优化的未知量，通常用 $ x_1, x_2, :raw-latex:`\dots`, x_n $

     表示. 例如，生产计划中的产品数量.



2. | **目标函数**

   | 待优化的线性函数，形式为：

   | 



     .. math::





        \max/\min \quad c_1x_1 + c_2x_2 + \dots + c_nx_n

         



     例如，最大化利润或最小化成本.



3. | **约束条件**

   | 由线性不等式或等式构成，限制决策变量的可行范围，例如：

   | 



     .. math::





        \begin{cases}

        a_{11}x_1 + a_{12}x_2 + \dots + a_{1n}x_n \leq (\text{或} \geq, =) \, b_1 \\

        \vdots \\

        a_{m1}x_1 + a_{m2}x_2 + \dots + a_{mn}x_n \leq (\text{或} \geq, =) \, b_m \\

        x_1, x_2, \dots, x_n \geq 0 \quad \text{（非负约束）}

        \end{cases}



**标准形式**

~~~~~~~~~~~~



| 线性规划的标准形式为：

| 



  .. math::





     \begin{align*}

     \max \quad & \mathbf{c}^T \mathbf{x} \\

     \text{s.t.} \quad & \mathbf{A} \mathbf{x} \leq \mathbf{b} \\

     & \mathbf{x} \geq \mathbf{0}

     \end{align*}

| 其中，\ :math:`\mathbf{c}` 是目标函数系数向量，\ :math:`\mathbf{A}`

  是约束矩阵，\ :math:`\mathbf{b}` 是约束右端项向量.



**求解方法**

~~~~~~~~~~~~



1. | **单纯形法**

   | 由George

     Dantzig在1947年提出，通过迭代从一个顶点（基本可行解）移动到相邻顶点，逐步逼近最优解.



2. | **对偶理论**

   | 每个线性规划问题都有一个对应的对偶问题，两者的最优解存在密切关系，可用于验证解的正确性或求解复杂问题.



3. | **内点法**

   | 适用于大规模问题，通过在可行域内部移动路径寻找最优解.



LP Duality

----------



下面从不同角度为你详细介绍线性规划对偶问题的推导过程.



从拉格朗日对偶性推导

~~~~~~~~~~~~~~~~~~~~



对于标准形式的线性规划原问题：



.. math::





   \begin{align*}

   \max\quad & z = c^T x \\

   \text{s.t.}\quad & Ax \leq b \\

   & x \geq 0

   \end{align*}



1. **引入拉格朗日函数** 引入非负的拉格朗日乘子向量

:math:`y=(y_1,y_2,\cdots,y_m)^T\geq0` 和

:math:`s=(s_1,s_2,\cdots,s_n)^T\geq0`\ ，构造拉格朗日函数：



.. math:: L(x,y,s)=c^T x + y^T(b - Ax)-s^T x



这里 :math:`y` 对应不等式约束 :math:`Ax\leq b`\ ，\ :math:`s`

对应非负约束 :math:`x\geq0`.



2. **推导对偶问题** 对偶问题为



   .. math:: \min_{y\geq0,s\geq0}\max_{x}L(x,y,s)



   对 :math:`L(x,y,s)` 关于 :math:`x` 求极大，令

   :math:`\frac{\partial L}{\partial x}=c - A^T y - s = 0`\ ，即

   :math:`s = c - A^T y`.



   将 :math:`s = c - A^T y` 代入 :math:`L(x,y,s)` 中，此时

   :math:`L(x,y,s)` 关于 :math:`x` 求极大后的值为 :math:`y^T b`.

   同时，由于 :math:`s\geq0`\ ，所以

   :math:`c - A^T y\geq0`\ ，这样就得到对偶问题：



   .. math::





      \begin{align*}

      \min\quad & w = b^T y \\

      \text{s.t.}\quad & A^T y \geq c \\

      & y \geq 0

      \end{align*}



**定理（线性规划对偶定理）** 如果 :math:`P` 和 :math:`D`

是一对线性规划的原 - 对偶问题，那么会出现以下四种情况之一： 1.

两者都不可行. 2. :math:`P` 无界且 :math:`D` 不可行. 3. :math:`D` 无界且

:math:`P` 不可行. 4. 两者都可行，并且存在 :math:`P` 和 :math:`D`

的最优解 :math:`x`\ ，\ :math:`y`\ ，使得 :math:`c^{\top}x = b^{\top}y`.



我们已经看到，情况2和情况3是弱对偶定理的简单推论.

第一种情况很容易出现：一个简单的例子是，取 :math:`A`

为零矩阵，\ :math:`b` 严格为负，\ :math:`c` 严格为正.

因此，唯一仍然值得关注的情况是情况4.



几何证明. 设 :math:`P` 为规划问题

:math:`\max(c^{\top}x\mid Ax\leq b, x\in\mathbb{R}^n)`\ ，\ :math:`D`

为对偶规划问题 :math:`\min(b^{\top}y\mid A^{\top}y = c, y\geq0)`.



假设 :math:`x^*` 是 :math:`P` 的一个最优可行解. 设对于

:math:`i\in I`\ ，\ :math:`a_{i}^{\top}x\leq b_{i}` 是在 :math:`x^*`

处所有起作用的约束条件 . 我们断言，目标函数向量 :math:`c` 包含在由向量

:math:`\{a_{i}\}_{i\in I}` 生成的锥

:math:`K = \{x\mid x=\sum_{i\in I}\lambda_{i}a_{i},\lambda_{i}\geq0\}`

中.



为了推出矛盾，假设 :math:`c` 不在这个锥中. 那么在 :math:`c` 和 :math:`K`

之间一定存在一个分离超平面： 即，存在一个向量

:math:`d\in\mathbb{R}^n`\ ，使得对于所有的 :math:`i\in I`\ ，有

:math:`a_{i}^{\top}d\leq0`\ ，但 :math:`c^{\top}d > 0`. 现在考虑点

:math:`z = x^{*}+\epsilon d`\ ，其中 :math:`\epsilon>0` 是一个很小的数.

注意以下几点： - 对于足够小的 :math:`\epsilon`\ ，点 :math:`z` 满足约束

:math:`Az\leq b`. 考虑 :math:`j\notin I` 时的

:math:`a_{j}^{\top}z\leq b`\ ： 由于这个约束在 :math:`x^{*}`

处不是起作用约束，所以如果 :math:`\epsilon` 足够小，就不会违反该约束.

对于 :math:`j\in I` 时的 :math:`a_{j}^{\top}z\leq b`\ ，我们有

:math:`a_{j}^{\top}z = a_{j}^{\top}x^{*}+\epsilon a_{j}^{\top}d = b+\epsilon a_{j}^{\top}d\leq b`\ ，因为

:math:`\epsilon>0` 且 :math:`a_{j}^{\top}d\leq0`. -

目标函数值会增加，因为

:math:`c^{\top}z = c^{\top}x^{*}+\epsilon c^{\top}d>c^{\top}x^{*}`.



这与 :math:`x^{*}` 是最优解这一事实相矛盾.



因此，向量 :math:`c` 位于由约束条件的法向量所构成的锥内，所以 :math:`c`

是这些法向量的正线性组合. 对于 :math:`i\in I`\ ，选择

:math:`\lambda_{i}` 使得

:math:`c = \sum_{i\in I}\lambda_{i}a_{i}`\ ，\ :math:`\lambda\geq0`\ ，并且对于

:math:`j\notin I`\ ，令 :math:`\lambda_{j}=0`. - 我们知道

:math:`\lambda\geq0`. -

:math:`A^{\top}\lambda=\sum_{i\in[m]}\lambda_{i}a_{i}=\sum_{i\in I}\lambda_{i}a_{i}=c`.

-

:math:`b^{\top}\lambda=\sum_{i\in I}b_{i}\lambda_{i}=\sum_{i\in I}(a_{i}x^{*})\lambda_{i}=\sum_{i\in I}\lambda_{i}a_{i}x^{*}=c^{\top}x^{*}`.



因此，\ :math:`\lambda` 是对偶问题的一个解，且

:math:`c^{\top}x^{*}=b^{\top}\lambda`\ ，所以根据弱对偶定理，\ :math:`OPT(P)=OPT(D)`.

:math:`\square`

