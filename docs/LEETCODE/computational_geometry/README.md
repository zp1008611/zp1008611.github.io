# 计算几何

## Reference

- https://leetcode.cn/discuss/post/3584388/fen-xiang-gun-ti-dan-shu-xue-suan-fa-shu-gcai/

## 点、线

1. 给定一个数组 coordinates ，其中 coordinates[i] = [x, y] ， [x, y] 表示横坐标为 x、纵坐标为 y 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。[LC1232](https://leetcode.cn/problems/check-if-it-is-a-straight-line/description/)

2. 给你一个二维整数数组 stockPrices ，其中 stockPrices[i] = [dayi, pricei] 表示股票在 dayi 的价格为 pricei 。折线图 是一个二维平面上的若干个点组成的图，横坐标表示日期，纵坐标表示价格，折线图由相邻的点连接而成。请你返回要表示一个折线图所需要的 最少线段数 。[LC2280](https://leetcode.cn/problems/minimum-lines-to-represent-a-line-chart/description/)

3. 给定两条线段（表示为起点start = {X1, Y1}和终点end = {X2, Y2}），如果它们有交点，请计算其交点，没有交点则返回空值。[LC面试题16.03](https://leetcode.cn/problems/intersection-lcci/description/)

4. 给定一个二维平面及平面上的 N 个点列表Points，其中第i个点的坐标为Points[i]=[Xi,Yi]。请找出一条直线，其通过的点的数目最多。设穿过最多点的直线所穿过的全部点编号从小到大排序的列表为S，你仅需返回[S[0],S[1]]作为答案，若有多条直线穿过了相同数量的点，则选择S[0]值较小的直线返回，S[0]相同则选择S[1]值较小的直线返回。[LC面试题16.14](https://leetcode.cn/problems/best-line-lcci/description/)


## 圆

1. 给你一个以 (radius, xCenter, yCenter) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2) ，其中 (x1, y1) 是矩形左下角的坐标，而 (x2, y2) 是右上角的坐标。如果圆和矩形有重叠的部分，请你返回 true ，否则返回 false 。换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。[LC1401](https://leetcode.cn/problems/circle-and-rectangle-overlapping/description/)


2. Alice 向一面非常大的墙上掷出 n 支飞镖。给你一个数组 darts ，其中 darts[i] = [xi, yi] 表示 Alice 掷出的第 i 支飞镖落在墙上的位置。Bob 知道墙上所有 n 支飞镖的位置。他想要往墙上放置一个半径为 r 的圆形靶。使 Alice 掷出的飞镖尽可能多地落在靶上。给你整数 r ，请返回能够落在 任意 半径为 r 的圆形靶内或靶上的最大飞镖数。[LC1453](https://leetcode.cn/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/description/)


## 矩形

1. 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。矩形的上下边平行于 x 轴，左右边平行于 y 轴。如果相交的面积为 正 ，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。给出两个矩形 rec1 和 rec2 。如果它们重叠，返回 true；否则，返回 false 。 [LC836](https://leetcode.cn/problems/rectangle-overlap/description/)

2. 给你 二维 平面上两个 由直线构成且边与坐标轴平行/垂直 的矩形，请你计算并返回两个矩形覆盖的总面积。每个矩形由其 左下 顶点和 右上 顶点坐标表示：第一个矩形由其左下顶点 (ax1, ay1) 和右上顶点 (ax2, ay2) 定义。第二个矩形由其左下顶点 (bx1, by1) 和右上顶点 (bx2, by2) 定义。[LC223](https://leetcode.cn/problems/rectangle-area/description/)

3. 给定2D空间中四个点的坐标 p1, p2, p3 和 p4，如果这四个点构成一个正方形，则返回 true 。点的坐标 pi 表示为 [xi, yi] 。 输入没有任何顺序 。一个 有效的正方形 有四条等边和四个等角(90度角)。[LC593](https://leetcode.cn/problems/valid-square/description/)

4. 给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。如果没有任何矩形，就返回 0。[LC939](https://leetcode.cn/problems/minimum-area-rectangle/description/)

5. 给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边不一定平行于 x 轴和 y 轴。如果没有任何矩形，就返回 0。[LC963](https://leetcode.cn/problems/minimum-area-rectangle-ii/description/)

## 凸包

1. 给定一个数组 trees，其中 trees[i] = [xi, yi] 表示树在花园中的位置。你被要求用最短长度的绳子把整个花园围起来，因为绳子很贵。只有把 所有的树都围起来，花园才围得很好。返回恰好位于围栏周边的树木的坐标。[LC587](https://leetcode.cn/problems/erect-the-fence/description/)

2. 小王来到了游乐园，她玩的第一个项目是模拟推销员。有一个二维平面地图，其中散布着 N 个推销点，编号 0 到 N-1，不存在三点共线的情况。每两点之间有一条直线相连。游戏没有规定起点和终点，但限定了每次转角的方向。首先，小王需要先选择两个点分别作为起点和终点，然后从起点开始访问剩余 N-2 个点恰好一次并回到终点。访问的顺序需要满足一串给定的长度为 N-2 由 L 和 R 组成的字符串 direction，表示从起点出发之后在每个顶点上转角的方向。根据这个提示，小王希望你能够帮她找到一个可行的遍历顺序，输出顺序下标（若有多个方案，输出任意一种）。可以证明这样的遍历顺序一定是存在的。[LCLCP15](https://leetcode.cn/problems/you-le-yuan-de-mi-gong/description/)