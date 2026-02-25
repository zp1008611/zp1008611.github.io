# Search-R1

## Reference

- **论文链接**: [arXiv:2503.09516](https://arxiv.org/abs/2503.09516v5)
- **代码仓库**: [GitHub - PeterGriffinJin/Search-R1](https://github.com/PeterGriffinJin/Search-R1)


## 1 SEARCH-R1的训练目的

SEARCH-R1 是基于强化学习（RL）设计的大语言模型（LLM）训练框架，其核心训练目的是解决现有模型在“推理+外部知识检索”任务中的核心痛点，让LLM能够**自主、高效地结合实时搜索引擎进行分步推理**，具体可拆解为以下3个目标：

### 1. 让LLM掌握“何时搜索、如何搜索”的自主决策能力

现有依赖提示词（Prompting）的检索增强方法（如IRCoT、Search-o1），仅通过固定指令引导LLM调用搜索引擎，无法让模型自主判断“是否需要搜索”“搜索什么内容”“何时停止搜索”。SEARCH-R1通过RL训练，让LLM在推理过程中动态决策：

- 当内部知识不足时，自动生成有效搜索查询（包裹在`<search>`标签中）；  
- 当检索到外部信息后，结合新信息继续推理，避免冗余搜索或无效搜索；  
- 当信息足够时，停止搜索并输出最终答案（包裹在`</think>`标签中）。

例如在案例研究中，面对“Chris Jericho和Gary Barlow的共同职业”这一问题，SEARCH-R1先搜索两人职业，发现“musician”是交集后停止搜索，而非机械重复调用引擎。

### 2. 解决“检索-推理”过程的稳定性与优化难题

传统RL方法应用于“搜索+推理”场景时，存在两大障碍： 

- **检索内容的非可微性**：搜索引擎返回的外部文本（如Wikipedia片段）不属于LLM生成内容，直接参与RL优化会导致训练不稳定；  
- **多轮交互的轨迹优化**：LLM推理与搜索调用的 interleaved（交织）轨迹难以通过端到端梯度下降优化。  

SEARCH-R1通过“检索token掩码（Retrieved Token Masking）”解决这一问题：仅对LLM生成的推理文本、搜索查询进行RL损失计算，屏蔽检索到的外部文本（包裹在`<information>`标签中）的优化，确保训练过程稳定。同时，其支持PPO、GRPO等RL算法，通过多轮轨迹采样优化推理策略。

### 3. 以极简奖励函数实现高效泛化，摆脱对大规模标注数据的依赖

现有工具调用类方法（如Toolformer）需依赖大规模人工标注的“搜索-推理轨迹”训练模型，成本高且泛化性差；而SEARCH-R1采用**纯结果导向的奖励函数**（如精确匹配EM），仅根据最终答案的正确性反馈奖励，无需标注中间推理步骤： 

- 例如在事实问答任务中，奖励函数直接计算模型输出答案与标准答案的EM值（公式：$r_{\phi }(x,y)=EM(a_{pred},a_{gold})$）；  
- 这种设计让模型无需依赖任务特定标注，即可在7个问答数据集（涵盖通用QA、多跳QA）上泛化，且性能显著优于依赖标注的监督微调（SFT）方法。


## 2 SEARCH-R1与RAG的核心区别

RAG（Retrieval-Augmented Generation，检索增强生成）是传统的“检索+生成”框架，而SEARCH-R1是基于RL优化的“自主推理+动态检索”框架，二者在核心设计、交互逻辑、优化目标等维度存在本质差异，具体对比如下：

| 对比维度                | RAG（传统检索增强生成）                                                                 | SEARCH-R1（RL驱动的搜索-推理框架）                                                      |
|-------------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| **检索触发机制**        | 静态触发：仅在生成前基于**初始输入**（如用户问题）进行1轮检索，检索结果一次性传入LLM上下文。 | 动态触发：LLM在**分步推理中自主触发多轮检索**，根据当前推理状态决定是否搜索（如发现知识缺口时生成`<search>`标签）。 |
| **检索策略灵活性**      | 固定策略：检索查询由初始输入直接生成，无法根据推理过程调整（如多跳问题中无法生成中间查询）。 | 自适应策略：LLM可生成多轮不同查询，逐步补全知识（如先搜“Curious香水所属歌手”，再搜“该歌手出生地”）。 |
| **优化方式**            | 无显式优化：检索器与生成器多为独立模块，仅通过“检索结果拼接上下文”提升生成质量，无端到端优化。 | RL端到端优化：通过PPO/GRPO优化“推理-检索”完整轨迹，目标是最大化最终答案正确率（结果导向奖励）。 |
| **对检索内容的处理**    | 被动接收：检索结果全部传入上下文，LLM被动使用，可能包含冗余/无关信息，影响生成精度。       | 主动筛选与屏蔽：仅使用相关检索结果，且通过“检索token掩码”排除外部文本的优化干扰，避免训练不稳定。 |
| **推理与检索的交互逻辑**| 串行流程：“检索→生成”线性执行，无交织（检索完成后才开始生成，生成中无法补充检索）。       | 交织流程：“推理→搜索→再推理→再搜索”循环，检索结果实时融入推理过程（如检索到Britney Spears信息后，立即基于该信息继续分析出生地）。 |
| **泛化能力与标注依赖**  | 依赖任务适配：需针对不同任务调整检索器参数（如多跳QA需特殊检索策略），部分变体依赖标注数据。 | 低标注依赖+高泛化：仅用结果导向奖励（无需中间标注），在通用QA、多跳QA等7个数据集上均优于RAG，且跨数据集泛化性强。 |
| **性能提升核心来源**    | 依赖“检索结果的相关性”：性能上限由检索器精度决定（如E5、DPR的检索召回率）。               | 依赖“自主决策的有效性”：性能提升来自LLM对“何时搜、搜什么”的判断优化，即使使用与RAG相同的检索器（如E5），性能仍提升20%-24%。 |


### 关键差异示例
以“Curious香水所属歌手的出生地”这一问题为例，二者的处理流程差异如下：
1. **RAG的处理流程**：  
   - 步骤1：基于初始问题“Curious香水所属歌手的出生地”生成检索查询；  
   - 步骤2：检索器返回相关文档（可能包含香水信息、歌手信息）；  
   - 步骤3：LLM基于“问题+所有检索结果”一次性生成答案，若检索结果未明确歌手出生地，则生成错误答案（如误判歌手为Beyoncé）。

2. **SEARCH-R1的处理流程**：  
   - 步骤1：LLM推理“需先确定Curious香水所属歌手”，生成`<search> Curious fragrance information </search>`；  
   - 步骤2：检索到“Britney Spears是该香水代言人”，LLM继续推理“需确定Britney的出生地”，生成`<search> Britney Spears birthplace </search>`；  
   - 步骤3：检索到“Britney出生于密西西比州McComb”，LLM验证信息后停止搜索，输出正确答案。  

可见，RAG的“1轮检索”无法应对需要多步知识补全的问题，而SEARCH-R1的“动态多轮检索”能自主拆解问题，逐步补全知识缺口。


### 总结
- **核心定位差异**：RAG是“工具级”的检索辅助工具，解决“LLM缺乏外部知识”的基础问题；SEARCH-R1是“智能体级”的自主推理框架，解决“LLM如何高效使用检索工具”的高阶问题。  
- **性能优势来源**：RAG的性能依赖检索器精度，而SEARCH-R1的性能依赖RL优化的“决策智能”——让LLM学会“聪明地搜索”，而非“被动地使用搜索结果”，因此在复杂推理任务（如多跳QA）上优势更显著（如在HotpotQA数据集上，SEARCH-R1比RAG性能提升45%+）。



## 3 训练方法


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

```bash
1. Initialize rollout sequence $y \leftarrow \emptyset$
2. Initialize action count $b \leftarrow 0$
```

- 第1行：初始化最终响应序列$y$为空（后续逐步拼接内容）。
- 第2行：初始化行动轮次计数器$b$为0（记录已执行的调用/推理轮次）。

#### 3. 主循环（控制最大轮次）

```bash
3. **while** $b < B$ **do**
```

- 核心循环条件：只要已执行轮次$b$小于最大预算$B$，就继续执行（避免模型无限尝试）。

#### 4. 单轮生成子流程

```bash
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

```bash
11.    $y \leftarrow y + y_b$
```

- 把本轮生成的临时内容$y_b$（比如一段推理、一个搜索指令）拼接到最终响应$y$中。

#### 6. 分支判断（根据本轮内容执行不同逻辑）

##### 分支1：检测到搜索指令 → 调用搜索引擎

```bash
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

```bash
16.    **else if** `<answer> </answer>` detected in $y_b$ **then**
17.        **return** final generated response $y$
```

- 第16行：如果本轮生成的$y_b$中包含`<answer>`和`</answer>`（答案指令对），说明模型已完成推理，准备输出最终答案。
- 第17行：直接返回当前拼接好的完整响应$y$（流程结束）。

##### 分支3：无有效指令 → 提示重新思考

```bash
18.    **else**
19.        Ask for rethink $y \leftarrow y + \text{"My action is not correct. Let me rethink."}$
```

- 第18-19行：如果本轮生成的内容既没有搜索指令，也没有答案指令（说明模型推理出错/无有效行动），就在最终响应$y$中拼接“我的操作不正确，让我重新思考”，引导模型下一轮重新推理。

#### 7. 轮次计数与循环终止

```bash
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

$$
r_{\phi }(x,y)=EM(a_{pred},a_{gold})
$$

其中 $a_{pred }$ 是从响应 $y$ 中提取的最终答案，$a_{gold }$ 是真实答案（ground truth answer）。与 Guo 等人（2025）的研究不同，作者未引入格式奖励——因为所训练的模型已展现出极强的结构遵循能力，更复杂的格式奖励探索将留待未来研究。此外，作者遵循 Guo 等人（2025）的思路，避免训练神经奖励模型，这一决策主要基于两方面考量：一是大型语言模型（LLMs）在大规模强化学习中对特定奖励形式的敏感性，二是训练此类模型会带来额外的计算成本与复杂度。


### 实验设计

- 训练模型：
    - Qwen-2.5-3B（Base/Instruct 版本）
    - Qwen-2.5-7B（Base/Instruct 版本

- 检索环节：
    - 以 2018 年维基百科数据 dump（Karpukhin 等人，2020）作为知识源
    - 以 E5 模型（Wang 等人，2022）作为检索器
    - 将所有基于检索的方法的检索段落数量（top-k）均设置为 3 篇


### 训练难点

## 4 评测数据


## 5 个人思考

1. search-r1只是用了一种工具，有没有使用多种工具的agent训练场景？