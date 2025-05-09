# 一些神经网络训练技巧

## Reference

- https://www.cse.iitm.ac.in/~miteshk/CS7015/Slides/Handout/Lecture9.pdf


## 1：深度神经网络训练快速回顾

我们已经了解了如何训练这个网络：
$$w = w - \eta\nabla w$$
其中：
$$\begin{aligned} \nabla w &= \frac{\partial \mathscr{L}(w)}{\partial w} \\ &= (f(x) - y) \cdot f(x) \cdot (1 - f(x)) \cdot x \end{aligned}$$
对于一个具有更多输入的更宽网络呢？
$$w_{1} = w_{1} - \eta\nabla w_{1}$$
$$w_{2} = w_{2} - \eta\nabla w_{2}$$
$$w_{3} = w_{3} - \eta\nabla w_{3}$$
其中， $\nabla w_{i} = (f(x) - y) \cdot f(x) \cdot (1 - f(x)) \cdot x_{i}$ 
如果我们有一个更深的网络呢？
我们现在可以使用链式法则计算 $\nabla w_{1}$ ：
$$\begin{aligned} \frac{\partial \mathscr{L}(w)}{\partial w_{1}} &= \frac{\partial \mathscr{L}(w)}{\partial y} \cdot \frac{\partial y}{\partial a_{3}} \cdot \frac{\partial a_{3}}{\partial h_{2}} \cdot \frac{\partial h_{2}}{\partial a_{2}} \cdot \frac{\partial a_{2}}{\partial h_{1}} \cdot \frac{\partial h_{1}}{\partial a_{1}} \cdot \frac{\partial a_{1}}{\partial w_{1}} \\ &= \frac{\partial \mathscr{L}(w)}{\partial y} \cdot \cdots \cdot h_{0} \end{aligned}$$
一般来说：
$$\nabla w_{i} = \frac{\partial \mathscr{L}(w)}{\partial y} \cdot \cdots \cdot h_{i - 1}$$
注意， $\nabla w_{i}$ 与相应的输入 $h_{i - 1}$ 成正比（我们稍后会用到这个事实）. 
如果我们有一个既深又宽的网络会发生什么呢？如何计算 $\nabla w_{2}$ ？它将由跨多条路径应用链式法则给出（我们在学习反向传播时详细讨论过）. 
### 需要记住的事情
- 训练神经网络是一场梯度的“游戏”（使用我们讨论过的任何现有的基于梯度的方法）. 
- 梯度告诉我们一个参数对损失的“贡献”. 
- 关于一个参数的梯度与该参数的输入成正比（回想一下 $\nabla w_{i}$ 公式中的“… \*  $x$ ”项或“…  $h_{i}$ ”项）. 
反向传播通过误差反向传播来学习表示，由鲁梅尔哈特（Rumelhart）等人在1986年推广. 然而，当用于真正的深度网络时，它并不是很成功. 事实上，直到2006年，训练非常深的网络都非常困难. 通常，即使经过大量的训练轮次，训练也不会收敛. 
### 模块9.2：无监督预训练
现在发生了什么变化？尽管存在训练大型网络的问题，深度学习是如何变得如此流行的呢？在2006年之前，它并不那么流行. 在2006年辛顿（Hinton）和萨拉胡特迪诺夫（Salakhutdinov）的开创性工作之后，这个领域重新焕发生机. 
1. G. E. Hinton和R. R. Salakhutdinov. Reducing the dimensionality of data with neural networks. Science, 313(5786):504–507, July 2006.
让我们看看这篇论文中引入的无监督预训练的思想……（注意，在这篇论文中，他们在受限玻尔兹曼机（RBMs）的背景下引入了这个思想，但我们将在自编码器的背景下讨论它）. 
考虑图中所示的深度神经网络. 让我们关注网络的前两层（ $x$ 和 $h_{1}$ ）. 我们将首先使用无监督目标来训练这两层之间的权重. 注意，我们试图从隐藏表示（ $h_{1}$ ）重建输入（ $x$ ）. 我们将其称为无监督目标，因为它不涉及输出标签（ $y$ ），只使用输入数据（ $x$ ）. 
在这一步结束时，第1层的权重被训练，使得 $h_{1}$ 捕获输入 $x$ 的抽象表示. 
我们现在固定第1层的权重，并对第2层重复相同的过程. 在这一步结束时，第2层的权重被训练，使得 $h_{2}$ 捕获 $h_{1}$ 的抽象表示. 我们继续这个过程，直到最后一个隐藏层（即输出层之前的层），以便每一层都能捕获前一层的抽象表示. 
在这种逐层预训练之后，我们添加输出层，并使用特定任务的目标来训练整个网络. 注意，实际上我们已经使用贪心无监督目标初始化了网络的权重，现在正在使用有监督目标对这些权重进行微调. 
为什么这样效果更好呢？是因为更好的优化吗？是因为更好的正则化吗？让我们看看这两个问题的含义，并根据一些（众多研究中的）现有研究来尝试回答它们. 
1. The difficulty of training deep architectures and effect of unsupervised pre-training - Erhan etal,2009
2. Exploring Strategies for Training Deep Neural Networks, Larocelle et al,2009
我们试图解决的优化问题是什么？
$$最小化 \mathscr{L}(\theta)=\frac{1}{m} \sum_{i = 1}^{m}(y_{i} - f(x_{i}))^{2}$$
是不是在没有无监督预训练的情况下，我们甚至无法将 $\mathscr{L}(\theta)$ 降低到0（即使对于训练数据）（因此优化效果不佳）？让我们更详细地看看……
深度神经网络的有监督目标的误差表面是高度非凸的，有许多山丘、高原和平原. 鉴于深度神经网络的大容量，仍然很容易陷入这些零误差区域之一. 事实上，拉罗谢尔（Larochelle）等人表明，如果最后一层具有大容量，那么即使没有预训练， $\mathscr{L}(\theta)$ 也会变为0. 然而，如果网络的容量较小，无监督预训练会有帮助. 
正则化的作用是什么？它将权重限制在参数空间的某些区域. 
- L - 1正则化：将大多数权重约束为0. 
- L - 2正则化：防止大多数权重取大值. 
无监督目标：
$$\Omega(\theta)=\frac{1}{m} \sum_{i = 1}^{m} \sum_{j = 1}^{n}(x_{ij} - \hat{x}_{ij})^{2}$$
我们可以将这个无监督目标视为对优化问题的额外约束. 
有监督目标：
$$\mathscr{L}(\theta)=\frac{1}{m} \sum_{i = 1}^{m}(y_{i} - f(x_{i}))^{2}$$
实际上，预训练将权重限制在参数空间的特定区域. 具体来说，它将权重限制在能够很好地捕获数据特征的区域（由无监督目标决定）. 这个无监督目标确保学习不会只关注有监督目标（并且也满足无监督目标）. 
其他一些实验也表明，预训练对随机初始化更具鲁棒性. 一个被接受的假设是，预训练会导致更好的权重初始化（以便各层捕获数据的内部特征）. 
1. The difficulty of training deep architectures and effect of unsupervised pre-training - Erhan et al,2009
那么2006 - 2009年之后发生了什么呢？深度学习不断发展，出现了更好的优化算法、更好的正则化方法、更好的激活函数、更好的权重初始化策略. 
### 模块9.3：更好的激活函数
在研究激活函数之前，让我们试着回答以下问题：“是什么让深度神经网络如此强大？”
考虑这个深度神经网络. 想象一下，如果我们在每一层都用一个简单的线性变换替换sigmoid函数，那么我们将只把 $y$ 学习为 $x$ 的线性变换. 换句话说，我们将被限制在学习线性决策边界，无法学习任意的决策边界. 
特别是，深度线性神经网络无法学习这样的边界，但深度非线性神经网络确实可以学习（回想通用逼近定理）. 
现在让我们看看一些通常在深度神经网络中使用的非线性激活函数（这些材料大多来自安德烈·卡帕西（Andrej Karpathy）的讲义）. 
1. http://cs231n.github.io
sigmoid函数：
$$\sigma(x)=\frac{1}{1 + e^{-x}}$$
显然，sigmoid函数将所有输入压缩到范围[0, 1]. 由于我们总是对梯度感兴趣，让我们求这个函数的梯度：
$$\frac{\partial \sigma(x)}{\partial x}=\sigma(x)(1 - \sigma(x))$$
（你可以很容易地推导出来）让我们看看如果在深度网络中使用sigmoid函数会发生什么. 
在计算 $\nabla w_{2}$ 时，在链式法则的某个点上，我们会遇到：
$$\frac{\partial h_{3}}{\partial a_{3}}=\frac{\partial \sigma(a_{3})}{\partial a_{3}}=\sigma(a_{3})(1 - \sigma(a_{3}))$$
这会有什么后果呢？为了回答这个问题，让我们首先理解饱和神经元的概念. 
当 $\sigma(x)=1$ 或 $\sigma(x)=0$ 时，sigmoid神经元被称为饱和. 饱和时的梯度是多少呢？从图中或我们推导的公式中可以看出，它将为0. 饱和神经元会导致梯度消失. 
但是神经元为什么会饱和呢？考虑一下，如果我们使用sigmoid神经元并将权重初始化为非常大的值会发生什么？神经元会很快饱和，梯度会消失，训练会停滞（稍后会详细介绍）. 
饱和神经元会导致梯度消失，sigmoid函数不是零中心的. 考虑关于 $w_{1}$ 和 $w_{2}$ 的梯度：
$$\nabla w_{1}=\frac{\partial \mathscr{L}(w)}{\partial y} \frac{\partial y}{h_{3}} \frac{\partial h_{3}}{\partial a_{3}} \frac{\partial a_{3}}{\partial w_{1}} h_{21}$$
$$\nabla w_{2}=\frac{\partial \mathscr{L}(w)}{\partial y} \frac{\partial y}{h_{3}} \frac{\partial h_{3}}{\partial a_{3}} \frac{\partial a_{3}}{\partial w_{2}} h_{22}$$
注意， $h_{21}$ 和 $h_{22}$ 在[0, 1]之间（即它们都是正的）. 所以如果第一个公共项（红色部分）是正的（负的），那么 $\nabla w_{1}$ 和 $\nabla w_{2}$ 都是正的（负的）. 
为什么这是个问题呢？基本上，一层中的所有梯度要么都是正的，要么都是负的. 这限制了可能的更新方向. 
最后，sigmoid函数计算成本很高（因为有 $e^{x}$ ）. 
双曲正切函数（tanh(x)）：将所有输入压缩到范围[-1, 1]，是零中心的. 这个函数的导数是什么呢？
$$\frac{\partial \tanh(x)}{\partial x}=(1 - \tanh^{2}(x))$$
梯度在饱和时仍然会消失，并且计算成本也很高. 
修正线性单元（ReLU）：
$$f(x)=\max(0, x)$$
它是一个非线性函数吗？确实是！实际上，我们可以组合两个ReLU单元来恢复sigmoid函数的分段线性近似. 
ReLU的优点：在正区域不会饱和，计算效率高，在实践中收敛速度比sigmoid/tanh快得多. 
1. ImageNet Classification with Deep Convolutional Neural Networks - Alex Krizhevsky Ilya Sutskever, Geoffrey E. Hinton, 2012
在实践中有一个注意事项. 让我们看看ReLU(x)的导数是多少：
$$\begin{aligned} \frac{\partial ReLU(x)}{\partial x} &= 0 & 如果x < 0 \\ &= 1 & 如果x > 0 \end{aligned}$$
现在考虑给定的网络. 如果在某个点上，一个大的梯度导致偏置 $b$ 更新为一个很大的负值会发生什么呢？
神经元将输出0（死亡神经元）. 不仅输出会为0，而且在反向传播过程中，甚至 $\frac{\partial h_{1}}{\partial a_{1}}$ 也会为零. 权重 $w_{1}$ 、 $w_{2}$ 和 $b$ 将不会被更新（因为在链式法则中会有一个零项）. 
在实践中，如果学习率设置得太高，很大一部分ReLU单元可能会死亡. 建议将偏置初始化为正值（0.01），并使用ReLU的其他变体（我们很快会看到）. 
泄漏修正线性单元（Leaky ReLU）：
$$f(x)=\max(0.01x, x)$$
不会饱和，不会死亡（ $0.01x$ 确保至少有一个小的梯度会流过），计算效率高，输出接近零中心. 
参数化修正线性单元（Parametric ReLU）：
$$f(x)=\max(\alpha x, x)$$
 $\alpha$ 是模型的一个参数， $\alpha$ 将在反向传播过程中更新. 
指数线性单元（Exponential Linear Unit）：具有ReLU的所有优点， $ae^{x}-1$ 确保至少有一个小的梯度会流过，输出接近零中心，计算成本高（需要计算 $e^{x}$ ）. 
$$ \begin{aligned} f(x) &= x & 如果x > 0 \\ &= ae^{x}-1 & 如果x \leq 0 \end{aligned} $$
Maxout神经元：
$$\max(w_{1}^{T}x + b_{1}, w_{2}^{T}x + b_{2})$$
推广了ReLU和Leaky ReLU，不会饱和！不会死亡！参数数量翻倍. 
### 需要记住的事情
- sigmoid函数不太好. 
- ReLU或多或少是卷积神经网络的标准单元. 
- 可以探索Leaky ReLU/Maxout/ELU. 
- tanh sigmoid函数仍然用于长短期记忆网络（LSTMs）/循环神经网络（RNNs）（我们稍后会看到更多相关内容）. 
### 模块9.4：更好的初始化策略
如果我们将所有权重初始化为0会发生什么呢？第1层的所有神经元将获得相同的激活. 现在在反向传播过程中会发生什么呢？
$$\nabla w_{11}=\frac{\partial \mathscr{L}(w)}{\partial y} \cdot \frac{\partial y}{\partial h_{11}} \cdot \frac{\partial h_{11}}{\partial a_{11}} \cdot x_{1}$$
$$\nabla w_{21}=\frac{\partial \mathscr{L}(w)}{\partial y} \cdot \frac{\partial y}{\partial h_{12}} \cdot \frac{\partial h_{12}}{\partial a_{12}} \cdot x_{1}$$
但是 $h_{11}=h_{12}$ ，并且 $a_{11}=a_{12}$ ，所以 $\nabla w_{11}=\nabla w_{21}$ . 
我们现在考虑一个前馈网络：
- 输入：1000个点，每个点 $\in R^{500}$ ，输入数据从单位高斯分布中抽取. 
- 网络有5层，每层有500个神经元. 
我们将使用不同的权重初始化在这个网络上运行前向传播. 
$$W = np.random.randn(fan\_in, fan\_out) * 0.01$$
让我们尝试将权重初始化为小的随机数. 我们将看看不同层的激活会发生什么. 
在反向传播过程中会发生什么呢？回想一下， $\nabla w_{1}$ 与通过它的激活成正比. 如果一层中的所有激活都非常接近0，连接这一层到下一层的权重的梯度会发生什么呢？它们都会接近0（梯度消失问题）. 
$$W = np.random.randn(fan\_in, fan\_out)$$
让我们尝试将权重初始化为大的随机数. 大多数激活已经饱和. 饱和时的梯度会发生什么呢？它们都会接近0（梯度消失问题）. 
让我们尝试找到一种更有原则的权重初始化方法. 假设输入和权重的均值为0， $Var(x_{i}) = Var(x)$ 对所有 $i$ 成立， $Var(w_{1i}) = Var(w)$ 对所有 $i$ 成立. 
$$s_{11}=\sum_{i = 1}^{n}w_{1i}x_{i}$$
$$Var(s_{11}) = Var(\sum_{i = 1}^{n}w_{1i}x_{i})=\sum_{i = 1}^{n}Var(w_{1i}x_{i})$$
$$=\sum_{i = 1}^{n}[(E[w_{1i}])^{2}Var(x_{i})+(E[x_{i}])^{2}Var(w_{1i})+Var(x_{i})Var(w_{1i})]$$
$$=\sum_{i = 1}^{n}Var(x_{i})Var(w_{1i})=(nVar(w))(Var(x))

一般来说，
$$Var(S_{1i}) = (nVar(w))(Var(x))$$

如果 $nVar(w) \gg 1$ 会怎样呢？ $S_{1i}$ 的方差会很大. 如果 $nVar(w) \to 0$ 又会怎样呢？ $S_{1i}$ 的方差会很小. 

让我们看看如果再增加一层会发生什么. 使用与上述相同的步骤，我们会得到：
$$\begin{gathered}Var(s_{21})=\sum_{i = 1}^{n}Var(s_{1i})Var(w_{2i})\\ = nVar(s_{1i})Var(w_{2})\end{gathered}$$

$$Var(S_{i1}) = nVar(w_{1})Var(x)$$

$$\begin{aligned}Var(s_{21}) &\propto [nVar(w_{2})][nVar(w_{1})]Var(x)\\ &\propto [nVar(w)]^{2}Var(x)\end{aligned}$$

假设所有层的权重具有相同的方差. 

一般来说，
$$Var(s_{ki}) = [nVar(w)]^{k}Var(x)$$

为了确保任何一层输出的方差既不会爆炸也不会缩小，我们希望：
$$nVar(w) = 1$$

如果我们从单位高斯分布中抽取权重并将它们缩放 $\frac{1}{\sqrt{n}}$ ，那么：
$$\begin{aligned}nVar(w) &= nVar(\frac{z}{\sqrt{n}})\\ &= n * \frac{1}{n}Var(z)=1 \leftarrow(单位高斯分布)\end{aligned}$$

$$W = np.random.randn(fan\_in,fan\_out)/\sqrt(fan\_in)$$

让我们看看如果使用这种初始化会发生什么. 

然而，这种方法对ReLU神经元不起作用. 为什么呢？何恺明等人认为，在处理ReLU神经元时需要一个系数2. 直观地说，这是因为ReLU神经元的范围只限于空间的正半轴. 

$$W = np.random.randn(fan\_in,fan\_out)/\sqrt(fan\_in/2)$$

确实，当我们考虑这个系数2时，我们会看到更好的性能. 

### 模块9.5：批量归一化
我们现在将介绍一种称为批量归一化的方法，它让我们在初始化时可以不用那么小心翼翼. 

为了理解批量归一化背后的直觉，让我们考虑一个深度网络. 让我们关注两层之间权重的学习过程. 通常我们使用小批量算法. 如果 $h_{3}$ 的分布不断发生变化会怎样呢？换句话说，如果在不同的小批量中 $h_{3}$ 的分布持续改变，学习过程会变得容易还是困难呢？

如果每一层的预激活是单位高斯分布，这会很有帮助. 为什么不通过标准化预激活来明确确保这一点呢？
$$\hat{s_{ik}}=\frac{s_{ik}-E[s_{ik}]}{\sqrt{var(s_{ik})}}$$

但是我们如何计算 $E[s_{ik}]$ 和 $Var[s_{ik}]$ 呢？我们从小批量数据中计算它们. 这样我们就明确确保了不同层输入的分布在不同批次之间不会改变. 

这就是带有批量归一化的深度网络的样子. 这样做合法吗？是的，因为就像tanh层是可微的一样，批量归一化层也是可微的. 因此我们可以通过这一层进行反向传播. 

 $\gamma^{k}$ 和 $\beta^{k}$ 是网络的额外参数. 问题来了：我们一定想要强制给tanh层输入一个单位高斯分布吗？为什么不让网络自己学习什么是最好的呢？在批量归一化步骤之后添加以下步骤：
$$y^{(k)}=\gamma^{k}\hat{s_{ik}}+\beta^{(k)}$$

如果网络学习到：
$$\gamma^{k}=\sqrt{var(x^{k})}$$
$$\beta^{k}=E[x^{k}]$$

会发生什么呢？我们将恢复 $s_{ik}$ . 换句话说，通过调整这些额外参数，如果这样更有利的话，网络可以学习恢复 $s_{ik}$ . 

我们现在将在MNIST数据上比较有批量归一化和没有批量归一化的两层网络的性能……

2016 - 2017年：仍然是激动人心的时代. 出现了更好的优化方法、数据驱动的初始化方法，以及超越批量归一化的技术.  