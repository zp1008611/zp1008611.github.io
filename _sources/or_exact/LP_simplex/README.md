# 单纯形法

## Reference

- https://web.stanford.edu/class/msande310/lecture09.pdf
- https://web.stanford.edu/class/msande310/lecture10.pdf
- https://www.cse.iitb.ac.in/~mitra/mtp/seminar/report/colgen.pdf

- https://zh.wikipedia.org/wiki/%E5%8D%95%E7%BA%AF%E5%BD%A2%E6%B3%95







## **1. 理论基础**

在线性规划中，可行解、基本解、基本可行解和最优解是几个重要的概念，它们的含义和相互关系如下：
- **可行解**：满足线性规划所有约束条件（包括约束方程和变量非负约束）的解. 例如在线性规划标准型$\begin{cases}\max\ z = c^T x \\ \text{s.t.}\ Ax = b,\ x \geq 0\end{cases}$ 中，若$x$ 满足$Ax = b$ 且$x \geq 0$，则$x$ 就是可行解，所有可行解构成的集合被称为可行域，它是一个凸集. 
- **基本解**：对于线性规划问题，假设约束矩阵$A$ 的秩为$m$，从$A$ 中选取$m$ 阶非奇异子矩阵$B$（即基矩阵），将变量分为基变量$x_B$ 和非基变量$x_N$ . 令非基变量$x_N = 0$，通过求解$Bx_B = b$ 得到$x_B = B^{-1}b$，由此组合成的解$x = \begin{pmatrix}x_B \\ 0\end{pmatrix}$ 就是基本解. 基本解只考虑了约束方程，不要求变量满足非负约束，所以基本解不一定是可行解.  
- **基本可行解**：既满足基本解的定义，又满足变量非负约束（即$x\geq0$）的解. **从几何意义上讲，基本可行解对应着可行域的顶点，其数量是有限的. 如果线性规划问题有可行解，那么必然存在基本可行解**.  
- **最优解**：在所有可行解中，能使目标函数达到最大值（或最小值，根据具体问题而定）的解. **若线性规划问题存在有界最优解，那么最优解一定可以在基本可行解中找到**. 这是因为基本可行解对应着可行域的极点，而线性规划问题若有最优解，则一定可在可行域的极点上达到. 例如在一个简单的二维线性规划问题中，可行域是一个多边形，最优解就位于这个多边形的顶点（即基本可行解）处 . 

这四种解的关系是：可行解包含基本可行解；基本解不一定是可行解，满足非负约束的基本解才是基本可行解；最优解是在可行解范围内使目标函数最优的解，且最优解会在基本可行解中产生.  

单纯形法的思想就是通过寻找基本可行解来得到最优解.


## **2. 单纯形法思想**
将线性规划问题
$$
\begin{align*}
\max \quad & \mathbf{c}^T \bar{\mathbf{x}} \\
\text{s.t.} \quad & \mathbf{A} \bar{\mathbf{x}} \leq \mathbf{b} \\
& \bar{\mathbf{x}} \geq \mathbf{0}
\end{align*}
$$
表示为：
$$
\begin{align*}
\max \quad & \mathbf{c}^T \mathbf{x} \\
\text{s.t.} \quad & \mathbf{A} \mathbf{x} = \mathbf{b} \\
& \mathbf{x} \geq \mathbf{0}
\end{align*}
$$
其中：
- $\mathbf{A} \in \mathbb{R}^{m \times n}$ 是约束矩阵（$m$ 个约束，$n$ 个变量），
- $\mathbf{b} \in \mathbb{R}^m$ 是右端项向量，
- $\mathbf{c} \in \mathbb{R}^n$ 是目标函数系数向量. 
下面我们来解释 pivoting 步骤的算法. 

设$A = (a_1, a_2, \cdots, a_n)$，其中$a_j$是$A$的第$j$列. 因为$\text{rank}(A)=m$，所以存在一个$m\times m$的非奇异子矩阵$B=(a_{B_1}, a_{B_2}, \cdots, a_{B_m})$. 设$J = \{1, 2, \cdots, n\}$且$K = \{B_1, B_2, \cdots, B_m\}$，令$N = J\setminus K$. 现在对$A$的列进行重新排列，使得$A = (B, N)$. 我们可以将$Ax = b$写成$Bx_B + Nx_N = b$，其中$x = (x_B, x_N)$. 那么$Ax = b$的一个解为$x_B = B^{-1}b$且$x_N = 0$. 
$$
Ax = \begin{bmatrix} B & N \end{bmatrix}\begin{bmatrix} x_B \\ 0 \end{bmatrix} = b, \text{ 即 } x_B = B^{-1}b. 
$$
如果$x$是一个真正的角点（它是可行的），则需满足$x_B\geq0$ . 目标函数为
$$
z=cx = \begin{bmatrix} c_B & c_N \end{bmatrix}\begin{bmatrix} x_B \\ 0 \end{bmatrix} = c_B B^{-1}b. 
$$
 
问题是，在离开这个角点之后下一步该往哪里走?

 通过对$A$进行消元操作可以简化这个决策，该操作会将方阵部分$B$化为单位矩阵. 用矩阵符号表示，就是将$Ax = b$两边同时乘以$A_B^{-1}$
$$
\begin{bmatrix} I & B^{-1}N \end{bmatrix}\begin{bmatrix} x_B \\ 0 \end{bmatrix} = B^{-1}b. 
$$

这里设$m=3,n=5$, 那么$A=\begin{bmatrix} a_1 & a_2 &a_3&a_4&a_5\end{bmatrix}$, $a_i$是列向量. 

设$x_B=\begin{bmatrix} x_1\\x_2\\x_3 \end{bmatrix}$, $x_N=\begin{bmatrix} x_4\\x_5 \end{bmatrix}$，则
$$\begin{bmatrix} I & B^{-1}N \end{bmatrix}=
\begin{bmatrix} 
  1 & 0&0 & （B^{-1}a_{4})_1& (B^{-1}a_{5})_1\\
  0 & 1&0 & （B^{-1}a_{4})_2& (B^{-1}a_{5})_2\\
  0 & 0&1 & （B^{-1}a_{4})_3& (B^{-1}a_{5})_3
  \end{bmatrix}$$
假设离基变量为$x_{2}$, 入基变量为$x_{4}$, 则有
 
$$
\begin{bmatrix} 
  1 & （B^{-1}a_{4})_1&0 & 0& (B^{-1}a_{5})_1\\
  0 & （B^{-1}a_{4})_2&0 &1 & (B^{-1}a_{5})_2\\
  0 & （B^{-1}a_{4})_3&1 & 0& (B^{-1}a_{5})_3
  \end{bmatrix}\begin{bmatrix} 
  x_1 \\ x_4\\x_3 \\ x_2\\ x_5
  \end{bmatrix}=\begin{bmatrix} 
  (B^{-1}b)_1 \\ (B^{-1}b)_2\\ (B^{-1}b)_3 
  \end{bmatrix}
$$





设$(B^{-1}a_4)_2 \neq 0$，对原方程组的增广矩阵进行高斯消元：

1. **初始增广矩阵**：  
$$
\left[\begin{array}{ccccc|c}
1 & (B^{-1}a_4)_1 & 0 & 0 & (B^{-1}a_5)_1 & (B^{-1}b)_1 \\
0 & (B^{-1}a_4)_2 & 0 & 1 & (B^{-1}a_5)_2 & (B^{-1}b)_2 \\
0 & (B^{-1}a_4)_3 & 1 & 0 & (B^{-1}a_5)_3 & (B^{-1}b)_3
\end{array}\right]
$$

2. **第二列消元**：  
将第二行除以$(B^{-1}a_4)_2$，使第二列主元为$1$，得到：  
$$
\left[\begin{array}{ccccc|c}
1 & (B^{-1}a_4)_1 & 0 & 0 & (B^{-1}a_5)_1 & (B^{-1}b)_1 \\
0 & 1 & 0 & \frac{1}{(B^{-1}a_4)_2} & \frac{(B^{-1}a_5)_2}{(B^{-1}a_4)_2} & \frac{(B^{-1}b)_2}{(B^{-1}a_4)_2} \\
0 & (B^{-1}a_4)_3 & 1 & 0 & (B^{-1}a_5)_3 & (B^{-1}b)_3
\end{array}\right]
$$

3. **消除其他行第二列元素**：  
用第一行减去第二行乘以$(B^{-1}a_4)_1$，第三行减去第二行乘以$(B^{-1}a_4)_3$，最终增广矩阵为：  
$$
\boxed{
\left[\begin{array}{ccccc|c}
1 & 0 & 0 & -\frac{(B^{-1}a_4)_1}{(B^{-1}a_4)_2} & (B^{-1}a_5)_1 - \frac{(B^{-1}a_4)_1(B^{-1}a_5)_2}{(B^{-1}a_4)_2} & (B^{-1}b)_1 - \frac{(B^{-1}a_4)_1(B^{-1}b)_2}{(B^{-1}a_4)_2} \\
0 & 1 & 0 & \frac{1}{(B^{-1}a_4)_2} & \frac{(B^{-1}a_5)_2}{(B^{-1}a_4)_2} & \frac{(B^{-1}b)_2}{(B^{-1}a_4)_2} \\
0 & 0 & 1 & -\frac{(B^{-1}a_4)_3}{(B^{-1}a_4)_2} & (B^{-1}a_5)_3 - \frac{(B^{-1}a_4)_3(B^{-1}a_5)_2}{(B^{-1}a_4)_2} & (B^{-1}b)_3 - \frac{(B^{-1}a_4)_3(B^{-1}b)_2}{(B^{-1}a_4)_2}
\end{array}\right]
}
$$

由于$x_1,x_4,x_3$是新的基变量，那么$x_1,x_4,x_3\geq 0$, 由于$x_2,x_5$是非基变量, 那么$x_2,x_5=0$, 所以
$$
x_1=(B^{-1}b)_1 - \frac{(B^{-1}a_4)_1(B^{-1}b)_2}{(B^{-1}a_4)_2}\\
x_4=\frac{(B^{-1}b)_2}{(B^{-1}a_4)_2}\\
x_3=(B^{-1}b)_3 - \frac{(B^{-1}a_4)_3(B^{-1}b)_2}{(B^{-1}a_4)_2}\\
x_2,x_5=0
$$
新的目标函数值为
$$
z'=c'x = \begin{bmatrix} c_B' & c_N' \end{bmatrix}\begin{bmatrix} x_B' \\ 0 \end{bmatrix} = c_{B1}x_1+c_{B3}x_3+c_{N1}x_4\\
=c_B^T(B^{-1}b-\frac{(B^{-1}b)_2}{(B^{-1}a_4)_2}B^{-1}a_4)+c_N^Tx_N\\
=c_B^TB^{-1}b-c_B^T
\begin{bmatrix}
B^{-1}a_{4}& B^{-1}a_{5}\end{bmatrix}\begin{bmatrix}
x_4 \\0\end{bmatrix}+c_N^Tx_N\\
=c_B^TB^{-1}b-c_B^TB^{-1}Nx_N+c_N^Tx_N=c_B^TB^{-1}b+(c_N^T-c_B^TB^{-1}N)x_N
$$

所以
- 要使$z'> z$， 则需要$c_N^T-c_B^TB^{-1}N>0$，$c_N^T-c_B^TB^{-1}N$越大，那么增加的值就越多.
- $\frac{(B^{-1}b)_2}{(B^{-1}a_4)_2}$越小，$c_N^T-c_B^TB^{-1}N$也越大.

## **3.单纯形法算法步骤**

单纯形法算法的步骤可归纳如下：

1. 把线性规划问题的约束方程组表达成典范型方程组，找出基本可行解作为初始基本可行解. 
2. 若基本可行解不存在，即约束条件有矛盾，则问题无解. 
3. 若基本可行解存在，从初始基本可行解作为起点，根据最优性条件和可行性条件，引入非基变量取代某一基变量，找出目标函数值更优的另一基本可行解. 
4. 按步骤3进行迭代，直到对应检验数满足最优性条件（这时目标函数值不能再改善），即得到问题的最优解. 
5. 若迭代过程中发现问题的目标函数值无界，则终止迭代. 



**检验数与最优性条件**

- **检验数向量**：  
  $$
  \boldsymbol{\sigma}_N = \mathbf{c}_N - \mathbf{N}^T (\mathbf{B}^{-1})^T \mathbf{c}_B
  $$
  若所有 $\boldsymbol{\sigma}_N \leq \mathbf{0}$（最大化问题），则当前解为最优解. 


**入基与离基变量选择**

- **入基变量**：选择检验数最大的非基变量 $x_j$（对应 $\boldsymbol{\sigma}_j > 0$. 
- **离基变量**：通过最小比值法确定：  
  $$
  \theta = \min \left\{ \frac{(\mathbf{B}^{-1} \mathbf{b})_i}{(\mathbf{B}^{-1} \mathbf{a}_j)_i} \mid (\mathbf{B}^{-1} \mathbf{a}_j)_i > 0 \right\}
  $$
  其中 $\mathbf{a}_j$ 是入基变量对应的列向量. 


### **4. 对偶性**

检验数向量 $\mathbf{\sigma} = \begin{pmatrix}\mathbf{\sigma}_B \\ \mathbf{\sigma}_N\end{pmatrix}=\begin{pmatrix}0 \\ \mathbf{c}_N - \mathbf{N}^T (\mathbf{B}^{-1})^T \mathbf{c}_B\end{pmatrix}$ ，其中基变量的检验数 $\sigma_B = 0$ . 

根据对偶理论，原问题和对偶问题达到最优时满足强对偶性，且存在互补松弛性. 从对偶问题的约束 $A^T y \geq c$ 来看，在最优解处，将 $A = \begin{pmatrix}B & N\end{pmatrix}$ ， $c = \begin{pmatrix}C_B \\ C_N\end{pmatrix}$ 代入可得 $\begin{pmatrix}B^T \\ N^T\end{pmatrix}y \geq \begin{pmatrix}C_B \\ C_N\end{pmatrix}$ ，即 $\mathbf{B}^T \mathbf{y} \geq \mathbf{c}_B$ 且 $\mathbf{N}^T \mathbf{y}\geq \mathbf{c}_N$ .

在原问题最优解时，由基变量检验数 $\sigma_B = \mathbf{c}_B - \mathbf{B}^T y = 0$ （因为基变量检验数为$0$ ），通过移项可以解出对偶问题的最优解 $y = (\mathbf{B}^{-1})^T \mathbf{c}_B$ 

从对偶问题的最优解看原问题的最优性条件：$\mathbf{c}_N - \mathbf{N}^T (\mathbf{B}^{-1})^T \mathbf{c}_B=\mathbf{c}_N - \mathbf{N}^T \mathbf{y}$，因此只有当$\mathbf{\sigma}_N\leq 0$时, 才能使$\mathbf{N}^T \mathbf{y}\geq \mathbf{c}_N$成立. 

