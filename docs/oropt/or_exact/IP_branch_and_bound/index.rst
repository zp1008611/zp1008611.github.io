分支定界
========



Reference

---------



-  https://web.stanford.edu/class/ee392o/bb.pdf

-  https://www.math.cuhk.edu.hk/course_builder/1415/math3220/L3-update.pdf

-  https://arxiv.org/pdf/2111.06257



在\ `凸包和有效不等式 <..\IP_convex_hull_and_valid_ineq\README.md>`__

的内容里，我们已经介绍了分支定界算法的思想，下面给出完整的算法框架形式.



1 算法概述

----------



| 考虑混合整数线性规划

| 



  .. math::





     z^* = \max \{ f(x) : x \in \mathcal{D} \} 

| 其中

| 



  .. math::





     f(x) = c^Tx, c\in\mathbb{R}^n\\

     \mathcal{D} = \{ x \in \mathbb{R}^n_+\mid A x \leq b,\, ,\, x_j \in \mathbb{Z}_+,\, \forall j \in I \}.



| **算法1 分支定界法**

| 1 令 $ :raw-latex:`\mathcal{L}` = :raw-latex:`\mathcal{D}` $，初始化 $

  :raw-latex:`\hat{x}` $

| 2 **while** $ :raw-latex:`\mathcal{L}`

  :raw-latex:`\neq `:raw-latex:`\emptyset `$ **do**

| 3 :math:`\quad` 从 $ :raw-latex:`\mathcal{L}` $ 中选择待探索的子集合 $

  :raw-latex:`\mathcal{S}`$ :math:`\\` 4 :math:`\quad`

  求\ :math:`(\mathcal{S},f)`\ 的线性松弛问题的解\ :math:`\hat{x}'`

  :math:`\\` 5 :math:`\quad` **if** $ :raw-latex:`\hat{x}`’ $是不可行解

  **or** $ :raw-latex:`\hat{x}`’

  :math:`是分数可行解，且`\ f（:raw-latex:`\hat{x}`‘）:raw-latex:`\leq `f(:raw-latex:`\hat{x}`)$

  **then** :math:`\\` 6 :math:`\quad\quad`

  :math:`\mathcal{S}`\ 赋予可以剪枝属性 :math:`\\` 7 :math:`\quad`

  **else if** $ :raw-latex:`\hat{x}`’ :math:`是分数可行解，且`\ f

  （:raw-latex:`\hat{x}`‘）> f(:raw-latex:`\hat{x}`)$ **then**

  :math:`\\` 8 :math:`\quad\quad` :math:`\mathcal{S}`\ 赋予不可剪枝属性

  :math:`\\` 9 :math:`\quad` **else if** $ :raw-latex:`\hat{x}`’

  $是整数可行解 **then** :math:`\\` 10 :math:`\quad\ \ \ ` $

  :raw-latex:`\hat{x}` = :raw-latex:`\hat{x}`’ $ :math:`\\` 11

  :math:`\quad\ \ \ ` :math:`\mathcal{S}`\ 赋予可以剪枝属性 :math:`\\`

  12 :math:`\ \ \ ` **end if** :math:`\\` 13 :math:`\ \ \ ` **if**

  :math:`\mathcal{S}`\ 不可剪枝 **then** :math:`\\` 14

  :math:`\quad\ \ \ ` 将 $ :raw-latex:`\mathcal{S}` $ 划分为 $

  :raw-latex:`\mathcal{S}`\_1, :raw-latex:`\mathcal{S}`\_2,

  :raw-latex:`\dots`, :raw-latex:`\mathcal{S}`\_r $

| 15 :math:`\quad\ \ \ ` 将 $ :raw-latex:`\mathcal{S}`\_1,

  :raw-latex:`\mathcal{S}`\_2, :raw-latex:`\dots`,

  :raw-latex:`\mathcal{S}`\_r $ 加入 $ :raw-latex:`\mathcal{L}` $

  :math:`\\` 16 :math:`\ \ \ ` **end if** :math:`\\` 17 :math:`\ \ \ `

  从 $ :raw-latex:`\mathcal{L}` $ 中移除 $ :raw-latex:`\mathcal{S}` $

| 18 **end while**

| 19 **return** $ :raw-latex:`\hat{x}` $



上述伪代码中，节点选择策略影响第 3

行节点的探索顺序；变量选择策略（分支规则）影响算法第 14

行子问题的划分方式；第 4-11 行的剪枝属性赋予策略决定 $

:raw-latex:`\mathcal{S}` $ 是被剪枝还是继续被划分.



.. raw:: html



   <!-- 分支定界算法是用于非凸问题全局优化的方法[LW66, Moo91]. 从它们能对（全局）最优目标值保持可证明的上界与下界这一角度看，这些算法属于非启发式算法；算法终止时，会给出找到的次优点为ε-次优的证明. 不过，分支定界算法可能（且常常）运行缓慢. 在最坏情况下，其计算量会随问题规模呈指数增长，但某些幸运场景下，算法能以少得多的计算量收敛. 在这些简短笔记中，我们将描述分支定界方法的两个典型简单示例. 



   ## 1 分支定界算法思想 

   本节内容取自[BBB91]. 此处描述的分支定界算法，用于在m维矩形区域$\mathcal{Q}_{\text{init}}$上，寻找函数$f: \mathbf{R}^m \to \mathbf{R}$的全局最小值. （当然，将$f$替换为$-f$，该算法也可用于求全局最大值. ）  



   对于矩形区域$\mathcal{Q} \subseteq \mathcal{Q}_{\text{init}}$，定义：  

   $$

   \Phi_{\min}(\mathcal{Q}) = \min_{q \in \mathcal{Q}} f(q).

   $$  

   随后，算法利用在$\{ \mathcal{Q} \mid \mathcal{Q} \subseteq \mathcal{Q}_{\text{init}} \}$上定义的两个函数$\Phi_{\text{lb}}(\mathcal{Q})$和$\Phi_{\text{ub}}(\mathcal{Q})$（一般而言，它们比$\Phi_{\min}(\mathcal{Q})$更容易计算），以绝对精度$\epsilon > 0$计算$\Phi_{\min}(\mathcal{Q}_{\text{init}})$. 这两个函数满足以下条件：  



   - **（R1）** $\Phi_{\text{lb}}(\mathcal{Q}) \leq \Phi_{\min}(\mathcal{Q}) \leq \Phi_{\text{ub}}(\mathcal{Q})$. 即$\Phi_{\text{lb}}$和$\Phi_{\text{ub}}$分别计算$\Phi_{\min}(\mathcal{Q})$的下界与上界.   

   - **（R2）** 当$\mathcal{Q}$各边的最大半长（记为$\text{size}(\mathcal{Q})$）趋于零时，上下界之差一致收敛于零，即：  

   $$

   \forall \epsilon > 0 \; \exists \delta > 0 \text{ 使得 } \forall \mathcal{Q} \subseteq \mathcal{Q}_{\text{init}}, \; \text{size}(\mathcal{Q}) \leq \delta \implies \Phi_{\text{ub}}(\mathcal{Q}) - \Phi_{\text{lb}}(\mathcal{Q}) \leq \epsilon.

   $$  

   粗略地说，随着矩形区域收缩至一点，界$\Phi_{\text{lb}}$和$\Phi_{\text{ub}}$会愈发精确. 





   ## 2 分支定界算法思想 

   首先计算$\Phi_{\text{lb}}(\mathcal{Q}_{\text{init}})$和$\Phi_{\text{ub}}(\mathcal{Q}_{\text{init}})$. 若$\Phi_{\text{ub}}(\mathcal{Q}_{\text{init}}) - \Phi_{\text{lb}}(\mathcal{Q}_{\text{init}}) \leq \epsilon$，算法终止. 否则，将$\mathcal{Q}_{\text{init}}$划分为子矩形的并集$\mathcal{Q}_{\text{init}} = \mathcal{Q}_1 \cup \mathcal{Q}_2 \cup \cdots \cup \mathcal{Q}_N$，并计算$i = 1, 2, \dots, N$时的$\Phi_{\text{lb}}(\mathcal{Q}_i)$和$\Phi_{\text{ub}}(\mathcal{Q}_i)$. 此时有：  

   $$

   \min_{1 \leq i \leq N} \Phi_{\text{lb}}(\mathcal{Q}_i) \leq \Phi_{\min}(\mathcal{Q}_{\text{init}}) \leq \min_{1 \leq i \leq N} \Phi_{\text{ub}}(\mathcal{Q}_i),

   $$  

   得到$\Phi_{\min}(\mathcal{Q}_{\text{init}})$的新边界. 若新边界差≤$\epsilon$，算法终止；否则，细化$\mathcal{Q}_{\text{init}}$划分并更新边界.   



   若划分$\mathcal{Q}_{\text{init}} = \cup_{i=1}^N \mathcal{Q}_i$满足$\text{size}(\mathcal{Q}_i) \leq \delta$（$i = 1, \dots, N$），根据条件（R2）：  

   $$

   \min_{1 \leq i \leq N} \Phi_{\text{ub}}(\mathcal{Q}_i) - \min_{1 \leq i \leq N} \Phi_{\text{lb}}(\mathcal{Q}_i) \leq \epsilon,

   $$  

   “$\delta$-网格”确保$\Phi_{\min}(\mathcal{Q}_{\text{init}})$的绝对精度$\epsilon$. 但“$\delta$-网格”的矩形数量及计算量随$1/\delta$指数增长. 分支定界算法采用启发式规则：给定待细化划分$\mathcal{Q}_{\text{init}} = \cup_{i=1}^N \mathcal{Q}_i$，选取$\mathcal{Q} \in \mathcal{L}$使$\Phi_{\text{lb}}(\mathcal{Q}) = \min_{1 \leq i \leq N} \Phi_{\text{lb}}(\mathcal{Q}_i)$，并将其分成两部分. 需强调这是启发式方法，最坏情况仍为$\delta$-网格.   



   以下描述中，$k$为迭代索引，$\mathcal{L}_k$为第$k$次迭代的矩形列表，$L_k$、$U_k$为$\Phi_{\min}(\mathcal{Q}_{\text{init}})$的下、上界.   



   ## 3 分支定界算法伪代码

   $

   k = 0; \\

   \mathcal{L}_0 = \{ \mathcal{Q}_{\text{init}} \}; \\

   L_0 = \Phi_{\text{lb}}(\mathcal{Q}_{\text{init}}); \\

   U_0 = \Phi_{\text{ub}}(\mathcal{Q}_{\text{init}}); \\

   \text{while } U_k - L_k > \epsilon \; \{ \\

    \quad \text{选取 } \mathcal{Q} \in \mathcal{L}_k \text{ 使 } \Phi_{\text{lb}}(\mathcal{Q}) = L_k; \\

    \quad 沿最长边将\mathcal{Q}分割为\mathcal{Q}_I \text{ 和 } \mathcal{Q}_{II}; \\

    \quad 从\mathcal{L}_k中移除\mathcal{Q}，加入\mathcal{Q}_I \text{ 和 } \mathcal{Q}_{II}，形成\mathcal{L}_{k+1}; \\

    \quad L_{k+1} := \min_{\mathcal{Q} \in \mathcal{L}_{k+1}} \Phi_{\text{lb}}(\mathcal{Q}); \\

    \quad U_{k+1} := \min_{\mathcal{Q} \in \mathcal{L}_{k+1}} \Phi_{\text{ub}}(\mathcal{Q}); \\

    \quad k := k + 1; \\

   \}\\

   $

   要求沿所选矩形最长边分割，此规则控制划分中矩形的条件数，其收敛性证明见[§1.1](https://web.stanford.edu/class/ee392o/bb.pdf). 



   在$k$次迭代结束时，$U_k$和$L_k$分别是$\Phi_{\min}(\mathcal{Q}_{\text{init}})$的上界和下界. 我们在[§1.1](https://web.stanford.edu/class/ee392o/bb.pdf)中证明，若界$\Phi_{\text{lb}}(\mathcal{Q})$和$\Phi_{\text{ub}}(\mathcal{Q})$满足条件（R2），则$U_k - L_k$必定收敛到零，因此分支定界算法将在有限步内终止.   



   ## 4 剪枝



   显然，在上述分支过程中，矩形数量等于迭代次数$N$. 不过，我们常常可以排除一些矩形；由于$\Phi_{\min}(\mathcal{Q}_{\text{init}})$无法在这些矩形中取得，因此可以将其“剪枝”. 具体操作如下：每次迭代时，从列表$\mathcal{L}_k$中移除满足$\Phi_{\text{lb}}(\mathcal{Q}) > U_k$的矩形$\mathcal{Q} \in \mathcal{L}_k$.   



   如果矩形$\mathcal{Q} \in \mathcal{L}_k$满足此条件，那么$q \in \mathcal{Q} \implies f(q) > U_k$；然而，$f(q)$在$\mathcal{Q}_{\text{init}}$上的最小值必定小于$U_k$，因此不可能在$\mathcal{Q}$中找到该最小值.   



   尽管剪枝对算法运行不是必需的，但它确实减少了存储需求. 算法通常会快速剪枝$\mathcal{Q}_{\text{init}}$的大部分区域，仅处理剩余的一小部分子集. 集合$\mathcal{L}_k$（即剪枝后列表中矩形的并集）充当$f$极小值点集的近似. 事实上，可保证$f$的每个极小值点都在$\mathcal{L}_k$中.   



   “剪枝”这一术语源于以下视角：该算法可视为生长一棵二叉树，其中节点对应当前划分$\mathcal{L}_k$中的矩形，给定节点的子节点代表分割该矩形得到的两部分. 通过排除某个矩形，我们对这棵树进行剪枝.  -->

