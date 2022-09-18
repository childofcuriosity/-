# 功能：已知3发射1接收，余弦定理求3角度。用于造数据和推算
from math import *
from lib import *
from pos1 import *

# 3发射：ABC     1接收：D   余弦定理求3角度 aAB aAC aBC
# 输入：A,B,C,D
# 输出：aAB, aAC, aBC
def main(A, B, C, D):
    AB = dis(A, B)
    AC = dis(A, C)
    AD = dis(A, D)
    BC = dis(B, C)
    BD = dis(B, D)
    CD = dis(C, D)
    aAB = costh(AB, AD, BD)
    aAC = costh(AC, AD, CD)
    aBC = costh(BC, BD, CD)
    return aAB, aAC, aBC


if __name__ == '__main__':
    A = (0, 0)
    B = (2, 0)
    C = (0, 2)
    D = (-1, -1)
    print(main(A, B, C, D))
