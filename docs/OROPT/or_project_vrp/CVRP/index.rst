有容量限制的车辆路径问题（Capacitated Vehicle Routing Problem, CVRP）
=====================================================================



Reference

---------



-  https://arxiv.org/pdf/1606.01935



1 问题概述

----------



CVRP

是车辆路径问题（VRP）的经典变体，聚焦于在车辆容量受限的条件下，优化配送路径.

其核心是规划一组车辆从中心 depot

出发，访问多个客户点，在满足每个客户需求且不超过车辆容量的前提下，最小化总行驶成本（如距离、时间等）.



| **问题目标**

| CVRP（有容量限制的车辆路径问题）的核心目标是在满足车辆容量约束的前提下，优化车辆行驶路径，以实现以下一项或多项优化指标：

| -

  **最小化总行驶距离**\ ：降低物流配送中的运输成本，这是最常见的优化目标.

| -

  **最小化总运输时间**\ ：提升配送效率，适用于对时效性要求高的场景（如生鲜配送）.

| -

  **最小化车辆使用数量**\ ：在满足需求的前提下，减少投入的车辆资源，降低运营成本.



| **问题约束**

| 1. **车辆容量约束**

| -

  每辆车辆有固定的容量（如载重量、体积限制），每条路径上所有客户的需求总和不能超过车辆容量.

  例如，若车辆容量为10吨，服务的客户需求分别为3吨、4吨、2吨，总和9吨（≤10吨）才符合约束.



2. **客户访问约束**



   -  **唯一性**\ ：每个客户必须且只能被一辆车访问一次，确保需求被满足且不重复服务.

   -  **需求满足**\ ：客户的货物需求必须被完全满足，即车辆对客户的配送量等于客户需求.



3. **车辆运行逻辑约束**



   -  **起点与终点**\ ：所有车辆必须从中心

      depot（如仓库、配送中心）出发，完成任务后返回 depot，形成闭合路径.

   -  **路径连贯性**\ ：车辆在路径中按顺序访问客户，行驶逻辑需符合实际交通规则（如无向图中双向可达，有向图中按指定方向行驶）.



4. **变量取值约束**



   -  决策变量（如车辆是否行驶某条路径）通常为二进制（0或1），表示“是否选择”该路径或服务关系.



这些目标与约束的结合，使CVRP成为复杂的组合优化问题，需通过算法平衡优化效果与约束满足，广泛应用于物流、供应链等实际场景.



| **求解方法**

| 1. **精确算法**\ ：

| -

  适用于小规模问题，如分支定界法、动态规划，但计算复杂度高（随问题规模呈指数增长）.

| 2. **启发式与元启发式算法**\ ：

| - **构造算法**\ ：如节约算法（Clarke-Wright），通过合并路径减少总距离.

| -

  **元启发式算法**\ ：遗传算法、模拟退火、蚁群优化、禁忌搜索等，通过迭代搜索近似最优解，适用于大规模问题.

| 3. **近似算法**\ ：如基于扫描法的路径构建，快速生成可行解.



| **应用场景**

| - **物流与配送**\ ：快递运输、货物配送路线规划.

| - **供应链管理**\ ：原材料运输、库存补货路径优化.

| -

  **服务行业**\ ：移动服务（如维修、家政）的路线安排，平衡服务需求与车辆/人员容量.



CVRP

因其复杂的约束和实际价值，成为组合优化领域的研究热点，推动了算法设计、运筹学等领域的发展.



2 问题数学公式表达（双指标车辆流公式）

--------------------------------------



用\ :math:`\mathcal{C}=\{ 1, \dots, n \}`

标记客户，\ :math:`\{0,n+1\}`\ 标记仓库depot.

令\ :math:`\mathcal{N}=\mathcal{C}\cup\{0,n+1\}`.



在双指标VF公式中，对于\ :math:`i， j\in\mathcal{N}`\ ，我们定义二元决策变量\ :math:`x_{ij}`\ ，\ :math:`x_{ij}=1`\ 当且仅当存在从顾客i直接到达j的路径.



| CVRP对应的双指标车辆流公式需要用到的变量： -



  .. math::



      

         x_{ij}= 

         \begin{cases} 

         1 & \text{路径从城市 } i \text{ 到城市 } j \\ 

         0 & \text{否则} 

         \end{cases} 

         

| - $ c\_{ij} > 0 $ 定义为从城市 $ i $ 到城市 $ j $ 的成本（距离）.



-  :math:`K`: 仓库depot中的车辆数目

-  :math:`Q`: 每辆车的最大容量

-  :math:`q_i`: 客户\ :math:`i`\ 的需求量

-  $ y_i

   :math:`:  车辆在订单`\ i\ :math:`（对应客户`\ i$）的出发地开始装货的重量.



CVRP为以下整数线性规划问题：



$$ :raw-latex:`\begin{align*}

&\min\ \sum_{i=0}^{n+1} \sum_{j=0}^{n+1} c_{ij}x_{ij} &\quad (2.1)\\

&\sum_{\substack{j=1 \\ j \neq i}}^{n+1} x_{ij} = 1, \quad i = 1, \dots, n, &\quad (2.2)\\

&\sum_{\substack{i=0 \\ i \neq h}}^{n} x_{ih} - \sum_{\substack{j=1 \\ j \neq h}}^{n+1} x_{hj} = 0, \quad h = 1, \dots, n, &\quad (2.3)\\

&\sum_{j=1}^{n} x_{0j} \leq K, &\quad (2.4)\\



&y_{j} \geq y_{i} + q_{j}x_{ij} - Q(1 - x_{ij}), \quad i,j = 0, \dots, n + 1, &\quad (2.5)\\



&q_{i} \leq y_{i} \leq Q, \quad i = 0, \dots, n + 1, &\quad (2.6)\\



&x_{ij} \in \{0,1\}, \quad i,j = 0, \dots, n + 1. &\quad (2.7)

\end{align*}` $$



约束 (2.2) 确保所有客户恰好被访问一次. 约束 (2.3)

保证车辆在弧线上的正确流向，即若车辆到达节点 $ h $，则必须从该节点出发.

约束 (2.4) 将最大路径数量限制为 $ K $（车辆数量）. 约束 (2.5) 和 (2.6)

共同确保不超过车辆容量. 目标函数由 (2.1)

定义，要求最小化路径的总行驶成本.



约束 (2.5)

其实也是是MTZ公式的变形，还可以避免解中出现子回路（即不经过配送中心的循环路径）.

使用 (2.5) 和 (2.6)

的优势在于：就客户数量而言，该模型的约束数量呈多项式级.

然而，该模型线性松弛提供的下界相比其他模型更弱.



3 问题数学公式表达（集合划分公式，SP）

--------------------------------------



目前，求解车辆路径问题（VRP）变体最有效的精确方法基于集合划分（SP）公式.

SP公式中的变量对应问题的可行路径. 设 $ :raw-latex:`\mathcal{R}` $

为满足问题要求的路径集合. 例如，在有容量限制的车辆路径问题（CVRP）中，$

:raw-latex:`\mathcal{R}` $

中的路径必须从配送中心出发并返回，最多访问客户一次，遵守车辆容量限制，并确保若路径到达某客户，则必须离开该客户.



| 设 $ :raw-latex:`\lambda`\ *r $ 为二进制决策变量，当且仅当选择路径 $ r

  :raw-latex:`\in `:raw-latex:`\mathcal{R}` $ 时，$

  :raw-latex:`\lambda`\ r = 1 :math:`. SP公式如下：`\ $

  :raw-latex:`\begin{alignat*}{3}

  \min & \quad \sum_{r \in \mathcal{R}} c_r \lambda_r \quad & (3.1) \\

  \text{s.t.} & \quad \sum_{r \in \mathcal{R}} a_{ri} \lambda_r = 1, & \quad i \in \mathcal{C}, \quad (3.2) \\

  & \quad \sum_{r \in \mathcal{R}} \lambda_r \leq K, & \quad (3.3) \\

  & \quad \lambda_r \in \{0,1\}, & \quad r \in \mathcal{R}. \quad (3.4)

  \end{alignat*}`



  .. math::



       

     这可用于为CVRP、VRPTW和许多其他VRP变体建模，具体取决于对路径集合 $ \mathcal{R} $ 的定义. 目标函数（3.1）最小化所选路径的总成本. 路径 $ r \in \mathcal{R} $ 的成本 $ c_r $，使用弧成本 $ c_{ij} $ 计算. 即，给定依次访问节点 $ i_0, i_1, \dots, i_p $（$ p > 0 $）的路径 $ r $，其总成本为：  



  c_r = :raw-latex:`\sum`\ {j=0}^{p-1} c*\ {i_j i\_{j+1}}.

  :raw-latex:`\quad `(3.5) $$

| 约束（3.2）强制每个客户节点恰好被访问一次. 每一列 $ a_r = (a\_{r1},

  :raw-latex:`\dots`, a\_{rn})^T $ 是二进制向量，其中 $ a\_{ri} = 1 $

  当且仅当路径 $ r $ 访问客户 $ i $.

  约束（3.3）限制配送中心可用车辆的最大数量. 若 $ K $

  对问题足够大，可删除该约束.



通常，一般来说，生成\ :math:`\mathcal{R}`\ 中的所有路径是不切实际的，因其数量随客户数呈指数增长.

因此，集合划分公式需要使用列生成技术求解模型（3.1）-（3.4）的线性松弛.

为获得最优整数解，需借助分支定价方法.



| 在列生成技术中，我们从路径的一个小子集

  :math:`\overline{\mathcal{R}} \subset \mathcal{R}`

  开始，该子集用于创建以下受限主问题（RMP）：

| 



  .. math::





     \begin{alignat*}{3}

     \min & \quad \sum_{r \in \overline{\mathcal{R}}} c_r \lambda_r \quad & (3.6) \\

     \text{s.t.} & \quad \sum_{r \in \overline{\mathcal{R}}} a_{ri} \lambda_r = 1, & \quad i \in \mathcal{C}, \quad (3.7) &\quad \text{(RMP)}\\

     & \quad \sum_{r \in \overline{\mathcal{R}}} \lambda_r \leq K, & \quad (3.8) \\

     & \quad \lambda_r \geq 0, & \quad r \in \overline{\mathcal{R}}. \quad (3.9)

     \end{alignat*}

| 注意，RMP 是（3.1）–（3.4）的线性松弛，但仅考虑变量的一个子集. 设 $ u

  = (u_1, :raw-latex:`\dots`, u_n)

  :raw-latex:`\in `:raw-latex:`\mathbb{R}`^n $ 和 $

  :raw-latex:`\sigma `:raw-latex:`\geq 0` $

  分别为与约束（3.7）和（3.8）相关的对偶变量.

  在列生成方法的每次迭代中，我们求解(RMP)以获得对偶解

  :math:`(\bar{u}, \bar{\sigma})`\ ，该解用于生成尚未在

  (RMP)中的变量/列\ :math:`\lambda_{r}(r\in\mathcal{R}\backslash \overline{\mathcal{R}})`.

  需要加入的列的对应下标\ :math:`r`\ 通过求解以下子问题得到：

| 



  .. math::





     \overline{s}=\min_{r\in\mathcal{R}} c_r - \sum_{i \in \mathcal{C}} \overline{u}_i a_{ri} - \overline{\sigma} =\sum_{i \in \mathcal{N}} \sum_{j \in \mathcal{N}} (c_{ij} - \bar{u}_i)x_{rij} - \bar{\sigma} \quad (3.10)



其中，\ :math:`\bar{u}_0 = \bar{u}_{n+1} = 0`\ ，且

:math:`x_r = \{x_{rij}\}_{i,j \in N}` 是一个二进制向量，当且仅当路径

:math:`r \in \mathcal{R}` 访问节点 :math:`i` 并直接前往节点 :math:`j`

时，\ :math:`x_{rij} = 1`.

这个子问题是一个\ **资源受限基本最短路问题（ESPPRC）**.

若\ :math:`\overline{s}`\ 为负数且有限，则\ :math:`\lambda_{\overline{r}}`

被添加到(RMP)中，然后重新求解新的(RMP). 如果\ :math:`\overline{s}`

非负，且 :math:`(\bar{u}, \bar{\sigma})` 是当前 RMP

的最优对偶解，那么当前(RMP)的最优解对于主问题（MP）的线性松弛也是最优的.

至此，列生成方法终止.

（注意：只要求出最小成本路径加入(RMP)即可，下标\ :math:`r`\ 无需求出，这里只是为了保证理论严谨）.



列生成算法的计算实现性能在很大程度上取决于 RMP 和子问题的求解方式.

为确保成功，实现过程应快速求解 RMP，并使用稳定的对偶解以减少总迭代次数.

有效求解 ESPPRC 也是列生成算法处理 VRP 变体的重要要求. 尽管存在 ESPPRC

的整数规划公式，但当前最先进的优化求解器无法有效求解它们.

目前最佳策略是使用基于动态规划的\ **标签设置算法**.



   --------------



   求解(RMP)对偶问题：\ :math:`\\` 引入拉格朗日乘子 $ u_i

   $（对应等式约束 $ :raw-latex:`\sum`\ *{r

   :raw-latex:`\in `:raw-latex:`\overline{\mathcal{R}}`} a*\ {ri}

   :raw-latex:`\lambda`\ *r = 1 $）和 $

   :raw-latex:`\sigma `:raw-latex:`\geq 0` $（对应不等式约束 $

   :raw-latex:`\sum`*\ {r

   :raw-latex:`\in `:raw-latex:`\overline{\mathcal{R}}`}

   :raw-latex:`\lambda`\ *r :raw-latex:`\leq `K

   :math:`），拉格朗日函数为：`\ $ L(:raw-latex:`\lambda`, u,

   :raw-latex:`\sigma`) = :raw-latex:`\sum`*\ {r

   :raw-latex:`\in `:raw-latex:`\overline{\mathcal{R}}`} c_r

   :raw-latex:`\lambda`\ *r + :raw-latex:`\sum`*\ {i

   :raw-latex:`\in `:raw-latex:`\mathcal{C}`} u_i :raw-latex:`\left`(1 -

   :raw-latex:`\sum`\ *{r

   :raw-latex:`\in `:raw-latex:`\overline{\mathcal{R}}`} a*\ {ri}

   :raw-latex:`\lambda`\ *r :raw-latex:`\right`) +

   :raw-latex:`\sigma `:raw-latex:`\left`(K - :raw-latex:`\sum`*\ {r

   :raw-latex:`\in `:raw-latex:`\overline{\mathcal{R}}`}

   :raw-latex:`\lambda`\ *r :raw-latex:`\right`).



   .. math::



         

      对$\lambda$求导：$ \frac{\partial L(\lambda, u, \sigma)}{\partial \lambda} =\sum\limits_{r\in\overline{R}}\big( c_r - \sum_{i \in \mathcal{C}} u_i a_{ri} - \sigma \big)$ . 由于 $ \lambda_r \geq 0 $，当 $ c_r - \sum_{i \in \mathcal{C}} u_i a_{ri} - \sigma \geq 0 $ 时，$ \lambda_r $ 取 $ 0 $ 可最小化 $ L $；若存在 $ r $ 使 $ c_r - \sum_{i \in \mathcal{C}} u_i a_{ri} - \sigma < 0 $，则 $ L $ 无下界（趋于 $ -\infty $）. 因此：  



   :raw-latex:`\min`*\ {:raw-latex:`\lambda`}L(:raw-latex:`\lambda`, u,

   :raw-latex:`\sigma`) = \\



   .. raw:: latex



      \begin{cases} 

      \sum_{i \in \mathcal{C}} u_i + \sigma K, & \text{若 } c_r - \sum_{i \in \mathcal{C}} u_i a_{ri} - \sigma \geq 0, \forall r \in \overline{\mathcal{R}}, \\

      -\infty, & \text{否则}.

      \end{cases}



   .. math::



        

      因此，对偶问题  



   :raw-latex:`\begin{alignat*}{3}

   \max & \quad \sum_{i \in \mathcal{C}} u_i + K\sigma \\

   \text{s.t.} & \quad \sum_{i \in \mathcal{C}} a_{ri} u_i + \sigma \leq c_r, & \quad \forall r \in \overline{\mathcal{R}}, \\

   & \quad \sigma \geq 0.

   \end{alignat*}`



   .. math::



        

      根据[行生成和列生成在大规模线性规划中的使用](../../or_exact/LP_large_scale_models/README.md)的列生成算法，假设对偶问题的最优解为$(\overline{u},\overline{\sigma})$，那么子问题求解



   :raw-latex:`\overline{r}` =

   :raw-latex:`\arg`:raw-latex:`\min`\ *{r:raw-latex:`\in`:raw-latex:`\mathcal{R}`}

   c_r - :raw-latex:`\sum`*\ {i

   :raw-latex:`\in `:raw-latex:`\mathcal{C}`}

   :raw-latex:`\overline{u}`\ *i a*\ {ri} -

   :raw-latex:`\overline{\sigma}` $$



..



   --------------



   | 为什么(3.10)是一个资源受限基本最短路问题（ESPPRC）？\ :math:`\\`

     该问题被认定为资源受限基本最短路径问题（ESPPRC），原因如下：

   | 资源受限体现在：(3.10)的可行解需要对应CVRP的可行路径，受到载重约束、路径联通约束的限制.

   | 基本最短路径体现在：目标函数 $ :raw-latex:`\bar`{s} =

     :raw-latex:`\min`\ *{r :raw-latex:`\in `:raw-latex:`\mathcal{R}`}

     c_r - :raw-latex:`\sum`*\ {i :raw-latex:`\in `C}

     :raw-latex:`\bar`{u}\ *i a*\ {ri} -

     :raw-latex:`\bar`{:raw-latex:`\sigma`} $

     本质是在资源约束下寻找成本最低的可行路径.



CVRPTW子问题ESPPRC的数学公式表达：



1. 变量定义



   .. math::



       x_{ij} = 

      \begin{cases} 

      1, & \text{如果最短路径中包含弧 } (i,j) \in \mathcal{N}  \times \mathcal{N}  \\

      0, & \text{否则}

      \end{cases}



   $ s_i $：到达点 $ i :raw-latex:`\in `:raw-latex:`\mathcal{N}` $

   的时刻



2. 数学模型表达式



   -  目标函数



      .. math::





          \min \sum_{i \in \mathcal{N}} \sum_{j \in \mathcal{N}} （c_{ij}-\overline{u}_i)x_{ij} -\overline{\sigma} \quad (1.1)

          



      目标是最小化路径中所有弧的成本总和.



   -  **容量约束**\ ：



      .. math::





          \sum_{i \in C} q_i \sum_{j \in \mathcal{N}} x_{ij} \leq Q \quad (1.2)

          



      确保客户节点需求量总和不超过车辆容量 $ Q $.



   -  **从起点出发**\ ：



      .. math::





          \sum_{j \in \mathcal{N}} x_{0j} = 1 \quad (1.3)

          



      保证路径从起点（节点 $ 0 $）出发.



   -  **流量守恒**\ ：



      .. math::





          \sum_{i \in \mathcal{N}} x_{ih} = \sum_{j \in \mathcal{N}} x_{hj} \quad \forall h \in C \quad (1.4)

          



      对每个客户节点 $ h $，流入弧的数量等于流出弧的数量.



   -  **到达终点**\ ：



      .. math::





          \sum_{i \in \mathcal{N}} x_{i,n+1} = 1 \quad (1.5)

          



      确保路径最终到达终点.



   -  **时间约束**\ ：



      .. math::





          s_i + t_{ij} \leq s_j + M_{ij}(1 - x_{ij}) \quad \forall i \in \mathcal{N}, \forall j \in \mathcal{N} \quad (1.6)

          



      利用大 $ M $ 法保证时间逻辑，若弧 $ (i,j) $ 未被选择（$ x\_{ij}=0

      :math:`），约束自动满足；若被选择（` x\_{ij}=1

      $），则保证时间先后关系.



   -  **时间窗约束**\ ：



      .. math::





          a_i \leq s_i \leq b_i \quad \forall i \in \mathcal{N} \quad (1.7)

          



      确保到达每个节点 $ i $ 的时刻 $ s_i $ 在规定的时间窗 $ [a_i, b_i]

      $ 内.



   -  **节点自身约束**\ ：



      由于任何节点都不能是自己的前继节点或者后继节点，因此需添加以下约束：



      .. math::





          x_{ii} = 0 \quad \forall i \in V \quad (1.9)

          



   -  **变量取值约束**\ ：



      .. math::





          x_{ij} \in \{0,1\} \quad \forall i \in \mathcal{N}, \forall j \in \mathcal{N} \quad (1.8)

          



      明确 $ x\_{ij} $ 为 0-1 变量.

