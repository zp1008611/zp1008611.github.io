# Vehicle Routing Problem with Private Carrier(VRPPC)

## Reference




## 0 引言  
得益于卡车“门到门”服务的便利性，整车取送货运输业务十分普遍，如集装箱卡车运输、平板车大件运输等. 由于需求波动，运输企业平时仅维持较小规模的自有车辆，需求繁忙时会选择部分订单外包以降低成本，通常表现为最小化外包订单的费用和自有车辆路径成本之和. 因此，研究带订单选择的整车取送货路径优化问题具有重要的现实意义.   

然而，外包会导致运输公司失去运输组织和服务质量的控制. 因此，并非所有运输任务都可外包，如需超限许可证的运输任务等. 这要求运输企业在做外包决策时，考虑部分关键任务只能由自有车辆运输. 因此，在考虑外包订单选择时，增加部分订单只能由自有车辆运输的限制十分必要.   


## 1 问题描述  
某运输公司有车场（记为 0），
若干**同型号**车辆（数量为 $ K $）
和一些整车运输订单（集合为 $ N, N = N^R \cup N^F $）. $ N^R $ 为只能由自有车辆运输的保留订单集，$ N^F $ 为可外包的自由订单集. 
订单 $ i \in N $ 需在给定的出发地 $ O_i $ 装货，并直接送达目的地 $ D_i $ 卸货. $ O_i $ 的时间窗为 $[a_i^O, b_i^O]$，$ D_i $ 的时间窗由 $[a_i^O, b_i^O]$、装货服务时间和行驶时间共同确定. 订单 $ i \in N $ 从 $ O_i $ 驶往 $ D_i $ 的重车距离为 $ d_i $，运输时间为 $ T_i $，自有车辆的运费为 $ \alpha_i $，外包费用为 $ \gamma_i (\gamma_i > \alpha_i) $. 车辆在 $ O_i $ 和 $ D_i $ 的服务时间分别为 $ s_i^O $ 和 $ s_i^D $. 从 $ D_i $ 驶往 $ O_j, j \in N $ 的空驶距离为 $ d_{ij} $，运输时间为 $ T_{ij} $，自有车辆运费为 $ \beta_{ij} (\beta_{ij}/d_{ij} < \alpha_i/d_i) $. 计划期内 $[0, T]$ 如何分派自由订单和规划自有车辆的运输路径使完成所有任务的总成本最小.   

该问题可刻画为考虑城市选择的多旅行商问题. 具体地，将订单 $ i \in N $ 的固定运输路径 $ O_i $ 到 $ D_i $ 视为顶点 $ i \in N $，将 $ T_i + s_i^O + s_i^D $ 视为车辆在顶点 $ i \in N $ 的服务时间. 进而，该问题可描述为图 $ G = (V, A) $，其中 $ V = N \cup \{0\} $，$ A = \{ (i, j) \mid i \in V, j \in V, 且 $ i \neq j \} $. 

### 算法传入参数的 JSON 格式：  
```json
{
  "depot": 0,
  "vehicle_quantity": "K",
  "orders": {
    "set": "N",
    "reserved_orders": "N^R",
    "free_orders": "N^F"
  },
  "order_details": [
    {
      "order_id": "i",
      "origin": "O_i",
      "destination": "D_i",
      "origin_time_window": ["a_i^O", "b_i^O"],
      "heavy_distance": "d_i",
      "transport_time": "T_i",
      "own_freight": "α_i",
      "outsource_cost": "γ_i",
      "origin_service_time": "s_i^O",
      "destination_service_time": "s_i^D"
    }
  ],
  "empty_drive": [
    {
      "from_destination": "D_i",
      "to_origin": "O_j",
      "empty_distance": "d_{ij}",
      "empty_transport_time": "T_{ij}",
      "empty_freight": "β_{ij}"
    }
  ],
  "planning_period": ["0", "T"]
}
```





### 2.2 数学模型  
引入 0-1 决策变量 $ x_{ij}, y_i $ 和非负实变量 $ t_i $. 其中 $ x_{ij} = 1 $ 表示自有车辆选择弧 $ (i, j) \in A $，否则 $ x_{ij} = 0 $；$ y_i = 1 $ 表示订单 $ i \in N $ 被外包，否则 $ y_i = 0 $；$ t_i $ 表示自有车辆在订单 $ i \in N $ 的出发地开始装货的时间. 进而，可建立弧流模型如下：  
$$
\begin{align*}
\min & \sum_{i \in N} \alpha_i (1 - y_i) + \sum_{(i,j) \in A^R} \beta_{ij} x_{ij} + \sum_{i \in N^F} \gamma_i y_i \tag{1} \\
\text{s.t.} & \sum_{j \in V} x_{0j} \leq K \tag{2} \\
& \sum_{j \in V} x_{ij} = \sum_{j \in V} x_{ji},\ \forall i \in N \tag{3} \\
& \sum_{j \in V} x_{ij} = 1,\ \forall i \in N^R \tag{4} \\
& \sum_{j \in V} x_{ij} + y_i = 1,\ \forall i \in N \tag{5} \\
& a_i^O \leq t_i \leq b_i^O,\ \forall i \in N \tag{6} \\
& t_i + s_i^O + s_i^D + T_i + T_{ij} - t_j \leq (1 - x_{ij}) M, \\
& \forall i \in N, \forall j \in N, i \neq j \tag{7}
\end{align*}
$$  
目标函数（1）最小化总成本，其中第 1 部分为自有车辆重车成本，第 2 部分为自有车辆空车成本，第 3 部分为外包成本. 约束（2）表示自有车辆数约束. 约束（3）表示顶点 $ i \in N $ 的流平衡. 约束（4）表示保留订单只能被自有车辆服务. 约束（5）表示每个自由订单可被自有车辆服务，也可被外包；约束（4）和（5）隐含了约束 $ y_i = 0, \forall i \in N^R $. 约束（6）表示时间窗约束. 约束（7）表示任意两个被自有车辆服务的订单访问时间的关系，其中 $ M $ 为一个很大的数. 该模型为混合整数线性规划模型.   

用 $ R $ 表示订单集 $ N $ 中订单的所有可行路径的集合，$ p_r $ 表示路径 $ r \in R $ 的最小成本；$ \alpha_{ir} $ 表示路径 $ r \in R $ 是否包含订单 $ i \in N $，若是，$ \alpha_{ir} = 1 $，否则，$ \alpha_{ir} = 0 $. 引入 0-1 决策变量 $ x_r $，若自有车辆的最优解中包含路径 $ r \in R $，则 $ x_r = 1 $，否则 $ x_r = 0 $. 进而，该问题可以描述为集划分模型：  
$$
\begin{align*}
\min & \sum_{r \in R} p_r x_r + \sum_{i \in N^F} c_i y_i \tag{8} \\
\text{s.t.} & \sum_{r \in R} \alpha_{ir} x_r = 1, \forall i \in N^R \tag{9} \\
& \sum_{r \in R} \alpha_{ir} x_r + y_i = 1, \forall i \in N \tag{10} \\
& \sum_{r \in R} x_r \leq K \tag{11}
\end{align*}
$$  
目标函数（8）最小化总成本，其中第 1 部分为自有车辆成本，第 2 部分为外包成本. 约束（9）保证每个保留订单必须且只能被自有车辆服务一次. 约束（10）表示每个自由订单要么被自有车辆服务，要么被外包. 约束（11）表示自有车辆数约束. 该模型为 0-1 规划模型. 将约束（10）中 $ y_i $ 带入式（8），等价变换约束（9）和（10），则可得模型 1 的等价模型 2，其中 $ C = \hat{C} + \sum_{i \in N^F} c_i $.   
$$
\begin{align*}
\hat{C} = \min & \sum_{r \in R} \left( p_r - \sum_{i \in N^F} c_i \alpha_{ir} \right) x_r \tag{12} \\
\text{s.t.} & \sum_{r \in R} \alpha_{ir} x_r \geq 1, \forall i \in N^R \tag{13} \\
& \sum_{r \in R} \alpha_{ir} x_r \leq 1, \forall i \in N^F \tag{14}
\end{align*}
$$
