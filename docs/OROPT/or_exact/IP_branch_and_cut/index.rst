分支切割
========



Reference

---------



-  https://en.wikipedia.org/wiki/Branch_and_cut

-  https://en.wikipedia.org/wiki/Branch_and_price

-  https://or.rwth-aachen.de/files/research/publications/branch-and-price.pdf

-  https://homes.di.unimi.it/righini/Didattica/ComplementiRicercaOperativa/MaterialeCRO/2000%20-%20Mitchell%20-%20branch-and-cut.pdf

-  https://optimization-online.org/wp-content/uploads/2008/06/1997.pdf



在\ `凸包和有效不等式 <..\IP_convex_hull_and_valid_ineq\README.md>`__

的内容里，我们简单介绍了一下分支切割算法，下面给出完整的算法框架形式.



.. _分支切割-1:



分支切割

--------



| 考虑混合整数线性规划

| 



  .. math::





     z^* = \max \{ f(x) : x \in \mathcal{D} \} 

| 其中

| 



  .. math::





     f(x) = c^Tx, c\in\mathbb{R}^n\\

     \mathcal{D} = \{ x \in \mathbb{R}^n_+\mid A x \leq b,\, ,\, x_j \in \mathbb{Z}_+,\, \forall j \in I \}.



| **算法1 分支切割法**

| 1 令 $ :raw-latex:`\mathcal{L}` = :raw-latex:`\mathcal{D}` $，初始化 $

  :raw-latex:`\hat{x}` $

| 2 **while** $ :raw-latex:`\mathcal{L}`

  :raw-latex:`\neq `:raw-latex:`\emptyset `$ **do**

| 3 :math:`\quad` 从 $ :raw-latex:`\mathcal{L}` $ 中选择待探索的子集合 $

  :raw-latex:`\mathcal{S}`$ :math:`\\` 4 :math:`\quad`

  求\ :math:`(\mathcal{S},f)`\ 的线性松弛问题的解\ :math:`\hat{x}'`

  :math:`\\` 5 :math:`\quad` **if** $ :raw-latex:`\hat{x}`’ $是不可行解

  **or** $ :raw-latex:`\hat{x}`’

  :math:`是分数可行解，且`\ f（:raw-latex:`\hat{x}`‘）:raw-latex:`\leq `f(:raw-latex:`\hat{x}`)$

  **then** :math:`\\` 6 :math:`\quad\quad`

  :math:`\mathcal{S}`\ 赋予可以剪枝属性 :math:`\\` 7 :math:`\quad`

  **else if** $ :raw-latex:`\hat{x}`’ :math:`是分数可行解，且`\ f

  （:raw-latex:`\hat{x}`‘）> f(:raw-latex:`\hat{x}`)$ **then**

  :math:`\\` 8 :math:`\quad\quad` :math:`\mathcal{S}`\ 赋予不可剪枝属性

  :math:`\\` 9 :math:`\quad\quad` **if** 需要添加切平面 **then**

  :math:`\\` 10 :math:`\quad\quad\quad` 找到分离 $ :raw-latex:`\hat{x}`’

  $ 与 $ :raw-latex:`\mathcal{S}` $ 的割平面 $

  :raw-latex:`\langle `:raw-latex:`\boldsymbol{a}`,

  :raw-latex:`\hat{x}`’

  :raw-latex:`\rangle `:raw-latex:`\leq `:raw-latex:`\beta `$

| 11 :math:`\quad\quad\quad` $ :raw-latex:`\mathcal{S}`\_{t+1}

  :raw-latex:`\leftarrow `:raw-latex:`\mathcal{S}`\_t

  :raw-latex:`\cap `{ x

  :raw-latex:`\mid `:raw-latex:`\langle `:raw-latex:`\boldsymbol{a}`,

  :raw-latex:`\hat{x}`’

  :raw-latex:`\rangle `:raw-latex:`\leq `:raw-latex:`\beta `} $

  :math:`\\` 11 :math:`\quad\quad\quad` 返回第4行 :math:`\\` 9

  :math:`\quad` **else if** $ :raw-latex:`\hat{x}`’ $是整数可行解

  **then** :math:`\\` 10 :math:`\quad\ \ \ ` $ :raw-latex:`\hat{x}` =

  :raw-latex:`\hat{x}`’ $ :math:`\\` 11 :math:`\quad\ \ \ `

  :math:`\mathcal{S}`\ 赋予可以剪枝属性 :math:`\\` 12 :math:`\ \ \ `

  **end if** :math:`\\` 13 :math:`\ \ \ ` **if**

  :math:`\mathcal{S}`\ 不可剪枝 **then** :math:`\\` 14

  :math:`\quad\ \ \ ` 将 $ :raw-latex:`\mathcal{S}` $ 划分为 $

  :raw-latex:`\mathcal{S}`\_1, :raw-latex:`\mathcal{S}`\_2,

  :raw-latex:`\dots`, :raw-latex:`\mathcal{S}`\_r $

| 15 :math:`\quad\ \ \ ` 将 $ :raw-latex:`\mathcal{S}`\_1,

  :raw-latex:`\mathcal{S}`\_2, :raw-latex:`\dots`,

  :raw-latex:`\mathcal{S}`\_r $ 加入 $ :raw-latex:`\mathcal{L}` $

  :math:`\\` 16 :math:`\ \ \ ` **end if** :math:`\\` 17 :math:`\ \ \ `

  从 $ :raw-latex:`\mathcal{L}` $ 中移除 $ :raw-latex:`\mathcal{S}` $

| 18 **end while**

| 19 **return** $ :raw-latex:`\hat{x}` $

