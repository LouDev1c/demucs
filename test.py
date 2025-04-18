import torch
print(torch.__version__)          # 应输出 1.8.1+cu113
print(torch.cuda.is_available())  # 应返回 True
print(torch.version.cuda)         # 应输出 11.3
