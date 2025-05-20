Elementary Shortest Path Problem with Resource Constraints (ESPPRC)
===================================================================



Reference

=========



-  https://eva.fing.edu.uy/pluginfile.php/277396/mod_resource/content/1/Lozano-ESPPRC-TS-final-2016.pdf

-  https://onlinelibrary.wiley.com/doi/epdf/10.1002/net.20033



在\ `CVRP <../CVRP/README.md>`__\ 的用列生成算法求解SP模型中，我们得到了一个ESPPRC子问题:



.. math::





   \min_{r\in\mathcal{R}}\ \sum_{i \in \mathcal{N}} \sum_{j \in \mathcal{N}} (c_{ij} - \bar{u}_i)x_{rij} - \bar{\sigma}\\



由于\ :math:`r`\ 是CVRP问题的一条可行路径，则\ :math:`r`\ 满足以下约束

$$ :raw-latex:`\begin{align*}

&

\sum\limits_{i\in\mathcal{N}}\sum_{j \in \mathcal{N}}x_{rij}-\sum\limits_{i\in\mathcal{N}}\sum_{j \in \mathcal{N}}x_{rji} = 0,

\\



&y_{rj} \geq y_{ri} + q_{rj}x_{rij} - Q(1 - x_{rij}),\\



&q_{ri} \leq y_{ri} \leq Q,\\



&x_{rij} \in \{0,1\}, \quad i,j \in\mathcal{N}. 

\end{align*}`



.. math::





   由于这里指标$r$无作用，子问题可表示为：



:raw-latex:`\begin{align*}

&\min\ \sum_{i \in \mathcal{N}} \sum_{j \in \mathcal{N}} (c_{ij} - \bar{u}_i)x_{ij} - \bar{\sigma}\\

&

\sum\limits_{i\in\mathcal{N}}\sum_{j \in \mathcal{N}}x_{ij}-\sum\limits_{i\in\mathcal{N}}\sum_{j \in \mathcal{N}}x_{ji} = 0,

\\



&y_{j} \geq y_{i} + q_{j}x_{ij} - Q(1 - x_{ij}), \quad i,j \in \mathcal{N}\\



&q_{i} \leq y_{i} \leq Q, \quad i\in \mathcal{N},\\



&x_{ij} \in \{0,1\}, \quad i,j \in\mathcal{N}. 

\end{align*}` $$ 下面我们研究ESPPRC问题的求解.



1 元启发式算法

--------------



2 Labeling Algorithm 和 Pulse Algorithm

---------------------------------------



2.1 文献综述

~~~~~~~~~~~~



ESPPRC 是强 NP 难问题（Dror，1994）. Desrochers、Desrosiers 和

Solomon（1992）通过松弛变量设计动态规划（DP）算法，其线性松弛虽能提供弱下界与大分支定界，但允许路径循环.

Irnich 和 Villeneuve（2006）、Feillet 等（2004）首次提出 ESPPRC

精确算法，采用标记算法. Desrochers、Desrosiers 和

Solomon（1992）的算法包含客户访问指示，若客户未被列生成过程中的部分路径访问，可通过扩展算法处理.

Feillet 等（2004）证明，使用 ESPPRC 能提升分支定价算法每节点的下界.

Rousseau 等（2004）通过处理容量规划约束（CP）的分支定价方法求解

VRPTW，尽管 CP 组件灵活，但该方法与传统分支定价策略相比，速度略显不足.

受 Feillet 等（2004）启发，Chabrier（2006）将 ESPPRC 嵌入 VRPTW

分支定价框架，成功求解 17 个此前未解决的 Solomon 测试集开放实例.

随后，Feillet、Gendreau 和 Rousseau（2007）提出优化改进，减少 ESPPRC

子问题求解的计算时间. 近期，Righini 和

Salani（2008）提出基于状态空间松弛的动态标记算法，显著提升算法性能，优于

Feillet 等（2004）和 Chabrier（2006）的算法. Boland、Dethridge 和

Dumitrescu（2006）提出随机生成的算法，在测试实例中表现出色.

Lately、Jensen 等（2008）和 Petersen、Pisinger 与

Spoorendonk（2008）引入子集行不等式，提升分支定价算法下界，但增加问题复杂度.

Balseur、Desaulniers、Lessaud 和

Hadjar（2008）结合精确算法中的不等式，设计子问题搜索的禁忌算法，获取

Solomon 测试集 5 个实例的最优解.

此外，分支定价方法还结合列生成与割平面生成算法，如 Baldacci、Mingozzi 和

Roberti（2011）扩展的精确算法，Righini 和

Salani（2008）通过引入基于ng-route松弛的新函数计算部分路径完成边界，加速动态规划.



2.2 Pulse Algorithm

~~~~~~~~~~~~~~~~~~~



pulse algorithm（脉冲算法）与深度优先搜索（DFS） 有紧密联系. -

**联系**\ ： -

**搜索方式相似**\ ：深度优先搜索从起始节点开始，沿着一条路径尽可能深入地探索，直到无法继续或达到目标节点，然后回溯继续探索其他路径。脉冲算法也是以递归的方式探索图，从起始节点发送“脉冲”，沿着路径不断深入，当到达某个节点无法继续满足条件或探索完该节点所有可能的延伸时，就进行类似回溯的操作，去探索其他路径

，二者在探索路径的方式上思路相近。 -

**递归实现**\ ：深度优先搜索可以通过递归算法来实现，脉冲算法同样利用了递归过程来实现路径的探索，在实现手段上有一定的相似性。

- **区别**\ ： -

**约束处理和剪枝策略**\ ：脉冲算法在搜索过程中，会紧密结合资源约束（如车辆载重、时间窗等）进行判断和剪枝，当路径违反这些约束时，会直接舍弃该路径，避免无效搜索。而深度优先搜索本身并不专门针对资源约束进行处理，它主要侧重于遍历图的节点和路径。

-

**应用场景针对性**\ ：脉冲算法主要应用于资源约束下的最优路径求解问题，例如在车辆路径规划等场景中，考虑多种资源限制找到最优路径。深度优先搜索应用范围更广，不仅用于寻找路径，还常用于图的遍历、拓扑排序、判断连通性等多种图论相关问题

，以及一些涉及状态空间搜索的问题中。

