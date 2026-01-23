# AgentFlow

## Reference

- **论文链接**: [IN-THE-FLOW AGENTIC SYSTEM OPTIMIZATION FOR
EFFECTIVE PLANNING AND TOOL USE arXiv:2510.05592](https://arxiv.org/pdf/2510.05592)
- **代码仓库**: [GitHub - lupantech/AgentFlow](https://github.com/lupantech/AgentFlow)

## 1 训练目的


## 2 训练方法

### Flow-GRPO


**Require:** Dataset $\mathcal{D}$, Action Planner policy $\pi_\theta$, Tool Executor $\mathcal{E}$, Executive Verifier $\mathcal{V}$, Solution Generator $\mathcal{G}$, Toolset $K$, and Shared Evolving Memory $M$

**Ensure:** Optimized Action Planner parameters $\theta^*$

1. **for** each training iteration **do**
2. &nbsp;&nbsp;&nbsp;&nbsp;**for** each query–label pair $(q, y^*) \sim \mathcal{D}$ **do**
3. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**1. IN-THE-FLOW ROLLOUT GENERATION**
4. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Initialize: $t \leftarrow 1$, $M^t \leftarrow q$
5. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**repeat**
6. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$a^t \sim \pi_\theta(a^t \mid q, K, M^t)$ {*Plan Action*}
7. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$e^t \sim \mathcal{E}(e^t \mid a^t, K)$ {*Execute Action*}
8. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$v^t \sim \mathcal{V}(v^t \mid q, e^t, M^t)$ {*Verify Result*}
9. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$M^{t+1} = f_{\text{mem}}(M^t, a^t, e^t, v^t)$ {*Update Memory*}
10. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$t \leftarrow t + 1$
11. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**until** termination condition met
12. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$o \sim \mathcal{G}(o \mid q, M^T)$ {*Generate Final Solution*}
13. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**2. REWARD COMPUTATION**
14. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$R(a^t) = \tilde{R}(o, q, y^*)$, &nbsp;&nbsp;&nbsp;&nbsp;$\forall t = 1, \ldots, T$
15. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**3. POLICY UPDATE**
16. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Update the Action Planner policy $\pi_\theta$ by maximizing the Flow-GRPO objective (Eq. 5)
17. &nbsp;&nbsp;&nbsp;&nbsp;**end for**
18. **end for**
19. **return** optimized parameters $\theta^*$


给定查询指令 $q$ 和工具集 $K$ ，系统会进行可变轮次的交互。设 $M^{t}$ 表示第 $t$ 轮开始前的内存状态（其中 $M^{1}$ 初始化为查询相关信息）。在第 $t$ 轮中，规划器 $P$ （一个可训练策略 $\pi_{\theta}$ ）会制定子目标、从工具集 $K$ 中选择合适的工具 $k$ ，并从内存中提取相关上下文，最终生成动作： $a^{t} \sim \pi_{\theta}(a^{t} | q, K, M^{t})$ 。


工具执行器 $\varepsilon$ 会结合上下文调用所选工具，生成执行观测结果 $e^{t} \sim \mathcal{E}(e^{t} | a^{t}, K)$ 。随后，执行验证器 $v$ 会评估 $e^{t}$ 的有效性，以及累积的内存是否足以解决查询问题，最终输出二进制验证信号 $v^{t} \sim \mathcal{V}(v^{t} | q, e^{t}, M^{t})$ 。若 $v^{t}=0$ （需继续交互），内存会通过确定性方式更新以整合新证据： $M^{t+1}=f_{mem}(M^{t}, a^{t}, e^{t}, v^{t})$ ，其中 $f_{mem}(\cdot)$ 表示内存更新函数，该函数以简洁的结构化形式记录智能体的过程信息，同时包含时间、轮次索引、错误信号等上下文细节。

该过程会重复执行，直至 $v^{t}=1$（终止条件）或达到预设的最大轮次限制。当第 $T$ 轮终止时，解决方案生成器 $G$ 会基于查询指令和累积的内存生成最终答案 $o$，其数学表达式为：$o \sim G(o | q, M^{T})$。


### 奖励函数

**最终结果奖励**：为中间动作分配信用值具有挑战性，因为每个动作 $a^{t}$ 仅间接影响最终解决方案，且其价值可能需经过多个轮次后才会显现（例如错误累积或改进累积）。为避免脆弱的局部反馈，我们采用**基于最终结果的奖励机制**：一次轨迹推演（rollout）中的所有动作都会获得相同的全局奖励信号，该信号基于最终解决方案 $o$ 相对于查询指令 $q$ 和真实标签 $y^{*}$ 的正确性：

$$
r=R\left(a^{t}\right)=\overline{R}\left(o, q, y^{*}\right), \forall t=1, ..., T,
$$

其中 $\bar{R}(o, q, y^{*}) \in\{0,1\}$ 由大语言模型评判标准（LLM-as-judge rubric）赋值，用于判定语义、数值及选项层面的等价性。该机制将轨迹级成功信号反向传递至整个推理链，使每个决策 $a^{t}$ 都与全局正确性对齐。


## 3 评测数据