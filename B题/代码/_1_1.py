# 功能：给定三个发射坐标点，三个接收的两两角（天然满足a1+a2=a3），定位接收者的点
from math import *
from lib import *
from pos1 import *
from _1_1_1 import main as _1_1_1
# 弦的线段两点A,B，圆周角a，设圆心是Q
# 输入：A,B,a
# 输出：[(Q1,r),(Q2,r)]
from _1_1_2 import main as _1_1_2
# 两圆的圆心半径o1(O1[0],O1[1],r1),o2(O2[0],O2[1],r2)，求交点[D1, D2]
# 输入:o1,o2
# 输出：[D1, D2]
from _1_1_3 import main as _1_1_3
# 3发射：ABC     1接收：D   余弦定理求3角度 aAB aAC aBC
# 输入：A,B,C,D
# 输出：aAB, aAC, aBC



# 给定三个发射坐标点A(x1,y1)B(x2,y2)C(x3,y3)，三个接收的两两角aAB aAC aBC，求满足的点D
# 输入：A,B,C,aAB,aAC,aBC
# 输出：[D1,D2...]（可能多个满足）
def main(A, B, C, aAB, aAC, aBC):
    # if simp(A,B) or simp(A,C) or simp(B,C):
    #     print(A,B,C)
    # 得到两两夹角的可能圆，有上下两个
    circle_list = [_1_1_1(A, B, aAB), _1_1_1(A, C, aAC), _1_1_1(B, C, aBC)]
    # 可行解的列表
    ans_list = []
    # 二进制的000~111
    for i in range(8):
        # 选取圆
        now_circle_list = [circle_list[0][i & 1], circle_list[1][(i >> 1) & 1], circle_list[2][(i >> 2) & 1]]
        # 两两圆的公共点
        l1 = _1_1_2(now_circle_list[0], now_circle_list[1])
        l2 = _1_1_2(now_circle_list[0], now_circle_list[2])
        l3 = _1_1_2(now_circle_list[1], now_circle_list[2])
        # 三个圆之间如果有公共点，就ok
        for P1 in l1:
            for P2 in l2:
                for P3 in l3:
                    # 公共点
                    if simp(P1, P2) and simp(P1, P3):
                        # 附加限制：这个点不是ABC之一
                        if pinv(P1, [A, B, C]):
                            continue
                        # 附加限制：这个点不是之前出现过的
                        if pinv(P1, ans_list):
                            continue
                        ans_list.append(P1)
    return ans_list


if __name__ == '__main__':
    A = (0.0, 0.0)
    B = (100.0, 0.0)
    C = (17.364606251646684, 98.47495514978128)
    # aAB, aAC, aBC = 0.8738267244276083, 0.17483672782800355, 0.6989899965996057
    D = (17.365058742962116, -98.47873509355637)
    aAB, aAC, aBC = _1_1_3(A, B, C, D)
    print('求解：', main(A, B, C, aAB, aAC, aBC))
    # print('真实：', D)
