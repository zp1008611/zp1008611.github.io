# 列生成算法

## Reference

- https://www.cse.iitb.ac.in/~mitra/mtp/seminar/report/colgen.pdf
- https://imada.sdu.dk/u/jbj/DM209/Notes-DW-CG.pdf
- https://homes.di.unimi.it/righini/Didattica/ComplementiRicercaOperativa/MaterialeCRO/CG.pdf
- https://coral.ise.lehigh.edu/~ted/files/ie418/lectures/Lecture18.pdf


## 列生成算法思想 
对于线性规划问题
$$
\begin{align*}
\max \quad & \mathbf{c}^T \bar{\mathbf{x}} \\
\text{s.t.} \quad & \mathbf{A} \bar{\mathbf{x}} \leq \mathbf{b} \\
& \bar{\mathbf{x}} \geq \mathbf{0}
\end{align*}
$$
列生成的核心思想是求解一个**受限线性规划**，其中并非所有列都包含在单纯形表中，即并非所有变量都被允许成为基变量.   

在受限线性规划达到最优解后，我们已知所有**对偶变量**（$\lambda=c_B^TB^{-1}$）的值，进而可以提出问题：是否存在当前不在单纯形表中的列 $ j $，使得其在当前基解中的**检验数** $ \sigma_j $ 为正数？  

该问题的答案取决于列$ a_j $ 和对应成本系数 $ c_j $（即列的“结构”），因为 $ \sigma_j = c_j - \sum_{i=1}^{m} a_{ij}\lambda_i $.   

- 若答案为"否"，则可确定当前受限线性规划的最优解也是整个线性规划的最优解.   
- 若答案为"是"，则将检验数为负的列插入受限线性规划中，继续进行旋转变换（主元变换）. 
 


### 我们为何要使用列生成（CG）？  
将列生成应用于线性规划问题的主要原因，在于其**列（变量）的数量过多**.   

线性规划问题可能包含大量变量（例如，当变量有许多下标时）.   

单纯形算法的计算时间通常更多取决于约束条件的数量，而非变量的数量：因此，求解一个具有大量约束条件的线性规划问题的对偶问题，可能更为简便.   

线性规划问题可能呈现**块对角结构**，这样一来，当单独考虑关联约束时，它们可被分解为独立的子问题.   

线性规划问题也可能作为组合问题（具有指数级数量的变量）重构后的线性松弛形式出现. 






### 关于列生成的一些备注（1）  
**备注 1**：必须保证受限线性规划问题的**原问题可行性**. 为此，我们可添加一个或多个成本极高的虚拟列，其结构用于确保可行性.   
**备注 2**：无需确保**原问题有界性**：若受限线性规划无界，整个线性规划也必然无界.   
**备注 3**：当**正检验数对应列**被插入受限线性规划时，部分具有“较小”负检验数的**非基列**可从中删除. 这有助于在存储大型单纯形表时节省空间. 





### 关于列生成的一些备注（2）  
**备注 4**：我们可以在合适的数据结构中维护一个已知列的“库”，每次需要求解定价子问题时，就在库中搜索负检验数列. 被删除的列会存入该库，以备未来可能再次使用.   
**备注 5**：若没有列的显式列表，就必须对列有隐式描述. 此时，我们实际需要求解一个定价子问题（其本身就是优化问题）来生成列：  
$$
\begin{align*}
\operatorname{max} \quad & \sigma = c(\boldsymbol{a}) - \boldsymbol{a}^T\lambda  \\
\text{s.t.} \quad & \boldsymbol{a} \in \mathcal{A}
\end{align*}
$$  
其中，$\mathcal{A}$ 是可行列的集合，成本 $c$ 由列 $\boldsymbol{a}$ 决定. 在子问题中，列 $\boldsymbol{a}$ 充当变量的角色. 


### 定价  
在每次定价迭代中，不必一次仅生成一列，生成多个具有负检验数的列可能更为便利，这种方式称为**多重定价**.   

为加快列生成（CG），尽可能通过**启发式方法**生成负检验数列也较为实用. 但为确保不存在负检验数列，必须使用**精确优化算法**. 当启发式定价失效时，需借助**精确定价**. 


## 列生成算法具体步骤
1 令 $ k \leftarrow 0 $，$ \bar{\sigma}_{max} \leftarrow \infty $.

2 生成初始列并将其添加到受限集合 $ I_0 $ 中.

3 **while** $ \bar{\sigma}_{max} > 0 $ **do**  

4 $\ \ \ \ \ $ 求解受限主问题  
    $$
    \begin{align*}
    \max \quad & \sum_{i \in I_k} c_i x_i \\
    \text{s.t.} \quad & \sum_{i \in I_k} A_i x_i = b \tag{RMP} \\
    & x \geq 0
    \end{align*}
    $$  
    $\ \ \ \ \ \ \ $
    以获取对偶解 $ \lambda^k $.

5   $\ \ \ \ $
    求解列生成子问题，得到  
    $$
     \boldsymbol{a}^* \in \arg\max_{\boldsymbol{a} \in C} c(\boldsymbol{a}) - \boldsymbol{a}^T\lambda^k,  
    $$
    $\ \ \ \ \ \ $ 
    $C$是全部列所构成的集合. 并设定 $ \bar{\sigma}_{max} = c(\boldsymbol{a}) - \boldsymbol{a}^T{\lambda^{k}}$.  
6   $\ \ \ \ \ $
    **if** $ \bar{\sigma}_{max} > 0 $ **then**

7   $\ \ \ \ \ \ \ \ \ \ \ \ $
    $I_{k+1} \leftarrow I_k \cup \{a^*\} $

8   $\ \ \ \ \ $ 
    **end if**  

9   $\ \ \ \ \ $
    $ k \leftarrow k + 1 $  
10 **end while**




