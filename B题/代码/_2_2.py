# 功能：通过问题一数据，估算x,y坐标的t分布参数（相当于方差）
from lib import *
from pos1 import *


# 输入：raw列表
# 输出：ans
def main(raw):
    avg = sum(raw) / len(raw)
    ans2 = sum([(x - avg) ** 2 for x in raw]) / (len(raw) - 1)
    ans = ans2 ** (1 / 2)
    return ans


if __name__ == '__main__':
    raw = (
        (0, 0),
        (100, 0),
        (98, 40.10),
        (112, 80.21),
        (105, 119.75),
        (98, 159.86),
        (112, 199.96),
        (105, 240.07),
        (98, 280.17),
        (112, 320.28)
    )
    ex = tuple(pos(i) for i in range(len(raw)))
    raw = tuple(cotran((x[0], angtran(x[1]))) for x in raw)
    raw = tst(raw, ex)
    raw = [x[0] for x in raw] + [x[1] for x in raw]
    ans = main(raw)
    print(ans)
