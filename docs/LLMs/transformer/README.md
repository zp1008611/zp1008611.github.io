# Transformer


## Reference

- https://web.stanford.edu/~jurafsky/slp3/9.pdf
- https://spaces.ac.cn/archives/8231
- https://spaces.ac.cn/archives/8265


![alt text](image-1.png)

## Tokenization（分词）

- Tokenization是将一个整体（例如词、短语、句子、段落甚至语音、图像）分割成较小单位（被称为token）的过程.

- 中文分词难点：分词标准，切分歧义，未登录词（OOV，Out of Vocabulary 新词）

- Tokenization算法类型： word-based、character-based、subword-based.
    - Word-based：将文本按自然语言中的 “词” 进行分割，通常以空格、标点符号或特定分隔符作为分词边界. 例如英语中按空格分割，汉语则需要专门的分词工具（如 jieba）. 
        - “I love natural language processing” $\leftarrow$ ["I", "love", "natural", "language", "processing"]
        - 词级单位保留完整语义，但词汇表庞大，未登录词（OOV）问题突出
    - Character-based：将文本拆解为最小字符单元，每个字符（包括标点、空格）作为独立 token. 例如：
        - “Hello!” $\leftarrow$ ["H", "e", "l", "l", "o", "!"]
        - 词汇表极小，无 OOV 问题，但丢失词级语义
    - Subword-base：介于词与字符之间的折中方案，将词拆分为有意义的子词单元（如前缀、后缀、词根），平衡词汇表大小与语义保留. 
        - BPE（Byte Pair Encoding）
        - BBPE
        - WordPiece
        - Unigram
- GPT2使用BBPE，Bert使用WordPiece

### BPE

BPE核心逻辑是：  
**从字符级别开始，通过迭代合并高频相邻字符对，逐步构建更有语义的子词单元**，最终平衡词汇表大小与语义表达能力. 


**初始化：字符级分割与频率统计**
 
- **示例**：  
  假设语料中包含词：*“low”, “lower”, “new”, “newest”*  
  初始分割后：  
  ```
  low → l o w </w>  
  lower → l o w e r </w>  
  new → n e w </w>  
  newest → n e w e s t </w>
  ```  
  统计相邻字符对频率：  
  - (“l”, “o”): 2次（来自“low”和“lower”）  
  - (“o”, “w”): 2次  
  - (“w”, “</w>”): 1次  
  - (“w”, “e”): 1次（来自“lower”）  
  - (“e”, “r”): 1次  
  - (“n”, “e”): 2次（来自“new”和“newest”）  
  - (“e”, “w”): 2次  
  - (“w”, “e”): 1次（来自“newest”）  
  - …（其他低频对）

**迭代合并：高频字符对升级为子词**
- **核心规则**：每次选择**出现频率最高的字符对**，将其合并为一个新的子词单元，并更新词表和频率统计.   
- **示例（第一次迭代）**：  
  最高频对为(“l”, “o”)和(“n”, “e”)（均2次），假设先合并(“l”, “o”) → 新子词“lo”.   
  合并后词表更新：  
  ```
  low → lo w </w>  
  lower → lo w e r </w>  
  new → n e w </w>  
  newest → n e w e s t </w>
  ```  
  重新统计字符对频率：  
  - (“lo”, “w”): 2次（来自“low”和“lower”）  
  - (“w”, “</w>”): 1次  
  - (“w”, “e”): 1次  
  - (“e”, “r”): 1次  
  - (“n”, “e”): 2次  
  - (“e”, “w”): 2次  
  - (“w”, “e”): 1次  
  - …  
- **第二次迭代**：最高频对为(“n”, “e”)和(“e”, “w”)（均2次），合并(“n”, “e”) → “ne”.   
  词表更新为：  
  ```
  new → ne w </w>  
  newest → ne w e s t </w>
  ```  
  继续此过程，直到达到预设的迭代次数或词汇表大小. 


**形式化定义**
- 设初始词表为字符集合 $V_0 = \{c_1, c_2, ..., c_n, </w>\}$，  
- 第 $k$ 次合并后的词表为 $V_k$，  
- 合并操作 $\text{merge}(V_{k-1})$ 选择频率最高的字符对 $(a, b) \in V_{k-1} \times V_{k-1}$，生成新子词 $ab$，并更新 $V_k = V_{k-1} \cup \{ab\}$. 


**BPE算法流程**
1. **计算初始词表**：先把训练语料分成最小单元（英文中26个字母加上各种符号以及常见中文字符），这些作为初始词表.   
2. **构建频率统计**：统计所有子词单元对（bigram，即两个连续的子词）在文本中的出现频率.   
3. **合并频率最高的子词对**：合并出现频率最高的子词对，并更新词汇表和`merge rule`.   
4. **重复合并步骤**：不断重复步骤 2 和步骤 3，直到达到预定的词汇表大小、合并次数，或者直到不再有有意义的合并（即，进一步合并不显著提高词汇表的效益）.   
5. **分词**：使用最终得到的`merge rule`对文本进行分词. 

BPE分词流程：
![alt text](image.png)

### Word-Piece

计算过程绝大部分与BPE一致，将挑选bigram的指标从频率换成了PMI（点互信息，[Pointwise Mutual Information](https://en.wikipedia.org/wiki/Pointwise_mutual_information)）：  

$$ \text{PMI}(a, b) = \frac{P(a, b)}{P(a)P(b)} $$  
其中 $a$、$b$ 为相邻的subword.   

当 PMI 值较高时，表示 $a$ 和 $b$ 在一起出现的频率远高于它们各自独立出现的概率，说明它们之间的关联较强，可能是一个有意义的组合.   


**Word-Piece算法过程**  
1. **计算初始词表**：通过训练语料获得，或初始为英文26个字母 + 符号 + 常见中文字符，作为初始词表.   
2. **计算合并分数（PMI）**：对训练语料拆分的子词单元，按合并规则计算两两子词的PMI分数.   
3. **合并分数最高的子词对**：选择PMI最高的子词对，合并为新子词单元，更新词表.   
4. **重复合并步骤**：循环执行步骤2 - 3，直到达到预定词表大小、合并次数，或无意义合并（合并无法显著提升词表效益）.   
5. **分词**：用最终词汇表对文本分词（对比BPE，直接依赖词汇表匹配分词 ）. 


**Word-Piece分词流程**：

正向最大匹配法（Forward Maximum Matching, FMM）

原理：从左到右扫描句子，尽可能匹配最长的词语.   

步骤：
1. 设置一个最大词长（如6）.   
2. 从句子的起始位置开始，取最大词长的子串，与词汇表匹配.   
3. 如果匹配成功，则切分该词，继续处理剩余部分；否则，缩短词长，继续匹配.   
4. 重复上述步骤，直到句子全部切分完毕. 

### Unigram

## Embedding

- onehot

- word2vec
    - CBOW
    - skip-gram



## 多头注意力（MHA）



![alt text](image-2.png)


## 位置编码（Positional Encoding）

- 绝对位置编码
    - 固定的正余弦位置编码

- 相对位置编码
    - 旋转位置编码 

## 掩码（Mask）


## Normalization

## 解码（Decoding）