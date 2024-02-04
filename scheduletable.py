import pandas as pd  #生成一个A4大小的6×6表格
import matplotlib.pyplot as plt    #使用pandas、matplotlib库进行绘制
from pandas.plotting import table
# 创建一个6x6的空DataFrame，并用空字符串初始化所有值
df = pd.DataFrame("", index=range(1, 7), columns=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])

# 设置图表大小为横向A4纸张大小（29.7cm x 21cm）
plt.figure(figsize=(29.7*0.393701, 21*0.393701))

# 绘制表格
ax = plt.gca()
ax.axis('off')
tbl = table(ax, df, loc='center', cellLoc='center', bbox=[0, 0, 1, 1])  

tbl.auto_set_font_size(False)
tbl.set_fontsize(12)
tbl.scale(1.2, 1.2)  

plt.show()
