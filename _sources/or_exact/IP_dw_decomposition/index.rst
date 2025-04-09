Dantzig-Wolfe分解在MIP中的应用
==============================



Reference

---------



-  https://ise.ncsu.edu/wp-content/uploads/sites/9/2018/08/decomposition-A-generic-view-of-Danzig-Wolfe-decomposition-in-mixed-iteger-programming.pdf

-  https://www.or.uni-bonn.de/~held/hausdorff_school_22/slides/VRPSolverBonn_IntroductionCG.pdf

-  https://imada.sdu.dk/u/jbj/DM209/Notes-DW-CG.pdf

-  https://www.cse.iitb.ac.in/~mitra/mtp/stage1/report/report.pdf

-  https://dabeenl.github.io/IE631_lecture22_note.pdf



2 Dantzig-Wolfe分解

-------------------



| 考虑如下混合整数规划：

| 



  .. math::





     \begin{align*}

     z_{IP} = \max & \quad c^\top x \\

     \text{s.t.} & \quad Ax \leq b \\

     & \quad Ex \leq f \tag{MIP} \\

     & \quad x \in \mathbb{Z}_+^d \times \mathbb{R}_+^p.

     \end{align*}

| 我们将学习用于求解该混合整数规划的Dantzig-Wolfe分解框架.



2.1 基于拉格朗日对偶的Dantzig-Wolfe分解

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



| 定义集合 $ Q $ 如下：

| 



  .. math::





     Q = \left\{ x \in \mathbb{Z}_+^d \times \mathbb{R}_+^p : Ax \leq b \right\}.

| 假设 $ Q $ 非空，且 $ A, b $ 的元素为有理数. 设 $ m $ 为矩阵 $ E $

  的行数，取 $

  :raw-latex:`\lambda `:raw-latex:`\in `:raw-latex:`\mathbb{R}`\ *+^m $.

  回顾，关于 $

  :raw-latex:`\lambda `\ :math:`，对（MIP）定义的拉格朗日松弛如下：`\ $

  :raw-latex:`\begin{align*}

  z_{\text{LR}}(\lambda) = \max & \quad c^\top x + \lambda^\top (f - Ex) \\

  \text{s.t.} & \quad Ax \leq b \tag{LR} \\

  & \quad x \in \mathbb{Z}_+^d \times \mathbb{R}_+^p.

  \end{align*}`



  .. math::



       

     此外，回顾混合整数规划（MIP）的拉格朗日对偶定义为：  



  z*\ {:raw-latex:`\text{LD}`} = :raw-latex:`\min `:raw-latex:`\left`{

  z\_{:raw-latex:`\text{LR}`}(:raw-latex:`\lambda`) :

  :raw-latex:`\lambda `:raw-latex:`\geq 0` :raw-latex:`\right`}.

  :raw-latex:`\tag{LD}`



  .. math::



       

     我们已知，（MIP）与（LD）通过如下（LD）的特征描述相关联：  



  z\_{:raw-latex:`\text{LD}`} = :raw-latex:`\max `:raw-latex:`\left`{

  c^:raw-latex:`\top `x : Ex :raw-latex:`\leq `f, x

  :raw-latex:`\in `:raw-latex:`\text{conv}`(Q) :raw-latex:`\right`}. $$



| 此外，根据Minkowski-Weyl定理，\ :math:`\text{conv}(Q)` 可表示为

| 



  .. math::





     \text{conv}(Q) = \text{conv}\{v^1, \ldots, v^n\} + \text{cone}\{r^1, \ldots, r^\ell\}

| 其中 :math:`v^1, \ldots, v^n` 是 :math:`\text{conv}(Q)`

  的\ **极点**\ ，\ :math:`r^1, \ldots, r^\ell` 是

  :math:`\text{conv}(Q)` 的\ **极射线**. 那么，\ :math:`\text{conv}(Q)`

  中的任意点 :math:`x` 可写为：

| 



  .. math::





     x = \sum_{k \in [n]} \alpha_k v^k + \sum_{h \in [\ell]} \beta_h r^h

| 其中存在 :math:`\alpha \in \mathbb{R}_+^k` 和

  :math:`\beta \in \mathbb{R}_+^\ell`\ ，满足：

| 



  .. math::





     \sum_{k \in [n]} \alpha_k = 1.



| 基于此，可得：

| 



  .. math::





     \begin{align*}

     z_{\text{LD}} = \max & \sum_{k \in [n]} (c^\top v^k) \alpha_k + \sum_{h \in [\ell]} (c^\top r^h) \beta_k \\

     \text{s.t.} & \sum_{k \in [n]} (E v^k) \alpha_k + \sum_{h \in [\ell]} (E r^h) \beta_k \leq f \tag{DW1} \\

     & \sum_{k \in [n]} \alpha_k = 1 \\

     & \alpha \in \mathbb{R}_+^k,\ \beta \in \mathbb{R}_+^\ell.

     \end{align*}

| 回顾，混合整数规划（MIP）的拉格朗日对偶（LD）是（MIP）的一种松弛.

  因此，我们将（DW1）称为（MIP）的\ **Dantzig-Wolfe松弛**.

  此外，我们有：

| 



  .. math::





     z_{IP} = \max\left\{c^\top x : Ex \leq f,\ x \in \text{conv}(Q),\ x_j \in \mathbb{Z}_+\ \forall j \in [d] \right\}.

| 因此，推导出：

| 



  .. math::





     \begin{align*}

     z_{IP} = \max & \sum_{k \in [n]} (c^\top v^k) \alpha_k + \sum_{h \in [\ell]} (c^\top r^h) \beta_k \\

     \text{s.t.} & \sum_{k \in [n]} (E v^k) \alpha_k + \sum_{h \in [\ell]} (E r^h) \beta_k \leq f \\

     & \sum_{k \in [n]} \alpha_k = 1 \tag{DW2} \\

     & \alpha \in \mathbb{R}_+^k,\ \beta \in \mathbb{R}_+^\ell \\

     & \sum_{k \in [n]} \alpha_k v_j^k + \sum_{h \in [\ell]} \beta_h r_j^h \in \mathbb{Z}_+,\ j \in [d].

     \end{align*}

| 此处，公式（DW2）被称为（MIP）的\ **Dantzig-Wolfe重构**.



2.2 (:math:`\text{DW1}`)的对偶是(:math:`\text{LD}`)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



| 回顾，(:math:`\text{LD}`)的Dantzig-Wolfe分解由下式给出：

| 



  .. math::





     \begin{align*}

     \max & \sum_{k \in [n]} (c^\top v^k) \alpha_k + \sum_{h \in [\ell]} (c^\top r^h) \beta_k \\

     \text{s.t.} & \sum_{k \in [n]} (E v^k) \alpha_k + \sum_{h \in [\ell]} (E r^h) \beta_k \leq f \tag{DW1}\\

     & \sum_{k \in [n]} \alpha_k = 1 \\

     & \alpha \in \mathbb{R}_+^k,\ \beta \in \mathbb{R}_+^\ell,

     \end{align*}

| 对(:math:`\text{DW1}`)取对偶，对不等式约束使用对偶变量

  :math:`\lambda`\ ，对等式约束使用对偶变量 :math:`\mu`\ ，推导可得：

| 



  .. math::





     \begin{align*}

     \min & \lambda^\top f + \mu \\

     \text{s.t.} & \mu + (E v^k)^\top \lambda \geq c^\top v^k,\quad k \in [n] \\

     & (E r^h)^\top \lambda \geq c^\top r^h,\quad h \in [\ell] \\

     & \lambda \geq 0.

     \end{align*}

| 注意，上述式子等价于：

| 



  .. math::





     \begin{align*}

     \min & \lambda^\top f + \mu \\

     \text{s.t.} & \mu \geq \max_{k \in [n]} \left\{(c - E^\top \lambda)^\top v^k \right\} \\

     & \lambda \in \text{dom}(z_{\text{LR}}),

     \end{align*}

| 因

| 



  .. math::





     \text{dom}(z_{\text{LR}}) = \left\{\lambda : (c - E^\top \lambda)^\top r^h \leq 0\ \forall h \in [\ell],\ \lambda \geq 0 \right\}.

| 消去变量 :math:`\mu`\ ，得到：

| 



  .. math::





     \begin{align*}

     \min & \lambda^\top f + \max_{k \in [n]} \left\{(c - E^\top \lambda)^\top v^k \right\} \\

     \text{s.t.} & \lambda \in \text{dom}(z_{\text{LR}}).

     \end{align*}

| 该式等价于：

| 



  .. math::





     \begin{align*}

     & \min_{\lambda \in \text{dom}(z_{\text{LR}})} \max_{k \in [n]} \left\{\lambda^\top f + (c - E^\top \lambda)^\top v^k \right\} \\

     = & \min_{\lambda \in \text{dom}(z_{\text{LR}})} \max_{k \in [n]} \underbrace{\left\{c^\top v^k + \lambda^\top (f - E v^k)\right\}}_{z_{\text{LR}}(\lambda)} \\

     = & \min\left\{z_{\text{LR}}(\lambda) : \lambda \in \text{dom}(z_{\text{LR}}) \right\} \\

     = & z_{\text{LD}}.

     \end{align*}



2.3 二元整数线性规划的Dantzig-Wolfe分解

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



| 考虑如下二元整数规划：

| 



  .. math::





     \begin{align*}

     z_{IP} = \max & \quad c^\top x \\

     \text{s.t.} & \quad Ax \leq b \\

     & \quad Ex \leq f \tag{BP} \\

     & \quad x \in \{0, 1\}^d.

     \end{align*}

| 我们将 $ Q $ 定义为：

| 



  .. math::





     Q = \left\{ x \in \{0, 1\}^d : Ax \leq b \right\}.

| 由于 $ Q $ 有界且有限，因此 $ Q = {v^1, :raw-latex:`\ldots`, v^n}

  :math:`.

  那么，` Q $ 中的任意点 $ x $ 可表示为：

| 



  .. math::





     x = \sum_{k \in [n]} \alpha_k v^k,\quad \sum_{k \in [n]} \alpha_k = 1,\quad \alpha_k \in \{0, 1\}^n.

| 由此可得：

| 



  .. math::





     \begin{align*}

     z_{IP} = \max & \quad \sum_{k \in [n]} (c^\top v^k) \alpha_k \\

     \text{s.t.} & \quad \sum_{k \in [n]} (E v^k) \alpha_k \leq f \\

     & \quad \sum_{k \in [n]} \alpha_k = 1 \\

     & \quad \alpha \in \{0, 1\}^n.

     \end{align*}

| 该公式为（BP）的\ **Dantzig-Wolfe重构**.

  （BP）的\ **Dantzig-Wolfe松弛**\ 为：

| 



  .. math::





     \begin{align*}

     \max & \quad \sum_{k \in [n]} (c^\top v^k) \alpha_k \\

     \text{s.t.} & \quad \sum_{k \in [n]} (E v^k) \alpha_k \leq f \\

     & \quad \sum_{k \in [n]} \alpha_k = 1 \\

     & \quad \alpha \geq 0.

     \end{align*}



2.4 具有块对角结构的问题

~~~~~~~~~~~~~~~~~~~~~~~~



| 我们考虑如下优化模型：

| 



  .. math::





     \begin{align*}

     &\max \quad c^{1^\top}x^1 + c^{2^\top}x^2 + \cdots + c^{p^\top}x^p \\

     \text{s.t.} &\quad A^1x^1& \leq b^1 \\

     &\quad\quad\quad A^2x^2 &\leq b^2 \\

     &\quad\quad\quad\quad\quad \ddots \\

     &\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad\quad A^px^p &\leq b^p \\

     &\quad E^1x^1 + E^2x^2 + \cdots + E^px^p &\leq f \\

     &\quad x^j \in \{0, 1\}^{n_j},\quad j \in [p].

     \end{align*}

| 对于 $ j :raw-latex:`\in [p] `$，定义 $ Q_j $ 如下：

| 



  .. math::  Q_j = \left\{ x^j \in \{0, 1\}^{n_j} : A^jx^j \leq b^j \right\}. 

| 这里，$ Q_j $ 有界且有限，因此 $ Q_j $ 中的任意点 $ x^j $ 可写为：

| 



  .. math::  x^j = \sum_{v \in Q_j} \alpha_v^j v,\quad \sum_{v \in Q_j} \alpha_v^j = 1,\quad \alpha^j_v \in \{0, 1\}^{|Q_j|}. 

| 因此，该问题的Dantzig-Wolfe重构表示为：

| 



  .. math::





     \begin{align*}

     \max &\quad \sum_{v \in Q_1} (c^{1^\top}v)\alpha_v^1 + \sum_{v \in Q_2} (c^{2^\top}v)\alpha_v^2 + \cdots + \sum_{v \in Q_p} (c^{p^\top}v)\alpha_v^p \\

     \text{s.t.} &\quad \sum_{v \in Q_1} (E^1v)\alpha_v^1 + \sum_{v \in Q_2} (E^2v)\alpha_v^2 + \cdots + \sum_{v \in Q_p} (E^pv)\alpha_v^p \leq f \\

     &\quad \sum_{v \in Q_j} \alpha_v^j = 1,\quad j \in [p] \\

     &\quad \alpha^j_v \in \{0, 1\}^{|Q_j|},\quad j \in [p].

     \end{align*}

| 那么，该问题的Dantzig-Wolfe松弛为：

| 



  .. math::





     \begin{align*}

     \max &\quad \sum_{v \in Q_1} (c^{1^\top}v)\alpha_v^1 + \sum_{v \in Q_2} (c^{2^\top}v)\alpha_v^2 + \cdots + \sum_{v \in Q_p} (c^{p^\top}v)\alpha_v^p \\

     \text{s.t.} &\quad \sum_{v \in Q_1} (E^1v)\alpha_v^1 + \sum_{v \in Q_2} (E^2v)\alpha_v^2 + \cdots + \sum_{v \in Q_p} (E^pv)\alpha_v^p \leq f \\

     &\quad \sum_{v \in Q_j} \alpha_v^j = 1,\quad j \in [p] \\

     &\quad \alpha^j \geq 0,\quad j \in [p].

     \end{align*}



3 使用列生成方法求解Dantzig-Wolfe重构

-------------------------------------



| Dantzig-Wolfe松弛（DW1）包含对应\ :math:`\text{conv}(Q)`\ 极点的变量\ :math:`\alpha_1, \ldots, \alpha_n`\ ，以及对应\ :math:`\text{conv}(Q)`\ 极射线的变量\ :math:`\beta_1, \ldots, \beta_\ell`.

  因此，\ :math:`n`\ 和\ :math:`\ell`\ 可能极大. 此时，可应用列生成技术.

  回顾（DW1）的对偶问题为：

| 



  .. math::





     \begin{align*}

     \min & \quad \lambda^\top f + \mu \\

     \text{s.t.} & \quad \mu + (E v^k)^\top \lambda \geq c^\top v^k,\quad k \in [n] \\

     & \quad (E r^h)^\top \lambda \geq c^\top r^h,\quad h \in [\ell] \\

     & \quad \lambda \geq 0.

     \end{align*}

| 列生成流程如下：从\ :math:`N \subseteq [n]`\ 和\ :math:`L \subseteq [\ell]`\ 出发，得到主问题：

| 



  .. math::





     \begin{align*}

     \max & \quad \sum_{k \in N} (c^\top v^k) \alpha_k + \sum_{h \in L} (c^\top r^h) \beta_k \\

     \text{s.t.} & \quad \sum_{k \in N} (E v^k) \alpha_k + \sum_{h \in L} (E r^h) \beta_k \leq f \\

     & \quad \sum_{k \in N} \alpha_k = 1 \\

     & \quad \alpha \in \mathbb{R}_+^k,\ \beta \in \mathbb{R}_+^\ell.

     \end{align*}

| 给定对应的对偶解\ :math:`(\lambda, \mu)`\ ，关联的子问题为：

| 



  .. math::





     \max\left\{ \max_{k \in [n]}\left\{(c - E^\top \lambda)^\top v^k - \mu \right\},\ \max_{h \in [\ell]}\left\{(c - E^\top \lambda)^\top r^h \right\} \right\}.

| 若子问题的值严格为正，则存在\ :math:`k \in [n] \setminus N`\ 或\ :math:`h \in [\ell] \setminus L`\ ，其在对偶问题中的约束被违反，此时可添加对应变量.

  事实上，子问题可等价求解：

| 



  .. math::





     \max\left\{ (c - E^\top \lambda)^\top x - \mu : x \in \text{conv}(Q) \right\} \\ 

     \Leftrightarrow \max\left\{ c^\top x + \lambda^\top (f - Ex) : x \in \text{conv}(Q) \right\}.



若该优化问题无界，则对某些\ :math:`h \in [\ell] \setminus L`\ ，必存在极射线\ :math:`r^h`\ ，满足\ :math:`(E r^h)^\top \lambda < c^\top r^h`\ ；若有严格为正的有限最优解，则对某些\ :math:`k \in [n] \setminus N`\ ，存在极点\ :math:`v^k`\ ，使得\ :math:`\mu + (E v^k)^\top \lambda < c^\top v^k`.

