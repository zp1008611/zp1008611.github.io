# Search-R1

## Reference

- **论文链接**: [arXiv:2503.09516](https://arxiv.org/abs/2503.09516v5)
- **代码仓库**: [GitHub - PeterGriffinJin/Search-R1](https://github.com/PeterGriffinJin/Search-R1)


## 1 训练目的



## 2 训练方法


### 提示词

```bash
Answer the given question. You must conduct reasoning inside <think> and </think> first every time you get new information. After reasoning, if you find you lack some knowledge, you can call a search engine by <search> query </search>, and it will return the top searched results between <information> and </information>. You can search as many times as you want. If you find no further external knowledge needed, you can directly provide the answer inside <answer> and </answer> without detailed illustrations. For example, <answer> xxx </answer>. Question: question.
```

### 训练流程

**Require:** Input query $x$, policy model $\pi_\theta$, search engine $\mathcal{R}$, maximum action budget $B$.

**Ensure:** Final response $y$.

1. Initialize rollout sequence $y \leftarrow \emptyset$
2. Initialize action count $b \leftarrow 0$
3. **while** $b < B$ **do**
4. &nbsp;&nbsp;&nbsp;&nbsp;Initialize current action LLM rollout sequence $y_b \leftarrow \emptyset$
5. &nbsp;&nbsp;&nbsp;&nbsp;**while** True **do**
6. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Generate response token $y_t \sim \pi_\theta(\cdot \mid x, y + y_b)$
7. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Append $y_t$ to rollout sequence $y_b \leftarrow y_b + y_t$
8. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**if** $y_t$ in [`</search>`, `</answer>`, `<eos>`] **then break**
9. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**end if**
10. &nbsp;&nbsp;&nbsp;&nbsp;**end while**
11. &nbsp;&nbsp;&nbsp;&nbsp;$y \leftarrow y + y_b$
12. &nbsp;&nbsp;&nbsp;&nbsp;**if** `<search> </search>` detected in $y_b$ **then**
13. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Extract search query $q \leftarrow \text{Parse}(y_b, \text{<search>}, \text{</search>})$
14. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Retrieve search results $d = \mathcal{R}(q)$
15. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Insert $d$ into rollout $y \leftarrow y + \text{<information>}d\text{</information>}$
16. &nbsp;&nbsp;&nbsp;&nbsp;**else if** `<answer> </answer>` detected in $y_b$ **then**
17. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**return** final generated response $y$
18. &nbsp;&nbsp;&nbsp;&nbsp;**else**
19. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Ask for rethink $y \leftarrow y + \text{"My action is not correct. Let me rethink."}$
20. &nbsp;&nbsp;&nbsp;&nbsp;**end if**
21. &nbsp;&nbsp;&nbsp;&nbsp;Increment action count $b \leftarrow b + 1$
22. **end while**
23. **return** final generated response $y$



这段伪代码定义了一个让大语言模型（LLM）在生成回答时，能**动态、多轮调用搜索引擎**的核心流程：模型会根据输入问题逐步生成内容，当检测到“搜索指令”时自动调用搜索引擎获取信息，将信息融入上下文后继续推理，直到生成最终答案或达到最大尝试次数，全程保证推理和搜索的交错执行。

先明确关键符号/术语的含义，方便理解：
| 符号/术语 | 中文含义 |
|----------|----------|
| $x$ | 输入的用户查询（问题） |
| $\pi_\theta$ | 训练好的LLM策略模型（核心生成模型） |
| $\mathcal{R}$ | 搜索引擎（用于检索外部信息） |
| $B$ | 最大行动预算（最大允许的轮次/尝试次数） |
| $y$ | 最终生成的完整响应（包含推理、搜索、答案） |
| $y_b$ | 当前轮次LLM生成的临时内容 |
| $b$ | 已执行的行动轮次计数 |
| $y_t$ | LLM逐token生成的单个内容单元（如文字、指令令牌） |

---

#### 1. 前置定义（输入/输出）
```
**Require:** Input query $x$, policy model $\pi_\theta$, search engine $\mathcal{R}$, maximum action budget $B$.
**Ensure:** Final response $y$.
```
- 【输入要求】：需要准备4个核心要素——用户的查询问题$x$、LLM策略模型$\pi_\theta$、搜索引擎工具$\mathcal{R}$、最大行动预算$B$（防止无限循环）。
- 【输出保证】：最终会返回模型生成的完整响应$y$（包含推理过程、搜索信息、最终答案）。

#### 2. 初始化阶段
```
1. Initialize rollout sequence $y \leftarrow \emptyset$
2. Initialize action count $b \leftarrow 0$
```
- 第1行：初始化最终响应序列$y$为空（后续逐步拼接内容）。
- 第2行：初始化行动轮次计数器$b$为0（记录已执行的调用/推理轮次）。

#### 3. 主循环（控制最大轮次）
```
3. **while** $b < B$ **do**
```
- 核心循环条件：只要已执行轮次$b$小于最大预算$B$，就继续执行（避免模型无限尝试）。

#### 4. 单轮生成子流程
```
4.     Initialize current action LLM rollout sequence $y_b \leftarrow \emptyset$
5.     **while** True **do**
6.         Generate response token $y_t \sim \pi_\theta(\cdot \mid x, y + y_b)$
7.         Append $y_t$ to rollout sequence $y_b \leftarrow y_b + y_t$
8.         **if** $y_t$ in [`</search>`, `</answer>`, `<eos>`] **then break**
9.         **end if**
10.    **end while**
```
- 第4行：初始化当前轮次的临时生成序列$y_b$为空（存储本轮生成的内容）。
- 第5行：启动“逐token生成”的无限循环（直到触发终止条件）。
- 第6行：LLM基于“用户问题$x$ + 已生成的全部内容$y$ + 本轮临时内容$y_b$”，生成下一个token$y_t$（$\sim$表示“采样生成”）。
- 第7行：把新生成的token$y_t$拼接到本轮临时序列$y_b$中（逐步构建本轮内容）。
- 第8行：终止条件判断——如果生成的token是这三类之一（`</search>`：搜索指令结束、`</answer>`：答案结束、`<eos>`：生成结束），就停止本轮逐token生成。

#### 5. 拼接本轮内容到最终响应
```
11.    $y \leftarrow y + y_b$
```
- 把本轮生成的临时内容$y_b$（比如一段推理、一个搜索指令）拼接到最终响应$y$中。

#### 6. 分支判断（根据本轮内容执行不同逻辑）
##### 分支1：检测到搜索指令 → 调用搜索引擎
```
12.    **if** `<search> </search>` detected in $y_b$ **then**
13.        Extract search query $q \leftarrow \text{Parse}(y_b, \text{<search>}, \text{</search>})$
14.        Retrieve search results $d = \mathcal{R}(q)$
15.        Insert $d$ into rollout $y \leftarrow y + \text{<information>}d\text{</information>}$
```
- 第12行：如果本轮生成的$y_b$中包含`<search>`和`</search>`（搜索指令对），说明模型需要调用搜索引擎。
- 第13行：从$y_b$中解析出`<search>`和`</search>`之间的内容，作为搜索关键词$q$（比如用户问“2025年GDP数据”，模型生成`<search>2025年GDP官方数据</search>`，则$q$就是“2025年GDP官方数据”）。
- 第14行：调用搜索引擎$\mathcal{R}$，用关键词$q$检索得到结果$d$（比如相关网页、数据）。
- 第15行：把检索结果$d$用`<information>`和`</information>`包裹后，拼接到最终响应$y$中（让模型后续推理能用到这些外部信息）。

##### 分支2：检测到答案指令 → 返回最终结果
```
16.    **else if** `<answer> </answer>` detected in $y_b$ **then**
17.        **return** final generated response $y$
```
- 第16行：如果本轮生成的$y_b$中包含`<answer>`和`</answer>`（答案指令对），说明模型已完成推理，准备输出最终答案。
- 第17行：直接返回当前拼接好的完整响应$y$（流程结束）。

##### 分支3：无有效指令 → 提示重新思考
```
18.    **else**
19.        Ask for rethink $y \leftarrow y + \text{"My action is not correct. Let me rethink."}$
```
- 第18-19行：如果本轮生成的内容既没有搜索指令，也没有答案指令（说明模型推理出错/无有效行动），就在最终响应$y$中拼接“我的操作不正确，让我重新思考”，引导模型下一轮重新推理。

#### 7. 轮次计数与循环终止
```
20.    **end if**
21.    Increment action count $b \leftarrow b + 1$
22. **end while**
23. **return** final generated response $y$
```
- 第21行：本轮操作完成后，将行动轮次$b$加1（计数+1）。
- 第22行：如果$b$仍小于$B$，回到主循环继续；否则退出主循环。
- 第23行：若达到最大轮次$B$仍未生成答案，返回当前拼接的响应$y$（流程结束）。

#### 核心逻辑总结
1. **多轮交互**：模型不是一次性生成答案，而是分轮次推理，每轮可独立决定“调用搜索”“输出答案”或“重新思考”。
2. **搜索引擎集成**：通过`<search>`/`</search>`令牌触发搜索，检索结果用`<information>`封装后融入上下文，保证模型能利用外部信息。
3. **安全边界**：通过最大行动预算$B$防止无限循环，同时通过特定令牌（`</search>`/`</answer>`/`<eos>`）控制单轮生成的终止。
4. **容错机制**：当模型生成无意义内容时，主动提示“重新思考”，保证流程的鲁棒性。

简单来说，这段伪代码实现了“LLM推理→检测指令→调用搜索/输出答案/重新思考→融入信息继续推理”的闭环，是SEARCH-R1框架能实现“检索增强推理”的核心逻辑。


### 奖励模型

为训练 SEARCH-R1，作者采用纯基于规则的奖励系统，仅包含最终结果奖励，用于评估模型响应的正确性。例如，在事实推理任务中，可通过精确字符串匹配等基于规则的标准衡量正确性：
\[r_{\phi }(x,y)=EM(a_{pred},a_{gold})\]
其中 \(a_{pred }\) 是从响应 \(y\) 中提取的最终答案，\(a_{gold }\) 是真实答案（ground truth answer）。与 Guo 等人（2025）的研究不同，作者未引入格式奖励——因为所训练的模型已展现出极强的结构遵循能力，更复杂的格式奖励探索将留待未来研究。此外，作者遵循 Guo 等人（2025）的思路，避免训练神经奖励模型，这一决策主要基于两方面考量：一是大型语言模型（LLMs）在大规模强化学习中对特定奖励形式的敏感性，二是训练此类模型会带来额外的计算成本与复杂度。


### 实验设计

- 训练模型：
    - Qwen-2.5-3B（Base/Instruct 版本）
    - Qwen-2.5-7B（Base/Instruct 版本

- 检索环节：
    - 以 2018 年维基百科数据 dump（Karpukhin 等人，2020）作为知识源
    - 以 E5 模型（Wang 等人，2022）作为检索器
    - 将所有基于检索的方法的检索段落数量（top-k）均设置为 3 篇


### 训练难点

## 3 评测数据


## 4 个人思考

1. search-r1只是用了一种工具，有没有使用多种工具的agent训练场景？