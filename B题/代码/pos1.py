# 问题1共用的库

from lib import *
import pandas as pd
# 给出第一问编号为a的点的坐标A, 按照100
# 输入：a(0~9)
# 输出：A
def pos(a):
    if a == 0:
        return 0, 0
    th = angtran((a - 1) * 40)
    return R * cos(th), R * sin(th)


# (3)的ans转excel
def to_excel(ans, name='_1_3.xlsx'):
    df = []
    for an in ans:
        df.append([an[0][0], an[1]] + [tranco(x)[0] for x in an[0][1]] + [tranco(x)[1] for x in an[0][1]])
    df = pd.DataFrame(df)
    df.to_excel(name)
