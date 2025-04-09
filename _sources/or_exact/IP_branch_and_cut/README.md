# 分支切割

## Reference

- https://en.wikipedia.org/wiki/Branch_and_cut
- https://en.wikipedia.org/wiki/Branch_and_price
- https://or.rwth-aachen.de/files/research/publications/branch-and-price.pdf
- https://homes.di.unimi.it/righini/Didattica/ComplementiRicercaOperativa/MaterialeCRO/2000%20-%20Mitchell%20-%20branch-and-cut.pdf
- https://optimization-online.org/wp-content/uploads/2008/06/1997.pdf

在[凸包和有效不等式](..\IP_convex_hull_and_valid_ineq\README.md)
的内容里，我们简单介绍了一下分支切割算法，下面给出完整的算法框架形式.

## 分支切割
 
考虑混合整数线性规划  
$$
z^* = \max \{ f(x) : x \in \mathcal{D} \} 
$$  
其中  
$$
f(x) = c^Tx, c\in\mathbb{R}^n\\
\mathcal{D} = \{ x \in \mathbb{R}^n_+\mid A x \leq b,\, ,\, x_j \in \mathbb{Z}_+,\, \forall j \in I \}.
$$ 

**算法1 分支切割法**  
1  令 $ \mathcal{L} = \mathcal{D} $，初始化 $ \hat{x} $  
2 **while** $ \mathcal{L} \neq \emptyset $ **do**  
3 $\quad$ 从 $ \mathcal{L} $ 中选择待探索的子集合 $ \mathcal{S}$ $\\$
4 $\quad$ 求$(\mathcal{S},f)$的线性松弛问题的解$\hat{x}'$ $\\$
5 $\quad$ **if** $ \hat{x}' $是不可行解 **or** $ \hat{x}' $是分数可行解，且$f（\hat{x}'）\leq f(\hat{x})$ **then** $\\$
6 $\quad\quad$ $\mathcal{S}$赋予可以剪枝属性 $\\$
7   $\quad$ **else if**  $ \hat{x}' $是分数可行解，且$f
（\hat{x}'）> f(\hat{x})$ **then** $\\$
8 $\quad\quad$ $\mathcal{S}$赋予不可剪枝属性 $\\$
9 $\quad\quad$ **if** 需要添加切平面 **then** $\\$ 
10 $\quad\quad\quad$ 找到分离 $ \hat{x}' $ 与 $ \mathcal{S} $ 的割平面 $ \langle \boldsymbol{a}, \hat{x}' \rangle \leq \beta $  
11 $\quad\quad\quad$ $ \mathcal{S}_{t+1} \leftarrow \mathcal{S}_t \cap \{ x \mid \langle \boldsymbol{a}, \hat{x}' \rangle \leq \beta \} $ $\\$
11 $\quad\quad\quad$ 返回第4行  $\\$
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