import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np

# 用于存储每个按钮对应的图像组件
signal_canvases = {
    "单位脉冲信号": None,
    "单位阶跃信号": None,
    "矩形脉冲信号": None,
    "三角脉冲信号": None,
    "指数信号": None
}


def unit_impulse():
    toggle_signal("单位脉冲信号", lambda: generate_unit_impulse())


def unit_step():
    toggle_signal("单位阶跃信号", lambda: generate_unit_step())


def rectangular_pulse():
    toggle_signal("矩形脉冲信号", lambda: generate_rectangular_pulse())


def triangular_pulse():
    toggle_signal("三角脉冲信号", lambda: generate_triangular_pulse())


def exponential_signal():
    toggle_signal("指数信号", lambda: generate_exponential_signal())


def generate_unit_impulse():
    n = np.arange(-10, 11)
    x = np.zeros_like(n)
    x[n == 0] = 1
    return n, x


def generate_unit_step():
    n = np.arange(-10, 11)
    x = np.where(n >= 0, 1, 0)
    return n, x


def generate_rectangular_pulse():
    n = np.arange(-10, 11)
    x = np.where((n >= -2) & (n <= 2), 1, 0)
    return n, x


def generate_triangular_pulse():
    n = np.arange(-10, 11)
    x = np.maximum(0, 1 - np.abs(n) / 3)
    return n, x


def generate_exponential_signal():
    n = np.arange(-10, 11)
    x = 0.8 ** n
    return n, x


def toggle_signal(signal_name, generate_func):
    global signal_canvases
    if signal_canvases[signal_name] is None:
        n, x = generate_func()
        signal_canvases[signal_name] = plot_signal(n, x, f"{signal_name} Signal")
    else:
        signal_canvases[signal_name].get_tk_widget().destroy()
        signal_canvases[signal_name] = None


def plot_signal(n, x, title):
    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel('n')
    ax.set_ylabel('x[n]')
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()
    return canvas


root = tk.Tk()
root.title("基本离散信号")

# 创建按钮框架
button_frame = tk.Frame(root)
button_frame.pack()

# 创建按钮
button_impulse = tk.Button(button_frame, text="单位脉冲信号", command=unit_impulse)
button_impulse.pack(side=tk.LEFT)

button_step = tk.Button(button_frame, text="单位阶跃信号", command=unit_step)
button_step.pack(side=tk.LEFT)

button_rect = tk.Button(button_frame, text="矩形脉冲信号", command=rectangular_pulse)
button_rect.pack(side=tk.LEFT)

button_tri = tk.Button(button_frame, text="三角脉冲信号", command=triangular_pulse)
button_tri.pack(side=tk.LEFT)

button_exp = tk.Button(button_frame, text="指数信号", command=exponential_signal)
button_exp.pack(side=tk.LEFT)

root.mainloop()
    