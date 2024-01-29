import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

# 创建一个6x6的空DataFrame，并用空字符串初始化所有值
df = pd.DataFrame("", index=range(1, 7), columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

# 设置图表大小为横向A4纸张大小（29.7cm x 21cm）
plt.figure(figsize=(29.7*0.393701, 21*0.393701))

# 绘制表格
ax = plt.gca()
ax.axis('off')
tbl = table(ax, df, loc='center', cellLoc='center', bbox=[0, 0, 1, 1])  # bbox用于控制表格的位置和大小

# 调整表格样式，使其更适合填充整个页面
tbl.auto_set_font_size(False)
tbl.set_fontsize(12)
tbl.scale(1.2, 1.2)  # 根据需要调整表格的缩放比例

# 显示图表
plt.show()
