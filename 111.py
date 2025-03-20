import numpy as np
import matplotlib.pyplot as plt

# 定义参数
A = 1  # 振幅
f = 1  # 频率
phi = 0  # 相位
t = np.linspace(0, 2, 1000)  # 时间范围

# 生成正弦信号
y_sin = A * np.sin(2 * np.pi * f * t + phi)

# 绘制信号
plt.figure(figsize=(12, 8))

plt.subplot(3, 1, 1)
plt.plot(t, y_sin)
plt.title('正弦信号')
plt.xlabel('时间 (s)')
plt.ylabel('振幅')

plt.tight_layout()
plt.show()
    