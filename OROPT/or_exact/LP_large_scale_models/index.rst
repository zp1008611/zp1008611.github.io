行生成和列生成在大规模线性规划中的使用
======================================

Reference
---------

-  https://dabeenl.github.io/IE631_lecture21_note.pdf

1 大规模线性规划模型
--------------------

| 考虑一个线性规划问题及其对偶问题，形式如下：
| 原问题：
| 

  .. math::


     \begin{align*}
     p^* = \min &\quad c^\top x \\
     \text{s.t.} &\quad Ax \geq b \\
     & \quad x \geq 0
     \end{align*}
| 对偶问题：
| 

  .. math::


     \begin{align*}
     d^* = \max &\quad b^\top \lambda \\
     \text{s.t.} &\quad A^\top \lambda \leq c \\
     & \quad \lambda \geq 0
     \end{align*}
| 其中 $ A $ 是 $ m :raw-latex:`\times `d $
  矩阵。根据应用场景，我们可能需要处理\ **极大规模**\ 的线性规划问题，具体包括：
| - 原问题存在大量约束（即对偶变量数量 $ m $ 大）；
| - 原问题存在大量变量（即对偶约束数量 $ d $ 大）。
| 我们考虑 $ m $ 或 $ d $ 很大（但不同时很大）的情形。本节中，假设 $
  p^\* $ 有限，根据强对偶性，此时 $ d^\* $ 也有限。

3 大 $ m $：原问题行生成
------------------------

| 当 $ m $ 很大时，约束条件数量庞大。此时，无需用全部 $ m $
  个约束求解，而是从一个约束子集开始，后续添加必要约束并迭代求解更新后的问题。具体考虑以下\ **主问题**\ ：
| 

  .. math::


     \begin{align*}
     p_M = \min &\quad c^\top x \\
     \text{s.t.} &\quad a_i^\top x \geq b_i,\ i \in M \\
     & \quad x \geq 0
     \end{align*}
| 其中 $ M $ 是 $ [m] $ 的子集。基本流程如下：
| 1. 求解主问题，得到最优解 $ x_M $；
| 2. 检查是否存在 $ i :raw-latex:`\in [m] `:raw-latex:`\setminus `M
  $，使得 $ x_M $ 违反约束 $ a_i^:raw-latex:`\top `x
  :raw-latex:`\geq `b_i $；
| 3. 若存在 $ i :raw-latex:`\in [m] `:raw-latex:`\setminus `M $ 满足 $
  a_i^:raw-latex:`\top `x_M < b_i $，则将该约束加入主问题；
| 4. 重复上述过程。

这一过程称为
**（原问题）行生成**\ ，也被称作\ **约束生成**\ 或\ **割平面法**\ 。以下是更详细的伪代码。

| **算法1 行生成框架** 1. 初始化 $ M
  :raw-latex:`\subseteq [m] `$，确保主问题存在有限最优解。
| 2. 设 $ S = -:raw-latex:`\infty `$。
| 3. 当 $ S < 0 $ 时，循环执行：
| - 求解主问题：
| 

  .. math::


         \begin{align*}
         p_M = \min & \quad c^\top x \\
         \text{s.t.} & \quad a_i^\top x \geq b_i, \quad i \in M \\
         & \quad x \geq 0
         \end{align*}
         
| 得到主问题的最优解 $ x_M $。
| - 求解子问题：
| 

  .. math::  S = \min_{i \in [m]} \{ a_i^\top x_M - b_i \} 
| - 更新 $ M :raw-latex:`\leftarrow `M :raw-latex:`\cup `{i^\ *} $，其中
  $ i^* :raw-latex:`\in `:raw-latex:`\operatorname{argmin}`\_{i
  :raw-latex:`\in [m]`} {a_i^:raw-latex:`\top `x_M - b_i} $。
| 4. 循环结束后，返回 $ x_M $ 作为原始线性规划的最优解。

4 大 $ d $：对偶问题的行生成 = 原问题的列生成
---------------------------------------------

| 当 $ d $
  很大时，线性规划含大量变量，此时其对偶问题含大量约束。我们可将行生成框架应用于对偶线性规划。回顾对偶线性规划为：
| 

  .. math::


     \begin{align*}
     d^* = \max & \quad b^\top \lambda \\
     \text{s.t.} & \quad \tilde{a}_j^\top \lambda \leq c_j, \quad j \in [d] \\
     & \quad \lambda \geq 0
     \end{align*}
| 其中 $ :raw-latex:`\tilde{a}`\_1, :raw-latex:`\ldots`,
  :raw-latex:`\tilde{a}`\_d $ 是约束矩阵 $ A $
  的列。为将行生成框架应用于对偶问题，从子集 $ D
  :raw-latex:`\subseteq [d] `$ 开始，考虑对应的主对偶问题：
| 

  .. math::


     \begin{align*}
     d^D = \max & \quad b^\top \lambda \\
     \text{s.t.} & \quad \tilde{a}_j^\top \lambda \leq c_j, \quad j \in D \\
     & \quad \lambda \geq 0
     \end{align*}
| 取主对偶问题的对偶，得到：
| 

  .. math::


     \begin{align*}
     p^D = \min & \quad \sum_{j \in D} c_j x_j \\
     \text{s.t.} & \quad \sum_{j \in D} \tilde{a}_j x_j \geq b_i \\
     & \quad x_j \geq 0, \quad j \in D
     \end{align*}

| 注意，原线性规划可写为
| 

  .. math::


     \begin{align*}
     p^* = \min & \sum_{j \in D} c_j x_j + \sum_{j \in [d] \setminus D} c_j x_j \\
     \text{s.t.} & \sum_{j \in D} \tilde{a}_j x_j + \sum_{j \in [d] \setminus D} \tilde{a}_j x_j \geq b_i \\
     & x_j \geq 0,\ j \in D \\
     & x_j \geq 0,\ j \in [d] \setminus D.
     \end{align*}
| 此处，主对偶问题的对偶等价于在原线性规划中令 $ j :raw-latex:`\notin `D
  $ 的 $ x_j = 0 $
  后得到的问题。因此，向对偶主问题添加一行，等价于向原问题添加一个变量:raw-latex:`\列`。于是，这种对偶中的行生成过程被称为
  **列生成**\ 。

| **算法 2 列生成框架**
| 1. 初始化 $ D
  :raw-latex:`\subseteq [d] `$，使对偶主问题存在有限最优解。
| 2. 设 $ S = +:raw-latex:`\infty `$。
| 3. 当 $ S > 0 $ 时，循环执行：
| - 求解对偶主问题：
| 

  .. math::


         \begin{align*}
         d^D = \max & \ b^\top \lambda \\
         \text{s.t.} & \ \tilde{a}_j^\top \lambda \leq c_j,\ j \in D \\
         & \ \lambda \geq 0.
         \end{align*}
         
| 得到对偶主问题的最优解 $ :raw-latex:`\lambda`^D $。
| - 求解子问题：
| 

  .. math::  S = \max_{j \in [d]} \{\tilde{a}_j^\top \lambda^D - c_j\} 
| - 更新 $ D :raw-latex:`\leftarrow `D :raw-latex:`\cup `{j^\ *} $，其中
  $ j^* :raw-latex:`\in `:raw-latex:`\operatorname{argmax}`\_{j
  :raw-latex:`\in [d]`}
  {:raw-latex:`\tilde{a}`\_j\ :sup:`:raw-latex:`\top `:raw-latex:`\lambda``\ D
  - c_j} $。
| 4. 循环结束后，利用 $ j :raw-latex:`\in `D $ 对应的列 $
  :raw-latex:`\tilde{a}`\_j $ 求解原线性规划，并返回最优解。

列生成框架将求解对偶线性规划。因此，在算法终止时，我们会得到一个子集 $ D
:raw-latex:`\subseteq [d] `$，使得 $ d^D = d^\*
:math:`。根据强对偶性，有：`\ $ p^D = d^D = d^\* = p^\*. $$
