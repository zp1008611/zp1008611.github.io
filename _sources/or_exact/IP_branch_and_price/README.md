# 分支定价

- https://dabeenl.github.io/IE631_lecture23_note.pdf
- https://www.zib.de/userpage/gamrath/publications/gamrath2010_genericBCP.pdf



### 2 基于Dantzig-Wolfe分解的分支定价法  
考虑如下混合整数规划：  
$$
\begin{align*}
z_I = \max & \quad c^\top x \\
\text{s.t.} & \quad Ax \leq b \\
& \quad Ex \leq f \tag{MIP} \\
& \quad x \in \mathbb{Z}_+^d \times \mathbb{R}_+^p.
\end{align*}
$$  
定义集合 $ Q $ 如下：  
$$
Q = \left\{ x \in \mathbb{Z}_+^d \times \mathbb{R}_+^p : Ax \leq b \right\}.
$$  
假设 $\text{conv}(Q)$ 可表示为：  
$$
\text{conv}(Q) = \text{conv}\{v^1, \ldots, v^n\} + \text{cone}\{r^1, \ldots, r^\ell\}
$$  
其中为某些向量 $v^1, \ldots, v^n$ 和 $r^1, \ldots, r^\ell$. 回顾，（MIP）的丹齐格－沃尔夫松弛由下式给出：  
$$
\begin{align*}
z_{\text{LD}} = \max & \sum_{k \in [n]} (c^\top v^k) \alpha_k + \sum_{h \in [\ell]} (c^\top r^h) \beta_k \\
\text{s.t.} & \sum_{k \in [n]} (E v^k) \alpha_k + \sum_{h \in [\ell]} (E r^h) \beta_k \leq f \tag{DW} \\
& \sum_{k \in [n]} \alpha_k = 1 \\
& \alpha \in \mathbb{R}_+^k,\ \beta \in \mathbb{R}_+^\ell.
\end{align*}
$$  
（DW）是（MIP）的一种松弛，为恢复整数约束，通过添加  
$$
x_j = \sum_{k \in [n]} \alpha_k v_j^k + \sum_{h \in [\ell]} \beta_h r_j^h \in \mathbb{Z},\quad j \in [d].
$$  
进而，可将分支定界框架应用于Dantzig-Wolfe松弛（DW），基本工作流程如下：  

1. 使用列生成算法求解（DW），获得最优解 $(\alpha^*, \beta^*)$，由此得到  
$$
x^* = \sum_{k \in [n]} \alpha_k^* v^k + \sum_{h \in [\ell]} \beta_h^* r^h.
$$  
2. 若对某些 $j \in [d]$，有 $x_j^* \notin \mathbb{Z}$，则基于析取创建两个子问题：  
$$
\sum_{k \in [n]} \alpha_k v_j^k + \sum_{h \in [\ell]} \beta_h r_j^h \geq \lceil x_j^* \rceil\ \text{ 或 }\ \sum_{k \in [n]} \alpha_k v_j^k + \sum_{h \in [\ell]} \beta_h r_j^h \leq \lfloor x_j^* \rfloor.
$$  
3. 对各子问题重复上述流程. 

由于使用列生成算法求解线性规划问题时需要求解定价子问题，所以在分支定界中使用列生成算法求解松弛问题（线性松弛或者Dantzig-Wolfe松弛）的算法叫做**分支定价算法**. 

**算法1 分支定价法**  
1  令 $ \mathcal{L} = \mathcal{D} $，初始化 $ \hat{x} $  
2 **while** $ \mathcal{L} \neq \emptyset $ **do**  
3 $\quad$ 从 $ \mathcal{L} $ 中选择待探索的子集合 $ \mathcal{S}$ $\\$
4 $\quad$ 使用列生成算法求$(\mathcal{S},f)$的松弛问题的解$\hat{x}'$ $\\$
5 $\quad$ **if** $ \hat{x}' $是不可行解 **or** $ \hat{x}' $是分数可行解，且$f（\hat{x}'）\leq f(\hat{x})$ **then** $\\$
6 $\quad\quad$ $\mathcal{S}$赋予可以剪枝属性 $\\$
7   $\quad$ **else if**  $ \hat{x}' $是分数可行解，且$f
（\hat{x}'）> f(\hat{x})$ **then** $\\$
8 $\quad\quad$ $\mathcal{S}$赋予不可剪枝属性 $\\$
9 $\quad$ **else if** $ \hat{x}' $是整数可行解 **then** $\\$
10 $\quad\ \ \ $ $ \hat{x} = \hat{x}' $  $\\$
11 $\quad\ \ \ $  $\mathcal{S}$赋予可以剪枝属性 $\\$
12 $\ \ \ $ **end if** $\\$
13 $\ \ \ $ **if** $\mathcal{S}$不可剪枝 **then** $\\$
14 $\quad\ \ \ $ 将 $ \mathcal{S} $ 划分为 $ \mathcal{S}_1, \mathcal{S}_2, \dots, \mathcal{S}_r $  
15 $\quad\ \ \ $ 将 $ \mathcal{S}_1, \mathcal{S}_2, \dots, \mathcal{S}_r $ 加入 $ \mathcal{L} $ $\\$
16 $\ \ \ $ **end if**  $\\$
17 $\ \ \ $ 从 $ \mathcal{L} $ 中移除 $ \mathcal{S} $  
18 **end while**  
19 **return** $ \hat{x} $ 