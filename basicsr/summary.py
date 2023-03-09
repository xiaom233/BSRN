from thop import profile
import torch
from archs.BSRN_arch import BSRN as net

model = net()
input = torch.randn(1, 3, 320, 180)

macs, params = profile(model, inputs=(input, ))

print("Multi-adds[G] ")
print(macs/1e9)
print("Parameters [K]")
print(params/1e3)