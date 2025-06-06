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

    # Split into multiple heads
    q = q.view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
    k = k.view(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
    v = v.veiw(batch_size, -1, self.num_heads, self.head_dim).transpose(1, 2)
    
    # Scaled dot-product attention
    scores =torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.head_dim)
    
    if mask is None:
      scores = scores.masked_fill(mask == 0, -1e9)
    
    attention  F.softmax(score, dim=-1)
    output  torch.matmul(attention, v)
    
    # Concatenate heads 
    output = output.transpose(1, 2).contiguous().veiw(
      batch_size, -1, self.d_model)
    
    return self.wo(output)

class PositionWiseFeedForward(nn.Module):
  def __init__(self, d_model, d_ff):
      super().__init__()
      self.fc1 = nn.linear(d_model, d_ff)
      self.fc2 = nn.linear(d_ff, d_model)
      self.dropout = nn.Dropout(0.1)

  def forward(self, x):
      return self.fc2(self.dropout(F.relu(self.fc1(x))))

class PositionalEncoding(nn.module):
  def __init__(self, d_model, max_len=5000):
    super__init__()
    pe = torch.zeros(max_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(torch.arange(0, d_model, 2).float() * (-math.log(10000.0) / d_model))

    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 0::2] = torch.cod(position * div_term)
    pe = pe.unsqueeze(0)
    self.register_buffer('pe', pe)

  def forward (self, x):
    return x + self.pe[:, :x.size(1)]

class EncoderLayer(nn.Module):
    def __init__(self. d_model, num_heads, d_ff, dropout=0.1):
      super().init()
self.self_attn = MultiHeadAttenion(d_model, num_heads)
self.norm1 = nn.layerNorm(d_model)
self.norm2 = nn.layerNorm(d_model)
self.dropout = nn.Dropout(dropout)

    def forward(self, x,mask):
      attn_output = self_attn(x,x,x mask)
      x = self.norm1(x + self.dropout(attn_output))
      ff_output = self.feed_forward(x)
      x = self.norm2(x + self.dropout(ff_output))
      return x

class DecoderLayer(nn.Module):
    def __init__(self, d_model, num_heads, d_ff, dropout=0.1):
      super()__init__()
      self.self_attn + MultiHeadAttenion(d_model, num_heads)
      self.cross_attn = MultiHeadAttention(d_model, num_heads)
      self.feed_forward = PositionWiseFeedForward(d_model, d_ff)
      self.norm1 = nn.LayerNorm(d_model)
      self.norm2 = nn.LayerNorm (d_model) 
      self.norm3 = nn.Dropout(dropout) 

    def forward(self, x enc_output, src_mask, tgt_mask):
      #self_attenion
      attn_output = self.self.attn(x,x,x, tgt_mask)
      x = self.norm1(x = self.dropout(attn_output))

      # Cross attention
      attn_output = self.cross_attn(x, enc_output, enc_output, src_mask)
      x = self.norm2(x + self.dropout(attn_output))

      # Feed forward
      ff_output = self.feed_forward(x)
      x = self.norm3(x = self.dropout(ff_output))
      return x

class Transformer(nn.Module):
    def __init__(self, src_vocab_size, tgt_vocab_size, d_model=512, num_heads=8,
                 num_layers=6, d_ff=2048, dropout=0.1):
    super().__init
    self.encoder_embedding = nn.Embedding(src_vocab_size, d_model)
    self.decoder_embedding = nn.Embedding(tgt_vocab_size, d_model)
    self.positional_encoding = PositionalEncoding(d_model)

    self.encoder_layers = nn.moduleList(
      [EncodeLayers(d_model, num_heads d_ff, dropout)
       for _ in range(num_layers)])
    self.decoder_layers = nn.ModuleList(
        [DecoderLayer(d_model, num_heads, d_ff, dropout)
         for _ in range(num_layers)])
  
    self.fc = nn.Linear(d_model, tgt_vocab_size) 
    self.dropout = nn.Dropout(dropout)

    # Encoder 
    src_embedding = self.dropout(self.positional _encodeing(self.encoder_emmbeding(src)))
    enc_output = src_emmbedding
    for enc_layer in self.encoder_layers:
        enc_output= enc_layer(enc_output, src_mask)

    # Decoder
    tgt_embedded = self.dropout(self.positonal_encoding(self.decoder_emmbeding(tgt)))
    dec_output = tgt_embedded
    for dec_layer in self.decoder_laters:
        dec_output = dec_layer(dec-output, enc_output, src_mask, tgt_mask)

    return self.fc(dec_output)

def create_padding_mask(seq):
    return (seq ! = 0).unsqueeze(1).unsqueeze(2)

def create_look_ahead_mask(size):
  mask = torch.triu(torch.ones(size, size), diagonal=1)
  return mask == 0

# Example usage
if __name__=="__main__":
  # Hyperparameters
  src_vocab_size =5000
  tgt_vocab_size =5000
  d_model =512
  num_heads = 8
  num_layers = 6
  d_ff = 2048
  dropout = 0.1

  #create model 
  transformer = Transformer(src_vocab_size, tgt_vocab_size, d_model ,
                            num_heads, num_layers, d_ff, dropout)

  # Example inputs 
  src = torch.randint(0, src_vocab_size, (32, 100)) # batch_size=32, seq_len=100
  tgt = torch.randint(0, tgt_vocab_size, (32, 90)) # batch_size=32, seq_len=90

  # Create masks
  src_mask = creat_padding_mask(src)
  tgt_mask = create_paddding_mask(tgt) & create_look_ahead_mask(tgt.size(1))

Forward pass
output = transform(src, tgt, src_mask, tgt_mask)
print("Output shape:", output.shape) # Should be (32, 90 tgt_vocab_size)



  

  


               








    
      

    





    



    
    

