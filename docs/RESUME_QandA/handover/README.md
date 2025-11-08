# 八股手撕

## MHA（Multi-Head Attention）

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class MultiHeadAttention(nn.Module):
    """
    Multi-Head Attention 实现
    
    Args:
        d_model: 模型维度
        num_heads: 注意力头数
        dropout: dropout 概率
    """
    def __init__(self, embed_dim, num_heads):
        super(MultiHeadAttention, self).__init__()
        
        self.embed_dim = embed_dim  # 模型维度，如 512
        self.num_heads = num_heads  # 头数，如 8
        self.head_dim = embed_dim // num_heads  # 每个头的维度，如 64
        self.W_Q = nn.Linear(embed_dim, embed_dim)  
        self.W_K = nn.Linear(embed_dim, embed_dim)
        self.W_V = nn.Linear(embed_dim, embed_dim)
        self.W_O = nn.Linear(embed_dim, embed_dim)
        
        
    def forward(self, query, key, value, mask=None):
        """
        前向传播
        
        Args:
            query: (batch_size, seq_len_q, d_model)
            key:   (batch_size, seq_len_k, d_model)
            value: (batch_size, seq_len_v, d_model)  # seq_len_k == seq_len_v
            mask:  (batch_size, 1, seq_len_q, seq_len_k) 或 None
                   用于屏蔽某些位置（如 padding、future tokens）
        
        Returns:
            output: (batch_size, seq_len_q, d_model)
            attention_weights: (batch_size, num_heads, seq_len_q, seq_len_k)
        """
        batch_size,seq_len,_ = query.size()
        
        Q = self.W_Q(query)  # (batch_size, seq_len_q, d_model)
        K = self.W_K(key)    # (batch_size, seq_len_k, d_model)
        V = self.W_V(value)  # (batch_size, seq_len_v, d_model)
        
        Q = Q.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = K.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = V.view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim)
        
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        
        attention_weights = F.softmax(scores, dim=-1)
        context = torch.matmul(attention_weights, V)
        context = context.transpose(1, 2).contiguous().view(
            batch_size, -1, self.head_dim
        )
        output = self.W_O(context) 
        
         return output
```

---

## PPO 损失函数

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class PPOLoss(nn.Module):
    def __init__(self, clip_epsilon=0.2, value_coef=0.5, entropy_coef=0.01):
        super().__init__()
        self.clip_epsilon = clip_epsilon
        self.value_coef = value_coef
        self.entropy_coef = entropy_coef
    
    def forward(self, log_probs_new, log_probs_old, advantages, 
                values_new, returns):
        # Ratio
        ratio = torch.exp(log_probs_new - log_probs_old)
        
        # Policy loss
        surr1 = ratio * advantages
        surr2 = torch.clamp(ratio, 1 - self.clip_epsilon, 
                           1 + self.clip_epsilon) * advantages
        policy_loss = -torch.min(surr1, surr2).mean()
        
        # Value loss
        value_loss = F.mse_loss(values_new, returns)
        
        # Total loss
        total_loss = policy_loss + self.value_coef * value_loss
        
        return total_loss
```

---

## GAE（Generalized Advantage Estimation）

### 核心公式

$$
\hat{A}_t^{\text{GAE}(\gamma, \lambda)} = \sum_{l=0}^{\infty} (\gamma \lambda)^l \delta_{t+l}^V
$$

其中 TD 误差：
$$
\delta_t^V = r_t + \gamma V(s_{t+1}) - V(s_t)
$$

**展开形式**：
$$
\hat{A}_t = \delta_t + (\gamma\lambda)\delta_{t+1} + (\gamma\lambda)^2\delta_{t+2} + \cdots
$$

**参数说明**：
- $\gamma$：折扣因子（discount factor），通常 0.99
- $\lambda$：GAE 参数，控制偏差-方差权衡，通常 0.95
  - $\lambda=0$：只用 1-step TD，低方差但高偏差
  - $\lambda=1$：完整 Monte Carlo，低偏差但高方差

**递归计算**（从后往前）：
$$
\hat{A}_t = \delta_t + (\gamma\lambda)(1 - \text{done}_t) \hat{A}_{t+1}
$$

---

### 代码实现

```python
import torch
# ==================== 简化版本（面试推荐） ====================

class GAE:
    def __init__(self, gamma=0.99, lam=0.95):
        self.gamma = gamma
        self.lam = lam
    
    def __call__(self, rewards, values, dones):
        """
        rewards: (T,) 奖励序列
        values: (T,) 价值估计
        dones: (T,) 终止标志
        """
        T = len(rewards)
        advantages = torch.zeros_like(rewards)
        last_gae = 0
        
        for t in reversed(range(T)):
            next_value = 0 if t == T - 1 else values[t + 1]
            delta = rewards[t] + self.gamma * next_value * (1 - dones[t]) - values[t]
            last_gae = delta + self.gamma * self.lam * (1 - dones[t]) * last_gae
            advantages[t] = last_gae
        
        returns = advantages + values
        return advantages, returns
```

---

## Transformer Decoder Block

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        
        self.W_Q = nn.Linear(embed_dim, embed_dim)
        self.W_K = nn.Linear(embed_dim, embed_dim)
        self.W_V = nn.Linear(embed_dim, embed_dim)
        self.W_O = nn.Linear(embed_dim, embed_dim)
    
    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)
        seq_len_q = query.size(1)
        seq_len_k = key.size(1)
        
        # Linear projections
        Q = self.W_Q(query).view(batch_size, seq_len_q, self.num_heads, self.head_dim).transpose(1, 2)
        K = self.W_K(key).view(batch_size, seq_len_k, self.num_heads, self.head_dim).transpose(1, 2)
        V = self.W_V(value).view(batch_size, seq_len_k, self.num_heads, self.head_dim).transpose(1, 2)
        
        # Scaled dot-product attention
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim)
        
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        
        attention_weights = F.softmax(scores, dim=-1)
        context = torch.matmul(attention_weights, V)
        
        # Concatenate heads
        context = context.transpose(1, 2).contiguous().view(batch_size, seq_len_q, self.embed_dim)
        output = self.W_O(context)
        
        return output


class PositionwiseFeedForward(nn.Module):
    def __init__(self, embed_dim, ff_dim, dropout=0.1):
        super().__init__()
        self.fc1 = nn.Linear(embed_dim, ff_dim)
        self.fc2 = nn.Linear(ff_dim, embed_dim)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        return self.fc2(self.dropout(F.relu(self.fc1(x))))


class DecoderBlock(nn.Module):
    """
    Transformer Decoder Block
    
    包含三个主要部分：
    1. Masked Multi-Head Self-Attention
    2. Multi-Head Cross-Attention (与 Encoder 输出交互)
    3. Position-wise Feed-Forward Network
    
    Args:
        embed_dim: 嵌入维度 (如 512)
        num_heads: 注意力头数 (如 8)
        ff_dim: 前馈网络隐藏层维度 (如 2048)
        dropout: dropout 概率
    """
    def __init__(self, embed_dim, num_heads, ff_dim, dropout=0.1):
        super().__init__()
        
        # Masked Self-Attention
        self.self_attention = MultiHeadAttention(embed_dim, num_heads)
        self.norm1 = nn.LayerNorm(embed_dim)
        self.dropout1 = nn.Dropout(dropout)
        
        # Cross-Attention
        self.cross_attention = MultiHeadAttention(embed_dim, num_heads)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.dropout2 = nn.Dropout(dropout)
        
        # Feed-Forward
        self.feed_forward = PositionwiseFeedForward(embed_dim, ff_dim, dropout)
        self.norm3 = nn.LayerNorm(embed_dim)
        self.dropout3 = nn.Dropout(dropout)
    
    def forward(self, x, encoder_output, src_mask=None, tgt_mask=None):
        """
        Args:
            x: decoder 输入 (batch_size, tgt_seq_len, embed_dim)
            encoder_output: encoder 输出 (batch_size, src_seq_len, embed_dim)
            src_mask: source mask for cross-attention (batch_size, 1, 1, src_seq_len)
            tgt_mask: target mask for self-attention (batch_size, 1, tgt_seq_len, tgt_seq_len)
                      通常是下三角矩阵，防止看到未来信息
        
        Returns:
            output: (batch_size, tgt_seq_len, embed_dim)
        """
        # 1. Masked Self-Attention + Residual + Norm
        self_attn_output = self.self_attention(x, x, x, mask=tgt_mask)
        x = self.norm1(x + self.dropout1(self_attn_output))
        
        # 2. Cross-Attention + Residual + Norm
        cross_attn_output = self.cross_attention(x, encoder_output, encoder_output, mask=src_mask)
        x = self.norm2(x + self.dropout2(cross_attn_output))
        
        # 3. Feed-Forward + Residual + Norm
        ff_output = self.feed_forward(x)
        x = self.norm3(x + self.dropout3(ff_output))
        
        return x
```

---

## Transformer Encoder Block

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_dim, num_heads):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        
        self.W_Q = nn.Linear(embed_dim, embed_dim)
        self.W_K = nn.Linear(embed_dim, embed_dim)
        self.W_V = nn.Linear(embed_dim, embed_dim)
        self.W_O = nn.Linear(embed_dim, embed_dim)
    
    def forward(self, query, key, value, mask=None):
        batch_size = query.size(0)
        seq_len = query.size(1)
        
        # Linear projections
        Q = self.W_Q(query).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        K = self.W_K(key).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        V = self.W_V(value).view(batch_size, seq_len, self.num_heads, self.head_dim).transpose(1, 2)
        
        # Scaled dot-product attention
        scores = torch.matmul(Q, K.transpose(-2, -1)) / math.sqrt(self.head_dim)
        
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        
        attention_weights = F.softmax(scores, dim=-1)
        context = torch.matmul(attention_weights, V)
        
        # Concatenate heads
        context = context.transpose(1, 2).contiguous().view(batch_size, seq_len, self.embed_dim)
        output = self.W_O(context)
        
        return output


class PositionwiseFeedForward(nn.Module):
    def __init__(self, embed_dim, ff_dim, dropout=0.1):
        super().__init__()
        self.fc1 = nn.Linear(embed_dim, ff_dim)
        self.fc2 = nn.Linear(ff_dim, embed_dim)
        self.dropout = nn.Dropout(dropout)
    
    def forward(self, x):
        return self.fc2(self.dropout(F.relu(self.fc1(x))))


class EncoderBlock(nn.Module):
    """
    Transformer Encoder Block
    
    包含两个主要部分：
    1. Multi-Head Self-Attention
    2. Position-wise Feed-Forward Network
    
    Args:
        embed_dim: 嵌入维度 (如 512)
        num_heads: 注意力头数 (如 8)
        ff_dim: 前馈网络隐藏层维度 (如 2048)
        dropout: dropout 概率
    """
    def __init__(self, embed_dim, num_heads, ff_dim, dropout=0.1):
        super().__init__()
        
        # Self-Attention
        self.self_attention = MultiHeadAttention(embed_dim, num_heads)
        self.norm1 = nn.LayerNorm(embed_dim)
        self.dropout1 = nn.Dropout(dropout)
        
        # Feed-Forward
        self.feed_forward = PositionwiseFeedForward(embed_dim, ff_dim, dropout)
        self.norm2 = nn.LayerNorm(embed_dim)
        self.dropout2 = nn.Dropout(dropout)
    
    def forward(self, x, mask=None):
        """
        Args:
            x: 输入 (batch_size, seq_len, embed_dim)
            mask: padding mask (batch_size, 1, 1, seq_len)
                  用于屏蔽 padding 位置
        
        Returns:
            output: (batch_size, seq_len, embed_dim)
        """
        # 1. Self-Attention + Residual + Norm
        attn_output = self.self_attention(x, x, x, mask=mask)
        x = self.norm1(x + self.dropout1(attn_output))
        
        # 2. Feed-Forward + Residual + Norm
        ff_output = self.feed_forward(x)
        x = self.norm2(x + self.dropout2(ff_output))
        
        return x
```

---

## BPE (Byte Pair Encoding)

```python
from collections import defaultdict

class BPE:
    """
    BPE 分词算法 - 简化版
    
    核心思想：
    1. 统计所有相邻字符对的频率
    2. 合并频率最高的字符对
    3. 重复 num_merges 次
    """
    def __init__(self, num_merges=10):
        self.num_merges = num_merges
        self.merges = []  # 存储合并顺序
    
    def get_stats(self, words):
        """统计相邻字符对频率"""
        pairs = defaultdict(int)
        for word in words:
            for i in range(len(word) - 1):
                pairs[(word[i], word[i + 1])] += 1
        return pairs
    
    def merge_vocab(self, pair, words):
        """合并指定的字符对"""
        new_words = []
        bigram = ' '.join(pair)
        replacement = ''.join(pair)
        
        for word in words:
            new_word = ' '.join(word).replace(bigram, replacement)
            new_words.append(tuple(new_word.split()))
        
        return new_words
    
    def train(self, corpus):
        """训练 BPE"""
        # 初始化：每个词拆成字符
        words = [tuple(word) + ('_',) for word in corpus.split()]
        
        for i in range(self.num_merges):
            pairs = self.get_stats(words)
            if not pairs:
                break
            
            # 找频率最高的pair
            best = max(pairs, key=pairs.get)
            words = self.merge_vocab(best, words)
            self.merges.append(best)
            print(f"{i+1}. {best} -> {''.join(best)}")
    
    def tokenize(self, text):
        """分词"""
        word = tuple(text) + ('_',)
        
        for pair in self.merges:
            bigram = ' '.join(pair)
            replacement = ''.join(pair)
            word_str = ' '.join(word).replace(bigram, replacement)
            word = tuple(word_str.split())
        
        return list(word)


# 使用示例
bpe = BPE(num_merges=10)
bpe.train("low low low low lower lower newest newest newest")
print(bpe.tokenize("lowest"))
```