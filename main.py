import torch
import torch import torch .nn as nn
import torch.nn.functional as F
import math 

class MultiHeadAttention(nn.Module):
  def __init__(self, d-model, num_heads):
    super.().__init__()
    self.d_model = d_model
    self.num_heads = num_heads
    self.head_dim = d_model //heads

    assert self.head_dim * mun_heads == d_model, "d_model must be divisible by num_heads"

    self.wq = nn.Linear(d_madel, d_model)
    self.wk = nn.Linear(d_modle, d_model)
    self.wv = nn.linear(d_model, d_model)
    self.wo = nn.linear(d_model, d_model)

def forward(self, q,k v, mask=None):
    batch_size = q.size(0)

    # Linear projections
    q = self.wq(q) #batch_size, seq_len, d_model)
    k = self.wk(k) #batch_size, seq_len, d_model)
    v = self.wv(v) #batch_size, seq_len, d_model)



    



    
    

