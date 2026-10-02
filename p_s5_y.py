import torch
d = torch.load("simto.pt", weights_only=True)
x1 = 1.0
x2 = 1.0
y = d["w1"] * x1 + d["w2"] * x2 + d["b"]
print(y)