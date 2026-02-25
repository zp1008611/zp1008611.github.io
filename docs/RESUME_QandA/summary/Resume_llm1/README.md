# llm面试问题总结

## NL2SQL

- 为什么要做难度分类？如何确定 sql 难度？配比率是怎么确定的？
  - 难度分类的核心目的是平衡训练数据的分布，避免模型因过度拟合简单样本而在复杂场景下泛化能力不足
  - 难度分级prompt
    - 简单：select 指定字段，where 简单条件，简单排序
    - 中等：简单基础上，加上聚合函数 Group By，范围查询 BETWEEN... AND，多表关联 JOIN
    - 复杂：子查询
  - 该配比通过多次微调测试得到，测试过的配比率有 5:3:2, 3:2:1, 4:4:2

- 只做有监督微调不行吗，为什么还需要使用强化学习微调？
  - SFT 依赖标注数据的分布，生成的回应受训练数据的影响，在nl2sql任务中，一个自然语言查询可能对应多个语法正确的SQL，但有部分SQL虽然能执行，却存在冗余字段和多余的关联，SFT仅能学到“学到符合训练数据模式”的SQL，却无法判断“哪个SQL更优”（如结果更匹配）。而 RL 通过奖励函数（如 “结果精准度”）可引导模型偏好更优解。

- 对于项目，只做有监督微调会出现什么情况？
  - 复杂查询容易失效：在处理多表连接、子查询等场景时，生成的 SQL 结构错误，比如多表连接，本来需要查询的字段来自表A，然后连接的表是表B，但是SFT给出的结果中，from和join后的表可能会调换

- 为什么不用 PPO 和 DPO，而是用GRPO？
  - PPO，DPO的数据构建需要有chosen response和rejected response，数据构造比较麻烦
  - PPO 需要同时训练策略模型（Actor）和价值模型（Critic），训练复杂度大，GRPO无需训练价值模型
  - PPO训练流程：
    - 采样一批prompt，用actor对每个prompt生成response，用奖励函数对reponse打分，得到奖励r
    - 用价值模型（Critic）预测当前 prompt 的状态价值，使用 GAE 计算优势值
    - 计算actor损失（希望actor产生更高奖励的response）和critic损失（希望critic的状态价值预测值更加准确）
    - 一般用神经网络表示actor和critic，使用反向传播更新actor和critic的参数
  - GRPO训练流程：
    - 从任务分布中采样一批 prompt，对每个 prompt，用 actor 生成 $N$ 个回复（$N \geq$ 2，形成 “回复组”）。用奖励模型对组内每个回复打分，得到奖励值 $r_1,r_2,\dots r_N$
    - 对每个回复组，计算组内平均奖励，计算每个回复的 “相对优势”
    - 计算actor损失
    - 一般用神经网络表示actor，使用反向传播更新actor的参数

  - PPO的奖励函数是根据对应的数据集训练得到的，一般用神经网络表示，损失函数为$-\log(\sigma(s_{w}-s_{l}))$，chosen response评分值-rejected response评分值，取sigmoid，再取-log，-log(sigma(d))是单调减函数，d为负数时，损失函数很大
  - GRPO的损失函数可以自定义
  
- 奖励函数是怎么设计的，为什么要这样设计？

  每个部分的奖励求和，然后加权

  1. 格式奖励（format，权重 1.0），评估目标：确保生成内容符合`<reasoning>`（推理过程）和`<sql>`（SQL 语句）的结构化格式，便于后续解析和执行。严格检查内容是否包含`<reasoning>...</reasoning>`和`<sql>...</sql>`标签。
  2. 推理质量奖励（reasoning，权重 0.7），评估目标：评估<reasoning>部分的合理性，鼓励模型生成逻辑清晰、步骤明确、关联数据库 schema 的推理过程。多因素评分：长度：推理内容越长（如 $\geq 50$ 词）得分越高（最高 0.2）；步骤性：包含 “第一步”“然后” 等步骤词得分更高（最高 0.15）；schema 关联：提及数据库中真实表名、列名越多，得分越高（最高 0.3）。
  3. SQL 正确性奖励（sql_correctness，权重 1.2），评估目标：评估生成 SQL 的语法正确性、执行有效性及结果与 “黄金 SQL”（参考标准答案）的一致性。执行成功，给予基础奖励，比较两者的查询结果（行数、列名、数据内容）：完全匹配：最高奖励；部分匹配：通过行列交集比例计算内容相似度，按比例给予奖励。若执行报错，根据错误类型给分，比如语法错误奖励为0，但是数据格式错误，则给0.2奖励，因为可能只是传的数值有问题，语法没问题

- 评价指标分数是怎么计算的？

  1. 等价匹配：两个sql结构等价，则EM为1，所有sql的EM求平均数为总EM
  2. 执行匹配：两个sql执行结果是否匹配，完全匹配 EX为1，不完全匹配按重合度计算，所有sql的EX求平均数为总EX
  3. 总score为0.3* EM + 0.7* EX

- 有监督微调的训练数据是什么？
  - {"prompt":xxxx,"sql":xxx}

- GRPO微调的训练数据是什么？
  - 试了两种，sft训练数据中生成结果评分较低对应的数据，sft训练数据，我做的选择数据集大小较小的，加快训练速度

- 有监督微调的prompt怎么写的？
  - 角色设定：sql大师，根据给定的查询给出对应的sql代码
  - 输出格式要求：输出sql

- GRPO的prompt怎么写的？
  - 角色设定：sql大师，根据给定的查询给出对应的sql代码
  - 示例：cot示例，三个难度各一个示例
  - 输出格式要求：推理包含在reasoning标签中，sql包含在sql标签中

- 有监督微调的训练时间大概多少？
  - 单机8卡，48小时

- GRPO的训练时间大概多少？
  - 单机8卡，56小时

- 介绍 有哪些提示词工程技术？
  - cot



- Qwen2.5-Coder-7B-Instruct的特点？模型结构以及是怎么训练的？与其他qwen系列模型的区别是什么？
- Qwen3-8B的特点？模型结构以及是怎么训练的？与其他qwen系列模型的区别是什么？


## 天池

- RAG的流程
- 介绍 Jina-Embeddings-v2，模型结构以及是怎么训练的？还有使用其他文本嵌入模型吗？
  - sentence-bert
      - 输入：两个sentence
      - 结构：双塔模型，共享参数，bert->pooling->u, bert->pooling-v, 
      - output：
          - 分类型：softmax(u,v,|u-v|)，训练数据：{(s_a1,s_b1,-1),(s_a2,s_b2,1),...}，1是相关，-1是不相关，优化损失函数是交叉熵
          - 回归型：余弦相似度(u,v)，训练数据：{(s_a1,s_b1,余弦相似度),(s_a2,s_b2,余弦相似度),...}，优化损失函数是均方根误差
          

  - jina-embedding-v1
      - 二元训练；子网络初始化为T5；损失函数
      - 三元组训练；子网络初始化为二元训练后的模型；损失函数

  - jina-embedding-v2
      - 预训练修改后的 BERT；注意力机制修改为 ALiBi 注意力机制，使模型能处理长序列；损失函数：
      - 二元训练；子网络初始化为修改后的bert；损失函数：
      - 三元组训练；子网络初始化为二元训练后的模型；损失函数：

- 向量库使用的是什么？与其他向量库的区别？
- 有什么方法创建向量索引？
- 密集检索与稀疏检索、混合检索的区别
- 介绍一下 Colpali，模型结构以及是怎么训练的？
- 提示词是怎么写的？
- Qwen2.5-VL 的特点？模型结构以及是怎么训练的？与其他多模态模型的区别是什么？


## agent

- 每个agent的输入和输出是什么？


各模块通过 LangGraph 的工作流定义形成有序执行逻辑，核心是 “生成 - 分析 - 优化 - 迭代” 的闭环，具体流程如下：

1. 初始启动：工作流从 task_generation_node（任务生成）开始，作为入口点。
2. 单向流程（首次执行）：
    - task_generation_node → task_dependency_node：生成任务后，立即分析任务依赖；
    - task_dependency_node → task_scheduler_node：基于依赖生成初始进度计划；
    - task_scheduler_node → task_allocation_node：根据进度计划分配团队成员；
    - task_allocation_node → risk_assessment_node：评估当前计划的风险。
3. 迭代优化（循环流程）：
    - risk_assessment_node → router（路由节点）：风险评估后，由路由节点判断是否继续优化；
        - 若未达最大迭代次数：路由到insight_generation_node（生成优化建议）；
        - 若达到最大迭代次数或风险已显著降低：路由到END（终止流程）；否则回到insight_generation_node
    - insight_generator → task_scheduler_node：生成优化建议后，回到进度计划节点，基于建议重新调度任务，开始下一轮迭代（重复 “调度→分配→风险评估→路由” 流程）。

- tasks : List, [(任务编号,任务名称，任务描述，完成该任务需要的时间),...]
- dependencies ：List，[(任务A，[任务A完成后才可开始的任务B，任务A完成后才可开始的任务C])]
- schedule : List, [(任务，任务开始时间，任务结束时间)]
- task_allocations: List, [(任务，任务所分配的人员)]
- risks: List, [(任务，风险评分)]
- project_risk_score：int，项目风险评分
- insight_generator：string，项目改进建议



- 介绍一下每一个模块的prompt怎么写的？

  - 输入
    - 项目描述：比如我要做一个关于宠物店预约管理的app，工期是1个月
    - 人员情况：产品策划，前端，后端

  - 任务生成agent：根据给定的项目描述，提取出可执行、现实的任务，并按照工期估计任务执行的大概天数；若任务超过5天，需拆分为更小的独立子任务

  - 依赖关系分析agent：为每个任务确定“必须先完成的前置任务”以及“依赖该任务完成得后续任务”

  - 任务调度节点：基于任务、依赖、历史洞察和之前的调度，为每个任务分配开始/结束天数（需尊重依赖）；

  - 任务分配节点：根据任务、调度、团队成员技能和可用性分配任务；确保成员无重叠任务，平衡工作量；遵循“一人一次一任务”约束，利用历史洞察优化分配。


  - 风险评估节点：分析当前分配、调度和风险，识别改进点（如瓶颈、资源冲突、高风险任务）；给予风险评分（0-10）；
  
  - 提供建议节点：给予分配建议，并回到任务调度节点

  - router节点：若未达最大迭代次数：路由到insight_generation_node（生成优化建议）；若达到最大迭代次数或风险已显著降低：路由到END（终止流程）；否则回到insight_generation_node

  - 输出：字典对象，键是“任务”，值是列表[任务执行者，开始时间，结束时间]








## 八股

- 介绍一下有什么优化器？
- 模型参数如何计算？
- 模型训练/推理显存如何计算？
- Lora训练显存占用分析
- 大模型训练节约显存的方法？
- 介绍 LoRa，LoRa 的参数是怎么选的？
- 介绍 DeepSpeed，介绍 Deepspeed ZeRO-1，ZeRO-2，ZeRO-3
- 介绍 transformer，和 rnn，cnn的区别
- 介绍 Tokenizer 方法
- 手撕 BPE
- 介绍 embedding 方法
- 介绍 位置编码方法，固定位置编码（正余弦绝对位置编码），相对位置编码（旋转位置编码 RoPE）
- 介绍 残差连接
- 介绍 batch normalize， layer normlize，
- mask 的作用
- 激活函数有哪些？范围是多少？导数是多少？
- 什么是梯度消失？
- 哪些激活函数容易出现梯度消失的情况？
- lstm，transformer如何解决梯度消失的问题？
- 损失函数有哪些？
  - 对比学习
    - InfoNCE loss
    - Contrastive Loss
  - 三元loss
    - Triplet Loss
  - 回归
    - RMSE
  - 分类
    - cross entropy
- transformer decoding 方法有哪些？
- 手撕 beam search
- 如何缓解LLM复读机现象？
- 介绍 deepseek 系列模型，模型结构以及是怎么训练的？
- 介绍 MOE 模型，和 dense模型的区别
- 简述 PPO，DPO，GRPO
- 介绍 Qwen 系列模型，模型结构以及是怎么训练的？
- 为什么大部分大模型是 decoder-only?
- 介绍 CLIP，BLIP-2，LLAVA，Qwen-VL，Qwen2.5-VL模型结构以及是怎么训练的？
  - Qwen-VL: 先冻大模型，对齐编码器；全部解冻，多任务训练；冻编码器，有监督微调大模型
- 手撕 PPO，DPO，GRPO 的 loss
- 手撕 MHA，MLA，GQA
- 手撕 MOE
- 什么是 agent？
  - agent = 大模型+planning+memory+工具使用
- Agent Memory
- Agent Planning
- A2A，ADK，MCP
- Function calling 是如何训练的？
