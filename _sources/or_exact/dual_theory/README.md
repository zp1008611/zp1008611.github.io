# 对偶理论



## 1 预备知识
$ n \times n $ 对称矩阵的集合记为 $ \mathbb{S}^n $，$ n \times n $ 对称半正定（正定）矩阵的集合记为 $ \mathbb{S}^n_+ (\mathbb{S}^{n}_{++}) $. 符号 $ X \succeq 0 \ (X \succ 0) $ 表示矩阵 $ X \in \mathbb{S}^n $ 是半正定（正定）的. 符号 $ X \geq 0 \ (X > 0) $ 表示矩阵 $ X $ 的每个元素都是非负的（正的）. $ X $ 的迹，即 $ X $ 对角元素之和，记为 $ \mathrm{Tr}(X) $. 两个矩阵 $ A \in \mathbb{R}^{m \times n} $ 和 $ B \in \mathbb{R}^{m \times n} $ 的内积定义为 $ \langle A, B \rangle := \sum_{j=1}^m \sum_{k=1}^n A_{jk}B_{jk} = \mathrm{Tr}(A^\top B) $. 矩阵 $ A \in \mathbb{R}^{m \times n} $ 的弗罗贝尼乌斯范数定义为 $ \|A\|_F := \sqrt{\sum_{i=1}^m \sum_{j=1}^n A_{ij}^2} $. 

## 2 弱对偶性
### 2.1 拉格朗日对偶问题
在本节中，我们考虑一个可能非凸的优化问题：  
$$
p^* := \min_{x} f_0(x) \ \text{s.t.} \ f_i(x) \leq 0, \ i = 1, \dots, m \tag{2.1}
$$ 
我们用 $ \mathcal{D} $ 表示问题的定义域（即所有涉及函数定义域的交集），用 $ \mathcal{X} \subseteq \mathcal{D} $ 表示其可行集.   

我们将上述问题称为原问题，原问题中的决策变量为 $ x $. 引入拉格朗日对偶性的一个目的是为极小化问题寻找下界（或为极大化问题寻找上界）. 之后，我们将使用对偶性工具推导凸问题的最优性条件.   

### 2.2 对偶问题  
**拉格朗日函数**：我们为该问题关联一个拉格朗日函数 $ \mathcal{L}: \mathbb{R}^n \times \mathbb{R}^m \to \mathbb{R} $，其定义为：  
$$
\mathcal{L}(x, \lambda) := f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) \tag{2.2}
$$
变量 $ \lambda \in \mathbb{R}^m $ 称为拉格朗日乘子.   

我们注意到，对于每个可行的 $ x \in \mathcal{X} $，以及每个 $ \lambda \geq 0 $，$ f_0(x) $ 有下界 $ \mathcal{L}(x, \lambda) $：  
$$
\forall x \in \mathcal{X}, \forall \lambda \in \mathbb{R}_+^m : f_0(x) \geq \mathcal{L}(x, \lambda).
$$  
拉格朗日函数可用于将原问题（??）表示为无约束问题. 确切地说：  
$$
p^* = \min_x \max_{\lambda \geq 0} \mathcal{L}(x, \lambda),
$$  
这里我们利用了以下事实：对于任意向量 $ f \in \mathbb{R}^m $，有  
$$
\max_{\lambda \geq 0} \lambda^\top f = 
\begin{cases} 
0 & \text{若 } f \leq 0 \\
+\infty & \text{否则}
\end{cases}
$$ 
**拉格朗日对偶函数**. 然后我们定义拉格朗日对偶函数（简称对偶函数）为函数  
$$
g(\lambda) := \min_x \mathcal{L}(x, \lambda).
$$  
根据上述边界（??），通过对右边的 $ x $ 求极小，我们得到  
$$
\forall x \in \mathcal{X}, \forall \lambda \geq 0 : f_0(x) \geq \min_{x'} \mathcal{L}(x', \lambda) = g(\lambda),
$$ 
对左边的 $ x $ 求极小后，得到下界  
$$
\forall \lambda \in \mathbb{R}_+^m : p^* \geq g(\lambda).
$$ 
**拉格朗日对偶问题**. 利用上述边界，我们能得到的最佳下界是 $ p^* \geq d^* $，其中  
$$
d^* = \max_{\lambda \geq 0} g(\lambda).
$$  
我们将上述问题称为对偶问题，向量 $ \lambda \in \mathbb{R}^m $ 称为对偶变量.   

**定理 2.1（极小极大不等式）**：对任意关于向量变量 $ x, y $ 的函数 $ \phi $，以及任意子集 $ \mathcal{X}, \mathcal{Y} $，有  
$$
\max_{y \in \mathcal{Y}} \min_{x \in \mathcal{X}} \phi(x, y) \leq \min_{x \in \mathcal{X}} \max_{y \in \mathcal{Y}} \phi(x, y).
$$

**定理 2.2.** 对于一般的（可能非凸的）问题（??），弱对偶性成立：$ p^* \geq d^* $.   

**含等式约束的情形**. 如果问题中存在等式约束，我们可以将其表示为两个不等式约束. 结果表明，这会得到相同的对偶问题，就好像我们直接为每个等式约束使用一个对偶变量，且该对偶变量符号不受限制. 为了说明这一点，考虑问题  
$$
\begin{aligned}
p^* := \min_x & \ f_0(x) \\
\text{s.t.} & \ f_i(x) \leq 0, \, i = 1, \dots, m, \\
& \ h_i(x) = 0, \, i = 1, \dots, p.
\end{aligned}
$$


我们将该问题写为  
$$
\begin{aligned}
p^* := \min_{x} & \ f_0(x) \\
\text{s.t.} & \ f_i(x) \leq 0, \, i = 1, \dots, m, \\
& \ h_i(x) \leq 0, \ -h_i(x) \leq 0, \, i = 1, \dots, p.
\end{aligned}
$$  
对约束 $ \pm h_i(x) \leq 0 $ 使用乘子 $ \nu_i^\pm $，我们将相关的拉格朗日函数写为  
$$
\begin{aligned}
\mathcal{L}(x, \lambda, \nu^+, \nu^-) 
&= f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{i=1}^p h_i(x) + \sum_{i=1}^p \nu_i^- (-h_i(x)) \\
&= f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{i=1}^p \nu_i h_i(x),
\end{aligned}
$$  
其中 $ \nu := \nu^+ - \nu^- $ 没有任何符号约束.因此，原问题中的不等式约束对应于相应乘子的符号约束，而等式约束的乘子没有显式约束.  

## 3 强对偶性  
### 3.1 原问题与对偶问题  
在本节中，我们考虑一个凸优化问题  
$$
\begin{aligned}
p^* := \min_{x} & \ f_0(x) \\
\text{s.t.} & \ f_i(x) \leq 0, \, i = 1, \dots, m, \\
& \ h_i(x) = 0, \, i = 1, \dots, p,
\end{aligned}\tag{3.1}
$$  
其中函数 $ f_0, f_1, \dots, f_m $ 是凸的，且 $ h_1, \dots, h_p $ 是仿射的.我们用 $ \mathcal{D} $ 表示问题的定义域（即所有涉及函数定义域的交集），用 $ \mathcal{X} \subseteq \mathcal{D} $ 表示其可行集.  

我们为该问题关联一个拉格朗日函数 $ \mathcal{L}: \mathbb{R}^n \times \mathbb{R}^m \times \mathbb{R}^p \to \mathbb{R} $，其定义为：  
$$
\mathcal{L}(x, \lambda, \nu) := f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{i=1}^p \nu_i h_i(x).
$$  
对偶函数是 $ g: \mathbb{R}^m \times \mathbb{R}^p \to \mathbb{R} $，定义为：  
$$
g(\lambda, \nu) := \min_{x} \mathcal{L}(x, \lambda, \nu).
$$  
相关的对偶问题是  
$$
d^* = \max_{\lambda \geq 0, \nu} g(\lambda, \nu).
$$


## 3.2 通过斯莱特条件的强对偶性  
**对偶间隙与强对偶性**：我们已了解弱对偶性如何构建一个凸优化问题，即便原（主）问题非凸，该问题也能为原问题提供下界.对偶间隙是一个非负数 $ p^* - d^* $.  
若对偶间隙为零（即 $ p^* = d^* $），则称问题（??）满足强对偶性.  

**斯莱特条件**：若问题严格可行，即  
$$
\exists x_0 \in \mathcal{D} : f_i(x_0) < 0,\, i = 1, \dots, m,\ h_i(x_0) = 0,\, i = 1, \dots, p,
$$  
则称其满足斯莱特条件.当 $ f_i $ 为仿射函数时，无需严格可行性，可用斯莱特条件的弱形式替代.由此可得：  

**定理 3.1（通过斯莱特条件的强对偶性）**：若原问题（??）为凸问题，且满足弱斯莱特条件，则强对偶性成立，即 $ p^* = d^* $.  

