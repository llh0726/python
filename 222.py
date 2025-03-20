import numpy as np
import matplotlib.pyplot as plt

# 定义时间范围
n = np.arange(-10, 11)

# 生成单位脉冲信号
delta = np.zeros_like(n)
delta[n == 0] = 1

# 绘制单位脉冲信号
plt.figure(figsize=(12, 9))
plt.subplot(3, 1, 1)
plt.stem(n, delta)
plt.title('单位脉冲信号')
plt.xlabel('n')
plt.ylabel('幅度')
plt.grid(True)

plt.tight_layout()
plt.show()
