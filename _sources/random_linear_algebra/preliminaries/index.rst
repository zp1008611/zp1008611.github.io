前言
====

Reference
---------

-  Randomized Numerical Linear Algebra: Foundations & Algorithms

随机算法概述
------------

1. **经典NLA问题**\ ：传统NLA处理密集/稀疏线性系统求解、正交化、特征值计算、奇异值分解等核心问题，但现代计算架构（如GPU、分布式系统）对算法提出新挑战.
2. **随机算法的兴起**\ ：概率算法自Ulam和von
   Neumann的蒙特卡洛方法起，在科学计算中占据重要地位.
   20世纪80年代后，随机算法逐步融入NLA，从早期频谱计算、矩阵迹估计，到20世纪90年代理论计算机科学拓展其应用，再到2000年后数值分析领域提出实用低秩近似算法，最终在2019年成为NLA主流.
3. **随机性的价值**\ ：随机算法可更高效处理特定NLA问题，如快速求解大规模最小二乘问题（如SPARSECHOLESKY算法）、实现单遍数据低秩SVD近似，还能优化矩阵计算结构，适配现代硬件加速计算.
4. **算法设计考量**\ ：需根据数据交互方式设计算法，涵盖流数据计算、内存密集矩阵处理、稀疏矩阵技术、昂贵矩阵评估场景等，随机化提供了重组算法、控制计算资源的途径.

线性代数基础
------------

1. **基础符号与定义**

   -  **符号规范**\ ：明确实数域（\ :math:`\mathbb{R}`\ ）、复数域（\ :math:`\mathbb{C}`\ ）表示，规定向量（小写粗体/希腊字母）、矩阵（大写字母）、零矩阵（\ **0**\ ）、单位矩阵（\ **I**\ ）的符号，以及矩阵索引（如
      **A**\ (i, j)）、共轭转置（$ ^\* :math:`）和自伴矩阵（`
      :raw-latex:`\mathbf{A}` = :raw-latex:`\mathbf{A}`^\* $）的定义.
   -  **伪逆矩阵**\ ：定义Moore–Penrose伪逆矩阵 $
      :raw-latex:`\mathbf{A}`^:raw-latex:`\dagger `$，满足 $
      :raw-latex:`\mathbf{A}`:raw-latex:`\mathbf{A}`^:raw-latex:`\dagger `$
      与 $
      :raw-latex:`\mathbf{A}`^:raw-latex:`\dagger`:raw-latex:`\mathbf{A}`
      $ 自伴、$
      :raw-latex:`\mathbf{A}`:raw-latex:`\mathbf{A}`^:raw-latex:`\dagger`:raw-latex:`\mathbf{A}`
      = :raw-latex:`\mathbf{A}` $ 等条件，列满秩时 $
      :raw-latex:`\mathbf{A}`^:raw-latex:`\dagger `=
      (:raw-latex:`\mathbf{A}`^\ *:raw-latex:`\mathbf{A}`)\ {-1}:raw-latex:`\mathbf{A}`*
      $.

2. **特征值与奇异值**

   -  定义半正定矩阵（PSD）、正定矩阵（PD）及半正定序（$
      :raw-latex:`\mathbf{A}`
      :raw-latex:`\preccurlyeq `:raw-latex:`\mathbf{B}` $）.
   -  规范自伴矩阵特征值（$ :raw-latex:`\lambda`\_1
      :raw-latex:`\geq `:raw-latex:`\lambda`\_2
      :raw-latex:`\geq `:raw-latex:`\dots `\ :math:`）和矩阵奇异值（`
      :raw-latex:`\sigma`\_1 :raw-latex:`\geq `:raw-latex:`\sigma`\ *2
      :raw-latex:`\geq `:raw-latex:`\dots `$）的表示，引入谱函数 $
      f(:raw-latex:`\mathbf{A}`) = :raw-latex:`\sum`*\ {i=1}^n
      f(:raw-latex:`\lambda`\_i):raw-latex:`\mathbf{u}`\_i:raw-latex:`\mathbf{u}`\_i^\*
      $.

3. **内积与范数**

   -  **向量空间**\ ：定义向量标准内积 $
      :raw-latex:`\langle `:raw-latex:`\mathbf{a}`,
      :raw-latex:`\mathbf{b}` :raw-latex:`\rangle `$、ℓ₂范数 $
      \|:raw-latex:`\mathbf{a}`\| $，单位范数向量集 $
      :raw-latex:`\mathbb{S}`^{n-1} $.
   -  **矩阵运算**\ ：包括矩阵迹 $
      :raw-latex:`\text{trace}`(:raw-latex:`\mathbf{A}`) $、迹内积 $
      :raw-latex:`\langle `:raw-latex:`\mathbf{A}`,
      :raw-latex:`\mathbf{B}` :raw-latex:`\rangle `=
      :raw-latex:`\text{trace}`(:raw-latex:`\mathbf{A}`^\*:raw-latex:`\mathbf{B}`)
      $、Frobenius范数 $ \|:raw-latex:`\mathbf{A}`\|_F
      :math:`，以及正交矩阵（`
      :raw-latex:`\mathbf{U}`^\*:raw-latex:`\mathbf{U}` =
      :raw-latex:`\mathbf{I}` $）.
   -  **矩阵范数**\ ：介绍谱范数（$ \|:raw-latex:`\cdot`\|
      :math:`，最大奇异值）、核范数（` \|:raw-latex:`\cdot`\|\_\*
      :math:`，奇异值之和）、Frobenius范数（` \|:raw-latex:`\cdot`\|_F
      $），并统一于Schatten $ p $-范数（如核范数为Schatten 1-范数）.

4. **近似与特殊概念**

   -  **谱范数近似**\ ：若 $ \|:raw-latex:`\mathbf{A}` -
      :raw-latex:`\tilde{\mathbf{A}}`\|
      :raw-latex:`\leq `:raw-latex:`\varepsilon `$，可推导线性泛函、奇异值的误差边界，讨论Frobenius范数近似在随机NLA中的实用性.
   -  **内在维数与稳定秩**\ ：对半正定矩阵 $ :raw-latex:`\mathbf{A}`
      $，定义内在维数 $
      :raw-latex:`\text{intdim}`(:raw-latex:`\mathbf{A}`) =
      :raw-latex:`\frac{\text{trace}(\mathbf{A})}{\|\mathbf{A}\|}`
      $；对矩阵 $ :raw-latex:`\mathbf{B}` $，稳定秩 $
      :raw-latex:`\text{srank}`(:raw-latex:`\mathbf{B}`) =
      :raw-latex:`\frac{\|\mathbf{B}\|_F^2}{\|\mathbf{B}\|^2}`
      $，作为秩的连续度量.
   -  **Schur补**\ ：基于部分高斯消元，定义PSD矩阵 $
      :raw-latex:`\mathbf{A}`(X) $ 及Schur补 $ :raw-latex:`\mathbf{A}`/X
      = :raw-latex:`\mathbf{A}` - :raw-latex:`\mathbf{A}`(X)
      $，在随机NLA中起关键作用.

5. **其他约定**

   -  采用计算机科学标准大O符号（如 $ O(n^3) $）描述算法复杂度.
   -  使用类MATLAB语法简化算法描述，如奇异值分解表示为
      :math:`[\mathbf{U}, \mathbf{\Sigma}, \mathbf{V}] = \text{svd}(\mathbf{A})`.

概率与高维概率基础
------------------

1. **基础概念**

   -  定义概率空间，涵盖标量、向量、矩阵形式的单值随机变量，规范符号：标量随机变量用斜体字母（如
      $ X,Y,Z $），向量用粗体（如 $ :raw-latex:`\mathbf{x,y}` $）.
   -  明确期望（$ :raw-latex:`\mathbb{E}`[:raw-latex:`\cdot`]
      :math:`）、方差（` :raw-latex:`\text{Var}`[:raw-latex:`\cdot`]
      $）运算规则，强调期望的线性性质（如 $
      :raw-latex:`\mathbb{E}`[:raw-latex:`\mathbf{A}`X] =
      :raw-latex:`\mathbf{A}`:raw-latex:`\mathbb{E}`[X] :math:`，`
      :raw-latex:`\mathbf{A}` $ 确定，$ X $ 随机）.
   -  定义随机变量“中心化”（期望为零）、向量“各向同性”（$
      :raw-latex:`\mathbb{E}`[:raw-latex:`\mathbf{xx}`^\*] =
      :raw-latex:`\mathbf{I}`
      $）、“标准化”（期望零且方差一），以及“统计独立同分布（i.i.d.）”.

2. **分布类型**

   -  **均匀分布（UNIF）**\ ：有限集上的均匀分布，如拉德马赫分布（$
      :raw-latex:`\text{UNIF}`{:raw-latex:`\pm 1`}
      $），对应随机向量各坐标独立分布.
   -  **正态分布（NORMAL）**\ ：表示为 $
      :raw-latex:`\text{NORMAL}`(:raw-latex:`\boldsymbol{\mu}`,
      :raw-latex:`\mathbf{C}`) :math:`，` :raw-latex:`\boldsymbol{\mu}`
      $ 为期望，$ :raw-latex:`\mathbf{C}` $
      为半正定协方差矩阵，标准正态分布期望为零，协方差为单位矩阵.

3. | **集中不等式**
   | 用于界定随机变量偏离期望的概率边界，标量情形参考Boucheron等文献，矩阵场景下以谱范数衡量偏离，是随机数值线性代数的重要工具，相关内容见Tropp的研究.

4. | **高斯随机矩阵**
   | 利用元素独立的高斯随机矩阵分析矩阵性质，控制最大和最小奇异值.
     经典理论关联Slepian、Chevet、Gordon不等式，近年研究发现Gordon不等式可反向应用，更详细资源参考Muirhead、Bai和Silverstein的研究，核心结论在Halko等人的文献中呈现.
