# 三角函数

## 5.1.2 弧度制

上课！同学们好！请坐！同学们，大家回想一下，我们在生活中测量长度时，使用有米也有英尺；测量质量时，使用的单位有千克也有磅. 不同的单位制在不同场景下都给我们带来了便利. 那大家想一想，我们之前学习角的度量时，用的是度作为单位，也就是角度制. 那角的度量是不是也能像长度、质量那样，有不同的单位制呢？能不能用十进制的实数来度量角的大小，让计算和研究更方便呢？今天，我们就一起来学习另一种度量角的单位制——弧度制. 

我们先来看，假设有一条射线 $OA$ 绕端点 $O$ 旋转到 $OB$ 形成角$\alpha$ ，假设 $\alpha$ 的大小为 $n^{\circ}$（$\alpha=n^{\circ}$），射线 $OA$ 上一点 $P$（假设 $OP$ 长度为 $r$）以及假设 $P$ 的旋转轨迹 弧 $\overset{\LARGE{\frown}}{PP_1}$ 的长度为$\ell$ ，我们可以通过圆的周长求得 $\ell$的长度，$\ell=2\pi r\cdot \frac{n}{360} = \frac{n \pi r}{180}$ ，讲$r$除过来可得 $\frac{l}{r}=n \frac{\pi}{180}$. 

如果在射线 $OA$ 上再另取一点 $Q$（假设 $OQ$ 长度为 $r_1$）以及假设 $Q$ 的旋转轨迹 弧 $\overset{\LARGE{\frown}}{QQ_1}$ 的长度为$\ell_1$ ，那么 $l_{1}$ 与 $r_{1}$ 的比值是多少呢？同学参照上面 $\ell$比$r$ 的计算过程，自己计算一下 $l_{1}$ 与 $r_{1}$ 的比值，一会我请一位同学进行阐述. 好的，我看大家写得差不多了，有请这位同学回答一下，好的，你说 $\frac{\ell_1}{r_1}=n \frac{\pi}{180}$，好的，回答得非常好，其实同学们可以发现，圆心角$\alpha$ 所对的弧长与半径的比值，只和 $\alpha$ 的大小 $n$ 有关，而且这个比值与 $\alpha$ 是一一对应关系，因此我们可以使用对应弧长与半径的比值来刻画角度. 

基于此，我们规定：对于角 $\alpha$， 如果对应弧长 $\ell$ 比半径 $r$ 等于 $1$， 我们就称 $\alpha$ 为 $1$ 弧度的角，记作 $\alpha= 1 \text{ rad}$. 
如果对应弧长 $\ell$ 比半径 $r$ 等于 一个正数 $x$ 的绝对值（$|x|$）， 我们就称 $\alpha$ 为 $x$ 弧度的角，记作 $\alpha= x \text{ rad}$.

此外，$\alpha$ 的正负由角$\alpha$ 终边的旋转方向决定，逆时针旋转为正，顺时针旋转为负，$\alpha$ 的正负也会影响其对应弧度数的大小. 对于正角, $\alpha$ 的弧度数为正（$\alpha=\frac{l}{r} \text{ rad}$）； 对于负角, $\alpha$ 的弧度数为负（$\alpha=-\frac{l}{r} \text{ rad}$）；对于零角，$\alpha$ 的弧度数为零（$\alpha=0 \text{ rad}$）. 

另外，角度制和弧度制是可以换算的. 我们有 $360^{\circ}=2\pi\text{ rad}$，$180^{\circ}=\pi\text{ rad}$，$1^{\circ}=\frac{\pi}{180}\text{ rad}$，$1\text{ rad}=\left(\frac{180}{\pi}\right)^{\circ}$.


同学们，今天我们学习了弧度制这个重要的知识. 我们知道了弧度制是另一种度量角的单位制，它是根据圆的弧长与半径的关系来定义的. 还学习了角度制和弧度制的换算公式. 大家课后要多做相关练习，巩固今天所学知识. 今天的课就到这里，同学们下课！ 


## 5.2.1 三角函数的概念

上课！同学们好！请坐！上节课我们学习了任意角和弧度制，利用弧度制，我可以将角的范围已经扩展到了全体实数. 利用这些知识，今天我们来研究一下单位圆上点及其对应圆心角的关系，这就是我们今天要学习主题（板书课题：5.2三角函数的概念）. 

初中的时候学过，角的正弦值、余弦值和正切值这三种三角函数值的定义，对于给定三角形的角 $\alpha$，我们定义 $\alpha$的正弦值为 $\sin \alpha = \frac{a}{c}$， 余弦值为 $\cos \alpha = \frac{b}{c}$, 正切值为 $\tan\alpha = \frac{a}{b}$. 今天我们来学习更为严谨的三角函数的定义. 假设在一个单位圆中，以圆心$O$为原点，以射线$OA$为$x$轴的非负半轴建立直角坐标系，点$A$坐标是$(1,0)$. 当射线$OA$绕点$O$按逆时针方向旋转角$\alpha$，终止位置为$OP$，点$P$坐标为$(x,y)$. 大家想想，当$\alpha=\frac{\pi}{6}$时，点$P$的坐标是什么呢？对，$y=1\cdot \sin\frac{\pi}{6}=\frac{\sqrt{3}}{2}$， $x = \sqrt{1-y^2}=\frac{1}{2}$；同理，当$\alpha=\frac{\pi}{2}$时，点$P$坐标是$(0,1)$；当$\alpha=\frac{2\pi}{3}$时，点$P$坐标是$(-\frac{1}{2},\frac{\sqrt{3}}{2})$ . 可以发现，对于任意给定的一个角$\alpha\in R$，它的终边$OP$与单位圆交点$P$的坐标，无论是横坐标$x$还是纵坐标$y$，都是唯一确定的. 根据函数的定义，$y$ 与 $\alpha$ 可以构成一个函数关系, $x$ 与 $\alpha$ 也可以构成函数关系，更特别地，当$x\neq 0$时，$y$与$x$ 的比值也是由$\alpha$唯一确定的，因此 $\frac{y}{x}$ 和 $\alpha$ 也可以构成函数关系.  

基于这三种函数关系，我们给出三角函数的定义：点$P$的纵坐标$y$叫做$\alpha$的正弦函数，记作$y = \sin\alpha$；点$P$的横坐标$x$叫做$\alpha$的余弦函数，记作$x = \cos\alpha$；当$x\neq0$时，点$P$的纵坐标与横坐标的比值$\frac{y}{x}$叫做$\alpha$的正切函数，记作$\tan\alpha$. 这里要注意，由于$x\neq 0$，所以正切函数的定义域$x\in\{x|x\neq\frac{\pi}{2}+k\pi,k\in Z\}$，而正弦函数和余弦函数的定义域则为$R$. 我们把正弦函数、余弦函数和正切函数统称为三角函数. 



通过今天的学习，我们知道了三角函数的定义和定义域. 这些知识是三角函数应用的重要基础，大家课后要多做练习，熟练掌握公式的运用. 今天的课就到这里，同学们下课！ 

## 5.2.2 同角三角函数的基本关系

上课！同学们好！请坐！同学们，之前我们学习了三角函数的定义，知道了三角函数值与角的终边和单位圆交点坐标的关系. 那大家想想，对于同一个角的正弦、余弦和正切值，它们之间有没有什么内在联系呢？这就是我们今天要学习的主题. （板书：同角三角函数的基本关系）

我们先回顾一下三角函数的定义. 在单位圆中，设角 $\alpha$ 的终边与单位圆交于点 $P(x,y)$ ，那么 $\sin\alpha = y$ ， $\cos\alpha = x$ ， $\tan\alpha=\frac{y}{x}(x\neq0)$ . （画图）

那下面老师来问同学们一个问题，$\sin^{2}\alpha+\cos^{2}\alpha$等于什么呢？以及 当$\alpha\neq\frac{\pi}{2}+k\pi$时, $\frac{\sin\alpha}{\cos\alpha}$等于什么呢？它们可以用 $y$ 和 $x$ 来表示吗？请同学们就这两个问题进行四人小组讨论，等会我请一位同学阐述一下自己的看法，我看大家讨论地非常激烈，好，有请这位同学来说一下，你说
$\sin^{2}\alpha+\cos^{2}\alpha=y^2+x^2$，没错回答得很好，那么根据勾股定理，$y^2+x^2$等于单位圆的半径也就是等于1.
再看，对于$\frac{\sin\alpha}{\cos\alpha}$，根据三角函数的定义，就等于$\frac{y}{x}$，这不就是正切函数 $\tan x$ 的定义吗？

这样我们就得到同角三角函数的两个基本关系式，这两个式子非常重要，请同学要牢记. 

下面我们通过例题来看看怎么运用这些关系. 例6中，已知 $\sin\alpha = -\frac{3}{5}$ ，求 $\cos\alpha$ 和 $\tan\alpha$ 的值. 好的，请同学们在草稿纸上试一下这道题的计算，时间为两分钟，一会我来讲解一下这道题. 对于题目中的 $\alpha$， 因为 $\sin\alpha<0$ 且 $\sin\alpha\neq - 1$ ，所以 $\alpha$ 是第三或第四象限角. 根据 $\sin^{2}\alpha+\cos^{2}\alpha = 1$ ，可以算出 $\cos^{2}\alpha = 1 - \sin^{2}\alpha = 1 - (-\frac{3}{5})^{2}=\frac{16}{25}$  . 如果 $\alpha$ 是第三象限角， $\cos\alpha<0$ ，所以 $\cos\alpha = -\frac{4}{5}$ ， $\tan\alpha=\frac{\sin\alpha}{\cos\alpha}=\frac{3}{4}$ ；如果 $\alpha$ 是第四象限角， $\cos\alpha=\frac{4}{5}$ ， $\tan\alpha = -\frac{3}{4}$  . 

好啦，同学们，我们来总结一下今天学习的内容. 今天我们学习了同角三角函数的两个基本关系： $\sin^{2}\alpha+\cos^{2}\alpha = 1$ 和 $\frac{\sin\alpha}{\cos\alpha}=\tan\alpha(\alpha\neq k\pi+\frac{\pi}{2},k\in Z)$  . 这些关系是三角函数应用的重要基础，大家课后要多做练习，熟练这些知识. 今天的课就到这里，同学们再见！ 

## 5.3 诱导公式

上课！同学们好！请坐. 同学们，之前我们学习了同角三角函数的基本关系，它是基于圆的几何性质得到的. 大家都知道，圆具有非常好的对称性，而函数呢，像我们熟悉的奇函数、偶函数，它们的奇偶性也是一种对称性的体现. 所以今天，我们就从圆的对称性出发，去探索三角函数的对称性，并学习一组新的重要公式——诱导公式. 


我们先来看关于原点对称的情况. 在直角坐标系里有一个单位圆，任意角 $\alpha$ 的终边和单位圆相交于点 $P_1$. 如果把 $P_1$ 关于原点对称，得到点 $P_2$，以 $OP_2$ 为终边的角 $\beta$. 那同学们知道 $\beta$ 和 $\alpha$ 有什么关系吗？没错，其实 $\beta$ 和 $\pi+\alpha$ 的终边是一样的，也就是 $\beta = 2k\pi+(\pi+\alpha)$ ， $k\in Z$ . 为了方便研究，我们只要搞清楚 $\pi+\alpha$ 与 $\alpha$ 的三角函数值之间的关系就行啦. 

假设 $P_1(x_1,y_1)$ ，因为 $P_2$ 是 $P_1$ 关于原点的对称点，所以 $P_2(-x_1,-y_1)$ . 根据三角函数的定义， $\sin\alpha = y_1$ ， $\cos\alpha = x_1$ ， $\tan\alpha=\frac{y_1}{x_1}$ ； $\sin(\pi+\alpha)=y_2 = -y_1$ ， $\cos(\pi+\alpha)=x_2 = -x_1$ ， $\tan(\pi+\alpha)=\frac{y_2}{x_2}=\frac{-y_1}{-x_1}=\frac{y_1}{x_1}$  . 这样我们就得到了第一组诱导公式：
 $\sin(\pi+\alpha)=-\sin\alpha$， 
 $\cos(\pi+\alpha)=-\cos\alpha$， 
 $\tan(\pi+\alpha)=\tan\alpha$. 

接着，看 $P_1$ 关于 $x$ 轴对称的情况. 作 $P_1$ 关于 $x$ 轴的对称点 $P_3$ ，以 $OP_3$ 为终边的角就是 $-\alpha$ ，由此我们可以推出第二组诱导公式：
 $\sin(-\alpha)=y_3=-y_1=-\sin\alpha$，
 $\cos(-\alpha)=x_3=x_1=\cos\alpha$，
 $\tan(-\alpha)=\frac{y_3}{x_3}=-\tan\alpha$. 

再看 $P_1$ 关于 $y$ 轴对称的情况. 作 $P_1$ 关于 $y$ 轴的对称点 $P_4$ ，以 $OP_4$ 为终边的角是 $\pi-\alpha$ ，进而得到第三组诱导公式：
 $\sin(\pi-\alpha)=y_4=y_1=\sin\alpha$，
 $\cos(\pi-\alpha)=x_4=-x_1=-\cos\alpha$， 
 $\tan(\pi-\alpha)=-\tan\alpha$.

利用这三组公式，我们就能把任意角的三角函数转化为锐角三角函数啦. 下面我们来做几道题目来对这种转化进行一下实操. 


例1，利用公式求下列三角函数值：
(1) $\cos225^{\circ}$ ， $\cos225^{\circ}=\cos(180^{\circ}+45^{\circ}) = -\cos45^{\circ}=-\frac{\sqrt{2}}{2}$ ；
(2) $\sin\frac{8\pi}{3}$ ， $\sin\frac{8\pi}{3}=\sin(2\pi+\frac{2\pi}{3})=\sin\frac{2\pi}{3}=\sin(\pi-\frac{\pi}{3})=\sin\frac{\pi}{3}=\frac{\sqrt{3}}{2}$ ；


好啦，同学们，我们来总结一下今天学的内容. 今天我们通过单位圆的对称性，推导出了三组诱导公式. 第一组诱导公式告诉我们 $\sin(\pi+\alpha)=-\sin\alpha$ ， $\cos(\pi+\alpha)=-\cos\alpha$ ， $\tan(\pi+\alpha)=\tan\alpha$ ；第二组诱导公式是 $\sin(-\alpha)=-\sin\alpha$ ， $\cos(-\alpha)=\cos\alpha$ ， $\tan(-\alpha)=-\tan\alpha$ ；第三组诱导公式是 $\sin(\pi-\alpha)=\sin\alpha$ ， $\cos(\pi-\alpha)=-\cos\alpha$ ， $\tan(\pi-\alpha)=-\tan\alpha$  ；
这些公式是三角函数应用的重要基础，大家课后要多做练习，熟练掌握公式的运用. 今天的课就到这里，同学们再见！ 


## 5.5.1 1 两角差与和的余弦公式

上课！同学们好！请坐！同学们，之前我们学习了诱导公式，诱导公式描述了 $\alpha$ 与 $\pi+\alpha$， $\alpha$ 与 $\pi-\alpha$, $-\alpha$ 与 $\alpha$， $\frac{\pi}{2}+\alpha$ 和 $\alpha$ 以及 $\frac{\pi}{2}-\alpha$ 和 $\alpha$ 的关系. 诱导公式是 $\pi$、$\frac{\pi}{2}$ 以及$0$ 角这三种特殊角和任意角 $\alpha$ 的和（或差）的三角函数关系. 现在我们把特殊角换成任意角 $\beta$ ，那任意角 $\alpha$ 和 $\beta$ 的和（或差）的三角函数，和 $\alpha$ 、 $\beta$ 本身的三角函数有什么关系呢？这就是我们今天探究的主题. （板书：两角差与和的余弦公式）

我们先来看两角差的余弦公式的推导. （展示课本图5.5 - 1）在单位圆中，设单位圆和 $x$ 轴正半轴交点是 $A(1,0)$ ，以 $x$ 轴非负半轴为始边作角 $\alpha$ 、 $\beta$ 、 $\alpha - \beta$ ，它们终边和单位圆交点分别是 $P_1(\cos\alpha,\sin\alpha)$ 、 $A_1(\cos\beta,\sin\beta)$ 、 $P(\cos(\alpha - \beta),\sin(\alpha - \beta))$ . 

根据圆的旋转对称性，把扇形 $OAP$ 绕点 $O$ 旋转 $\beta$ 角， $A$ 、 $P$ 会和 $A_1$ 、 $P_1$ 重合，弧 $\widehat{AP}$ 和 $\widehat{A_1P_1}$ 重合，所以弦 $AP = A_1P_1$  . 我们利用两点间距离公式列出等式，$AP^2=(x_P-x_A)^2+(y_A-y_P)^2=\left[\cos(\alpha-\beta)^2-1\right]^2+\sin^2(\alpha-\beta)$，$A_1P_1^2=(x_{P_1}-x_{A_1})^2+(y_{A_1}-y_{P_1})^2=(\cos\alpha-\cos\beta)^2+(\sin\alpha-\sin\beta)^2$，那么就有 $\left[\cos(\alpha-\beta)^2-1\right]^2+\sin^2(\alpha-\beta)=(\cos\alpha-\cos\beta)^2+(\sin\alpha-\sin\beta)^2$，请同学们在下面对这个等式进行化简，一会我请一位同学进行阐述，好的，我看大家写得差不多，有请这位同学回答一下，好的，你说化简结果为 $\cos(\alpha - \beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$，好的，回答地非常好，同学们，我们现在得到的这个公式就是两角差的余弦公式，这个公式对所有的角 $\alpha$ 、 $\beta$ 都成立，我们把它简记作 $C_{(\alpha - \beta)}$  . 

有了两角差的余弦公式，我们来推导两角和的余弦公式 $\sin(\alpha+\beta)$，大家觉得这个公式可以由两角差的余弦公式推导得到吗？没错，是可以的，我们知道 $\alpha + \beta=\alpha-(-\beta)$  ，把 $-\beta$ 代入两角差的余弦公式，就能得到两角和的余弦公式 $\cos(\alpha + \beta)=\cos\alpha\cos\beta - \sin\alpha\sin\beta$  ，我们把这个公式简记作 $C_{(\alpha + \beta)}$ . 大家对比这两个公式，可以看到两角差对应的是一个和式，但是两角和对应的是一个差式，大家要对这两点特别注意，在做题的时候不要混淆. 

下面我们通过例题来巩固一下两角差的余弦公式. 例1，利用公式 $C_{(\alpha - \beta)}$ 证明 $\cos(\frac{\pi}{2}-\alpha)=\sin\alpha$. $\cos(\frac{\pi}{2}-\alpha)=\cos\frac{\pi}{2}\cos\alpha+\sin\frac{\pi}{2}\sin\alpha= 1\cdot\cos\alpha + 0\cdot \sin\alpha=\cos\alpha$. 


好啦，同学们，我们来总结一下今天学习的内容. 今天我们学习了两角差与和的余弦公式 $\cos(\alpha - \beta)=\cos\alpha\cos\beta+\sin\alpha\sin\beta$ ， $\sin(\alpha + \beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$. 这些公式是三角函数应用的重要基础，大家课后要多做练习，熟练掌握公式的运用. 今天的课就到这里，同学们再见！ 


## 5.5.1 3 二倍角的正弦、余弦、正切公式

同学们，之前我们学习了三角函数的基本概念和一些基础性质. 在实际应用中，我们常常会遇到需要计算不同角度三角函数值之间关系的情况. 比如，已知$\sin30^{\circ}$，那$\sin15^{\circ}$怎么求呢？一个角的二倍角的三角函数值和这个角本身的三角函数值有什么联系呢？这就是我们今天要学习的主题。（板书：二倍角的正弦、余弦、正切公式）. 

首先我们先来回顾一下前面我们所学的两角差与和的正弦、余弦和正切公式，我们先来学习和（差）角公式的应用. 之前我们已经知道了和（差）角的正弦、余弦、正切公式，即 $S_{(\alpha\pm\beta)}$ 、 $C_{(\alpha\pm\beta)}$ 、 $T_{(\alpha\pm\beta)}$  . 利用这些公式，我们可以求一些特殊角的三角函数值. 

比如求 $\sin15^{\circ}$ 的值，我们可以把 $15^{\circ}$ 看成 $45^{\circ}-30^{\circ}$ ，根据 $\sin(\alpha - \beta)=\sin\alpha\cos\beta - \cos\alpha\sin\beta$ ， $\sin15^{\circ}=\sin(45^{\circ}-30^{\circ})=\sin45^{\circ}\cos30^{\circ}-\cos45^{\circ}\sin30^{\circ}=\frac{\sqrt{2}}{2}\times\frac{\sqrt{3}}{2}-\frac{\sqrt{2}}{2}\times\frac{1}{2}=\frac{\sqrt{6}-\sqrt{2}}{4}$  . 同样的方法， $\cos75^{\circ}=\cos(45^{\circ}+30^{\circ})=\cos45^{\circ}\cos30^{\circ}-\sin45^{\circ}\sin30^{\circ}=\frac{\sqrt{2}}{2}\times\frac{\sqrt{3}}{2}-\frac{\sqrt{2}}{2}\times\frac{1}{2}=\frac{\sqrt{6}-\sqrt{2}}{4}$  ； $\sin75^{\circ}=\sin(45^{\circ}+30^{\circ})=\sin45^{\circ}\cos30^{\circ}+\cos45^{\circ}\sin30^{\circ}=\frac{\sqrt{2}}{2}\times\frac{\sqrt{3}}{2}+\frac{\sqrt{2}}{2}\times\frac{1}{2}=\frac{\sqrt{6}+\sqrt{2}}{4}$  ； $\tan15^{\circ}=\tan(45^{\circ}-30^{\circ})=\frac{\tan45^{\circ}-\tan30^{\circ}}{1+\tan45^{\circ}\tan30^{\circ}}=\frac{1-\frac{\sqrt{3}}{3}}{1 + 1\times\frac{\sqrt{3}}{3}} = 2-\sqrt{3}$  . 

接下来，我们推导倍角公式. 以和（差）角公式为基础，我们来探究 $\sin2\alpha$ ， $\cos2\alpha$  ， $\tan2\alpha$ 的公式. 在 $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$ 中，令 $\beta=\alpha$ ，就得到 $\sin2\alpha = 2\sin\alpha\cos\alpha$ ；在 $\cos(\alpha+\beta)=\cos\alpha\cos\beta-\sin\alpha\sin\beta$ 中，令 $\beta=\alpha$ ，可得 $\cos2\alpha=\cos^{2}\alpha - \sin^{2}\alpha$ ；由正切公式 $\tan(\alpha+\beta)=\frac{\tan\alpha+\tan\beta}{1-\tan\alpha\tan\beta}$ ，令 $\beta=\alpha$ ，推出 $\tan2\alpha=\frac{2\tan\alpha}{1-\tan^{2}\alpha}$ . 

如果我们希望二倍角的余弦公式中仅含 $\alpha$ 的正弦或余弦，利用 $\sin^{2}\alpha+\cos^{2}\alpha = 1$ ，可以进一步变形得到 $\cos2\alpha = 1 - 2\sin^{2}\alpha = 2\cos^{2}\alpha - 1$ . 这些公式都叫做倍角公式，它们揭示了 $\alpha$ 的三角函数与 $2\alpha$ 的三角函数之间的关系. 


下面我们通过例题来加深对这些公式的理解和运用. 

例1，已知 $\cos\theta=-\frac{3}{5}$ ， $\theta\in(\frac{\pi}{2},\pi)$ ，求 $\sin(\theta+\frac{\pi}{3})$ 的值. 首先，根据 $\sin^{2}\theta+\cos^{2}\theta = 1$ ，可得 $\sin\theta=\sqrt{1 - \cos^{2}\theta}=\sqrt{1 - (-\frac{3}{5})^{2}}=\frac{4}{5}$ . 然后根据 $\sin(\alpha+\beta)=\sin\alpha\cos\beta+\cos\alpha\sin\beta$ ， $\sin(\theta+\frac{\pi}{3})=\sin\theta\cos\frac{\pi}{3}+\cos\theta\sin\frac{\pi}{3}=\frac{4}{5}\times\frac{1}{2}+(-\frac{3}{5})\times\frac{\sqrt{3}}{2}=\frac{4 - 3\sqrt{3}}{10}$  . 


同学们，今天我们学习了三角函数的和（差）角公式的应用以及倍角公式. 和（差）角公式可以帮助我们计算一些特殊角的三角函数值，而倍角公式则建立了 $\alpha$ 与 $2\alpha$ 三角函数之间的联系. 在解题过程中，我们要注意观察题目中给出的条件，合理选择公式进行计算. 

从这些公式的推导过程可以看出，数学知识之间是紧密相连的，和（差）角公式是倍角公式推导的基础，它们构成了一个完整的知识体系. 希望大家课后多做练习，熟练掌握这些公式，这样在后续学习三角函数相关知识以及解决更复杂的数学问题时，就能更加得心应手啦！ 