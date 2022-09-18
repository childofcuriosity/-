# 问题2共用的库

import pandas as pd
# 给出第2问编号为a的点的坐标A, 按照50
# 输入：a(0~14)
# 输出：A
r = 50
rd2 = r / 2
rs3 = rd2 * 3 ** (1 / 2)
pos_list = [(0, 0),
            (-rs3, rd2), (-rs3, -rd2),
            (-2 * rs3, r), (-2 * rs3, 0), (-2 * rs3, -r),
            (-3 * rs3, 3 * rd2), (-3 * rs3, rd2), (-3 * rs3, -rd2), (-3 * rs3, -3 * rd2),
            (-4 * rs3, 2 * r), (-4 * rs3, r), (-4 * rs3, 0), (-4 * rs3, -r), (-4 * rs3, -2 * r),
            ]


def pos(a):
    return pos_list[a]

# 2的ans转excel
def to_excel(ans, name='_1_3.xlsx'):
    df = []
    for an in ans:
        df.append([an[0][0], an[1]] + [x[0] for x in an[0][1]]+[x[1] for x in an[0][1]])
    df = pd.DataFrame(df)
    df.to_excel(name)
