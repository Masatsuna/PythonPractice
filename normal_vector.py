import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

font_path = '/usr/share/fonts/truetype/takao-gothic/TakaoPGothic.ttf'
font_prop = FontProperties(fname=font_path)
matplotlib.rcParams['font.family'] = font_prop.get_name()

x = np.arange(0, 6, 0.1)

fx = np.sin(x) + 2

plt.plot(x, fx, label="sin")
#plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("X")
plt.ylabel("Z")
plt.title('法線')

plt.legend()
plt.show()
