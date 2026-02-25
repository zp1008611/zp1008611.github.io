# 机器学习、深度学习、强化学习手撕

## Multi-Head Attention

### PyTorch版本（推荐）

```python
import torch
import torch.nn as nn
import math

class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        assert d_model % num_heads == 0
        
        self.num_heads = num_heads
        self.d_k = d_model // num_heads
        
        self.W_q = nn.Linear(d_model, d_model)
        self.W_k = nn.Linear(d_model, d_model)
        self.W_v = nn.Linear(d_model, d_model)
        self.W_o = nn.Linear(d_model, d_model)
    
    def forward(self, q, k, v, mask=None):
        B, N, C = q.shape
        
        # 线性变换
        Q = self.W_q(q)
        K = self.W_k(k)
        V = self.W_v(v)
        
        # 拆分多头: (B,N,C) -> (B,h,N,d_k)
        Q = Q.view(B, N, self.num_heads, self.d_k).transpose(1, 2)
        K = K.view(B, N, self.num_heads, self.d_k).transpose(1, 2)
        V = V.view(B, N, self.num_heads, self.d_k).transpose(1, 2)
        
        # Attention
        scores = (Q @ K.transpose(-2, -1)) / math.sqrt(self.d_k)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, -1e9)
        attn = scores.softmax(dim=-1)
        out = attn @ V
        
        # 合并多头: (B,h,N,d_k) -> (B,N,C)
        out = out.transpose(1, 2).contiguous().view(B, N, C)
        
        return self.W_o(out)
```

## GAE

```python
import torch
import numpy as np

def compute_gae(rewards, values, dones, gamma=0.99, lambda_=0.95):
    """
    计算GAE优势函数
    Args:
        rewards: 奖励序列 [T]
        values: 价值函数估计 [T+1] (包含最后一个next_value)
        dones: 终止标志 [T]
        gamma: 折扣因子
        lambda_: GAE参数
    Returns:
        advantages: 优势函数 [T]
    """
    T = len(rewards)
    advantages = torch.zeros(T)
    gae = 0
    
    # 从后向前计算
    for t in reversed(range(T)):
        # TD误差
        delta = rewards[t] + gamma * values[t+1] * (1 - dones[t]) - values[t]
        # GAE递推
        gae = delta + gamma * lambda_ * (1 - dones[t]) * gae
        advantages[t] = gae
    
    return advantages
```

---

## PPO损失函数

```python
import torch
import torch.nn.functional as F

def ppo_loss(log_probs_old, log_probs_new, advantages, values_old, values_new, 
             returns, epsilon=0.2, c1=0.5, c2=0.01):
    """
    PPO损失函数
    Args:
        log_probs_old: 旧策略的对数概率 [batch]
        log_probs_new: 新策略的对数概率 [batch]
        advantages: 优势函数 [batch]
        values_old: 旧价值函数 [batch]
        values_new: 新价值函数 [batch]
        returns: 回报 [batch]
        epsilon: clip参数 (0.2)
        c1: value loss系数 (0.5)
        c2: entropy系数 (0.01)
    Returns:
        loss: 总损失
    """
    # 1. Policy Loss (Clipped Surrogate Objective)
    ratio = torch.exp(log_probs_new - log_probs_old)
    surr1 = ratio * advantages
    surr2 = torch.clamp(ratio, 1 - epsilon, 1 + epsilon) * advantages
    policy_loss = -torch.min(surr1, surr2).mean()
    
    # 2. Value Loss (Clipped)
    value_loss_unclipped = (values_new - returns) ** 2
    values_clipped = values_old + torch.clamp(values_new - values_old, -epsilon, epsilon)
    value_loss_clipped = (values_clipped - returns) ** 2
    value_loss = 0.5 * torch.max(value_loss_unclipped, value_loss_clipped).mean()
    
    # 3. Entropy Loss (optional, 如果有的话)
    # entropy = -torch.mean(torch.exp(log_probs_new) * log_probs_new)
    # entropy_loss = -c2 * entropy
    
    # 总损失
    total_loss = policy_loss + c1 * value_loss  # + entropy_loss
    
    return total_loss, policy_loss, value_loss
```

### 简化版（只有policy loss）

```python
def ppo_policy_loss(log_probs_old, log_probs_new, advantages, epsilon=0.2):
    """PPO核心: Clipped Surrogate Objective"""
    ratio = torch.exp(log_probs_new - log_probs_old)
    surr1 = ratio * advantages
    surr2 = torch.clamp(ratio, 1 - epsilon, 1 + epsilon) * advantages
    return -torch.min(surr1, surr2).mean()
```

### 完整版（包含entropy）

```python
def ppo_loss_with_entropy(log_probs_old, log_probs_new, advantages, 
                          values_new, returns, entropy, 
                          epsilon=0.2, c1=0.5, c2=0.01):
    """
    完整PPO损失
    """
    # Policy loss
    ratio = torch.exp(log_probs_new - log_probs_old)
    surr1 = ratio * advantages
    surr2 = torch.clamp(ratio, 1 - epsilon, 1 + epsilon) * advantages
    policy_loss = -torch.min(surr1, surr2).mean()
    
    # Value loss (不带clip的简化版)
    value_loss = F.mse_loss(values_new, returns)
    
    # Entropy loss
    entropy_loss = -entropy.mean()
    
    # 总损失
    loss = policy_loss + c1 * value_loss + c2 * entropy_loss
    
    return loss, policy_loss, value_loss, entropy_loss
```

### 使用示例

```python
# 数据准备
log_probs_old = torch.tensor([-1.0, -1.2, -0.8])
log_probs_new = torch.tensor([-0.9, -1.3, -0.7])
advantages = torch.tensor([0.5, -0.3, 0.8])
values_new = torch.tensor([2.0, 3.0, 4.0])
returns = torch.tensor([2.5, 2.8, 4.3])

# 计算损失
loss = ppo_policy_loss(log_probs_old, log_probs_new, advantages)
print(f"Policy Loss: {loss.item()}")
```

### 核心要点

**Policy Loss核心**：
```python
ratio = exp(log_π_new - log_π_old)  # 重要性采样比
L^CLIP = min(ratio*A, clip(ratio, 1-ε, 1+ε)*A)
```

**关键参数**：
- `epsilon`: clip范围 (0.2)，限制策略更新幅度
- `c1`: value loss系数 (0.5)
- `c2`: entropy系数 (0.01)

**三个损失**：
1. **Policy Loss**: 带clip的surrogate objective
2. **Value Loss**: MSE或clipped版本
3. **Entropy Loss**: 鼓励探索（可选）