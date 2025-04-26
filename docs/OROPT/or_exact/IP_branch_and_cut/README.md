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

-  令 $\mathcal{L} = \mathcal{D}$，初始化 $\hat{x} $  
- **While** $\mathcal{L} \neq \emptyset$ **do**  
-   - 从 $\mathcal{L}$ 中选择待探索的子集合 $\mathcal{S}$ 
-   - 求 $(\mathcal{S},f)$ 的线性松弛问题的解 $\hat{x}'$
-   - **If** $\hat{x}'$是不可行解 **or** $\hat{x}'$是分数可行解，且 $f（\hat{x}'）\leq f(\hat{x})$ **then** 
-   -   - $\mathcal{S}$赋予可以剪枝属性 
-   - **else if**  $ \hat{x}' $是分数可行解，且$f
（\hat{x}'）> f(\hat{x})$ **then** 
-   -   - $\mathcal{S}$赋予不可剪枝属性 
-   - **If** 需要添加切平面 **then**  
-   -   - 找到分离 $\hat{x}'$ 与 $\mathcal{S}$ 的割平面 $\langle \boldsymbol{a}, \hat{x}' \rangle \leq \beta$  
-   -   - $\mathcal{S}_{t+1} \leftarrow \mathcal{S}_t \cap \{ x \mid \langle \boldsymbol{a}, \hat{x}' \rangle \leq \beta \}$ 
-   -   - 返回第4行  
-   - **else if** $\hat{x}'$是整数可行解 **then** 
-   -   - $\hat{x} = \hat{x}'$  
-   -   - $\mathcal{S}$赋予可以剪枝属性 
-   - **end if** 
-   - **if** $\mathcal{S}$不可剪枝 **then** 
-   -   - 将 $ \mathcal{S} $ 划分为 $ \mathcal{S}_1, \mathcal{S}_2, \dots, \mathcal{S}_r $  
-   -   - 将 $ \mathcal{S}_1, \mathcal{S}_2, \dots, \mathcal{S}_r $ 加入 $ \mathcal{L} $ 
-   - **end if**  
-   - 从 $ \mathcal{L} $ 中移除 $ \mathcal{S} $  
- **end while**  
- **return** $ \hat{x} $  