# 功能：已知两圆，求交点
from math import *
from lib import *
from pos1 import *

# 两圆的圆心半径o1(O1[0],O1[1],r1),o2(O2[0],O2[1],r2)，求交点[D1, D2]
# 输入:o1,o2
# 输出：[D1, D2]
def main(o1, o2):
    # 把公式实现
    O1 = o1[0]
    r1 = o1[1]
    O2 = o2[0]
    r2 = o2[1]
    d = dis(O1, O2)
    if d > (r1 + r2) or d < (r1 - r2):
        return []
    a = costh(r2, r1, d)
    _O1O2 = vinit(O1, O2)
    th = K(_O1O2, (1, 0))
    D1 = (O1[0] + r1 * cos(th + a), O1[1] + r1 * sin(th + a))
    if abs(a) < 1e-10:
        return [D1]
    D2 = (O1[0] + r1 * cos(th - a), O1[1] + r1 * sin(th - a))
    return [D1, D2]


if __name__ == '__main__':
    O1 = (0, 0)
    r1 = 2
    O2 = (2, 2)
    r2 = 2
    o1 = (O1, r1)
    o2 = (O2, r2)
    print(main(o1, o2))
