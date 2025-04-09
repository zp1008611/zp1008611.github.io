对偶理论
========

1 预备知识
----------

$ n :raw-latex:`\times `n $ 对称矩阵的集合记为 $
:raw-latex:`\mathbb{S}`^n :math:`，` n :raw-latex:`\times `n $
对称半正定（正定）矩阵的集合记为 $ :raw-latex:`\mathbb{S}`^n\_+
(:raw-latex:`\mathbb{S}`\ :sup:`{n}\ {++}) $. 符号 $ X
:raw-latex:`\succeq 0`  (X :raw-latex:`\succ 0`) $ 表示矩阵 $ X
:raw-latex:`\in `:raw-latex:`\mathbb{S}`^n $ 是半正定（正定）的. 符号 $
X :raw-latex:`\geq 0`  (X > 0) $ 表示矩阵 $ X $
的每个元素都是非负的（正的）. $ X $ 的迹，即 $ X $ 对角元素之和，记为 $
:raw-latex:`\mathrm{Tr}`(X) $. 两个矩阵 $ A
:raw-latex:`\in `:raw-latex:`\mathbb{R}`^{m :raw-latex:`\times `n} $ 和
$ B :raw-latex:`\in `:raw-latex:`\mathbb{R}`^{m :raw-latex:`\times `n} $
的内积定义为 $ :raw-latex:`\langle `A, B :raw-latex:`\rangle `:=
:raw-latex:`\sum`\ {j=1}`\ m :raw-latex:`\sum`\ *{k=1}^n A*\ {jk}B\_{jk}
= :raw-latex:`\mathrm{Tr}`(A^:raw-latex:`\top `B) $. 矩阵 $ A
:raw-latex:`\in `:raw-latex:`\mathbb{R}`^{m :raw-latex:`\times `n} $
的弗罗贝尼乌斯范数定义为 $ \|A|_F :=
:raw-latex:`\sqrt{\sum_{i=1}^m \sum_{j=1}^n A_{ij}^2}` $.

2 弱对偶性
----------

2.1 拉格朗日对偶问题
~~~~~~~~~~~~~~~~~~~~

| 在本节中，我们考虑一个可能非凸的优化问题：
| 

  .. math::


     p^* := \min_{x} f_0(x) \ \text{s.t.} \ f_i(x) \leq 0, \ i = 1, \dots, m \tag{2.1}

  我们用 $ :raw-latex:`\mathcal{D}` $
  表示问题的定义域（即所有涉及函数定义域的交集），用 $
  :raw-latex:`\mathcal{X}`
  :raw-latex:`\subseteq `:raw-latex:`\mathcal{D}` $ 表示其可行集.

我们将上述问题称为原问题，原问题中的决策变量为 $ x $.
引入拉格朗日对偶性的一个目的是为极小化问题寻找下界（或为极大化问题寻找上界）.
之后，我们将使用对偶性工具推导凸问题的最优性条件.

2.2 对偶问题
~~~~~~~~~~~~

**拉格朗日函数**\ ：我们为该问题关联一个拉格朗日函数 $
:raw-latex:`\mathcal{L}`: :raw-latex:`\mathbb{R}`^n
:raw-latex:`\times `:raw-latex:`\mathbb{R}`^m
:raw-latex:`\to `:raw-latex:`\mathbb{R}` :math:`，其定义为：`\ $
:raw-latex:`\mathcal{L}`(x, :raw-latex:`\lambda`) := f_0(x) +
:raw-latex:`\sum`\_{i=1}^m :raw-latex:`\lambda`\_i f_i(x)
:raw-latex:`\tag{2.2}` $$ 变量 $
:raw-latex:`\lambda `:raw-latex:`\in `:raw-latex:`\mathbb{R}`^m $
称为拉格朗日乘子.

我们注意到，对于每个可行的 $ x :raw-latex:`\in `:raw-latex:`\mathcal{X}`
$，以及每个 $ :raw-latex:`\lambda `:raw-latex:`\geq 0` :math:`，` f_0(x)
$ 有下界 $ :raw-latex:`\mathcal{L}`(x, :raw-latex:`\lambda`)
:math:`：`\ $ :raw-latex:`\forall `x
:raw-latex:`\in `:raw-latex:`\mathcal{X}`,
:raw-latex:`\forall `:raw-latex:`\lambda `:raw-latex:`\in `:raw-latex:`\mathbb{R}`\ *+^m
: f_0(x) :raw-latex:`\geq `:raw-latex:`\mathcal{L}`(x,
:raw-latex:`\lambda`).

.. math::

     
   拉格朗日函数可用于将原问题（??）表示为无约束问题. 确切地说：  

p^\* = :raw-latex:`\min`\ x
:raw-latex:`\max`\ {:raw-latex:`\lambda `:raw-latex:`\geq 0`}
:raw-latex:`\mathcal{L}`(x, :raw-latex:`\lambda`),

.. math::

     
   这里我们利用了以下事实：对于任意向量 $ f \in \mathbb{R}^m $，有  

:raw-latex:`\max`*\ {:raw-latex:`\lambda `:raw-latex:`\geq 0`}
:raw-latex:`\lambda`^:raw-latex:`\top `f =

.. raw:: latex

   \begin{cases} 
   0 & \text{若 } f \leq 0 \\
   +\infty & \text{否则}
   \end{cases}

| 

  .. math::

      
     **拉格朗日对偶函数**. 然后我们定义拉格朗日对偶函数（简称对偶函数）为函数  

  g(:raw-latex:`\lambda`) := :raw-latex:`\min`\ *x
  :raw-latex:`\mathcal{L}`(x, :raw-latex:`\lambda`).

  .. math::

       
     根据上述边界（??），通过对右边的 $ x $ 求极小，我们得到  

  :raw-latex:`\forall `x :raw-latex:`\in `:raw-latex:`\mathcal{X}`,
  :raw-latex:`\forall `:raw-latex:`\lambda `:raw-latex:`\geq 0` : f_0(x)
  :raw-latex:`\geq `:raw-latex:`\min`*\ {x’}
  :raw-latex:`\mathcal{L}`(x’, :raw-latex:`\lambda`) =
  g(:raw-latex:`\lambda`),

  .. math::

      
     对左边的 $ x $ 求极小后，得到下界  

  :raw-latex:`\forall `:raw-latex:`\lambda `:raw-latex:`\in `:raw-latex:`\mathbb{R}`\ *+^m
  : p^\* :raw-latex:`\geq `g(:raw-latex:`\lambda`).

  .. math::

      
     **拉格朗日对偶问题**. 利用上述边界，我们能得到的最佳下界是 $ p^* \geq d^* $，其中  

  d^\* = :raw-latex:`\max`*\ {:raw-latex:`\lambda `:raw-latex:`\geq 0`}
  g(:raw-latex:`\lambda`). $$
| 我们将上述问题称为对偶问题，向量 $
  :raw-latex:`\lambda `:raw-latex:`\in `:raw-latex:`\mathbb{R}`^m $
  称为对偶变量.

**定理 2.1（极小极大不等式）**\ ：对任意关于向量变量 $ x, y $ 的函数 $
:raw-latex:`\phi `$，以及任意子集 $ :raw-latex:`\mathcal{X}`,
:raw-latex:`\mathcal{Y}` :math:`，有`\ $ :raw-latex:`\max`\ *{y
:raw-latex:`\in `:raw-latex:`\mathcal{Y}`} :raw-latex:`\min`*\ {x
:raw-latex:`\in `:raw-latex:`\mathcal{X}`} :raw-latex:`\phi`(x, y)
:raw-latex:`\leq `:raw-latex:`\min`\ *{x
:raw-latex:`\in `:raw-latex:`\mathcal{X}`} :raw-latex:`\max`*\ {y
:raw-latex:`\in `:raw-latex:`\mathcal{Y}`} :raw-latex:`\phi`(x, y). $$

**定理 2.2.** 对于一般的（可能非凸的）问题（??），弱对偶性成立：$
p\ :sup:`\* :raw-latex:`\geq `d`\ \* $.

| **含等式约束的情形**.
  如果问题中存在等式约束，我们可以将其表示为两个不等式约束.
  结果表明，这会得到相同的对偶问题，就好像我们直接为每个等式约束使用一个对偶变量，且该对偶变量符号不受限制.
  为了说明这一点，考虑问题
| 

  .. math::


     \begin{aligned}
     p^* := \min_x & \ f_0(x) \\
     \text{s.t.} & \ f_i(x) \leq 0, \, i = 1, \dots, m, \\
     & \ h_i(x) = 0, \, i = 1, \dots, p.
     \end{aligned}

我们将该问题写为

.. math::


   \begin{aligned}
   p^* := \min_{x} & \ f_0(x) \\
   \text{s.t.} & \ f_i(x) \leq 0, \, i = 1, \dots, m, \\
   & \ h_i(x) \leq 0, \ -h_i(x) \leq 0, \, i = 1, \dots, p.
   \end{aligned}

对约束 $ :raw-latex:`\pm `h_i(x) :raw-latex:`\leq 0` $ 使用乘子 $
:raw-latex:`\nu`\_i^:raw-latex:`\pm `\ :math:`，我们将相关的拉格朗日函数写为`\ $

.. raw:: latex

   \begin{aligned}
   \mathcal{L}(x, \lambda, \nu^+, \nu^-) 
   &= f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{i=1}^p h_i(x) + \sum_{i=1}^p \nu_i^- (-h_i(x)) \\
   &= f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{i=1}^p \nu_i h_i(x),
   \end{aligned}

| $$
| 其中 $ :raw-latex:`\nu `:= :raw-latex:`\nu`^+ - :raw-latex:`\nu`^- $
  没有任何符号约束.因此，原问题中的不等式约束对应于相应乘子的符号约束，而等式约束的乘子没有显式约束.

3 强对偶性
----------

3.1 原问题与对偶问题
~~~~~~~~~~~~~~~~~~~~

| 在本节中，我们考虑一个凸优化问题
| 

  .. math::


     \begin{aligned}
     p^* := \min_{x} & \ f_0(x) \\
     \text{s.t.} & \ f_i(x) \leq 0, \, i = 1, \dots, m, \\
     & \ h_i(x) = 0, \, i = 1, \dots, p,
     \end{aligned}\tag{3.1}
| 其中函数 $ f_0, f_1, :raw-latex:`\dots`, f_m $ 是凸的，且 $ h_1,
  :raw-latex:`\dots`, h_p $ 是仿射的.我们用 $ :raw-latex:`\mathcal{D}` $
  表示问题的定义域（即所有涉及函数定义域的交集），用 $
  :raw-latex:`\mathcal{X}`
  :raw-latex:`\subseteq `:raw-latex:`\mathcal{D}` $ 表示其可行集.

我们为该问题关联一个拉格朗日函数 $ :raw-latex:`\mathcal{L}`:
:raw-latex:`\mathbb{R}`^n :raw-latex:`\times `:raw-latex:`\mathbb{R}`^m
:raw-latex:`\times `:raw-latex:`\mathbb{R}`^p
:raw-latex:`\to `:raw-latex:`\mathbb{R}` :math:`，其定义为：`\ $
:raw-latex:`\mathcal{L}`(x, :raw-latex:`\lambda`, :raw-latex:`\nu`) :=
f_0(x) + :raw-latex:`\sum`\ *{i=1}^m :raw-latex:`\lambda`\ i f_i(x) +
:raw-latex:`\sum`\ {i=1}^p :raw-latex:`\nu`\ i h_i(x).

.. math::

     
   对偶函数是 $ g: \mathbb{R}^m \times \mathbb{R}^p \to \mathbb{R} $，定义为：  

g(:raw-latex:`\lambda`, :raw-latex:`\nu`) := :raw-latex:`\min`\ {x}
:raw-latex:`\mathcal{L}`(x, :raw-latex:`\lambda`, :raw-latex:`\nu`).

.. math::

     
   相关的对偶问题是  

d^\* = :raw-latex:`\max`*\ {:raw-latex:`\lambda `:raw-latex:`\geq 0`,
:raw-latex:`\nu`} g(:raw-latex:`\lambda`, :raw-latex:`\nu`). $$

3.2 通过斯莱特条件的强对偶性
----------------------------

| **对偶间隙与强对偶性**\ ：我们已了解弱对偶性如何构建一个凸优化问题，即便原（主）问题非凸，该问题也能为原问题提供下界.对偶间隙是一个非负数
  $ p^\* - d^\* $.
| 若对偶间隙为零（即 $ p^\* = d^\* $），则称问题（??）满足强对偶性.

| **斯莱特条件**\ ：若问题严格可行，即
| 

  .. math::


     \exists x_0 \in \mathcal{D} : f_i(x_0) < 0,\, i = 1, \dots, m,\ h_i(x_0) = 0,\, i = 1, \dots, p,
| 则称其满足斯莱特条件.当 $ f_i $
  为仿射函数时，无需严格可行性，可用斯莱特条件的弱形式替代.由此可得：

**定理
3.1（通过斯莱特条件的强对偶性）**\ ：若原问题（??）为凸问题，且满足弱斯莱特条件，则强对偶性成立，即
$ p^\* = d^\* $.
