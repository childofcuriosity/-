# 功能：给出2个已知的发射者01和1个未知的发射者，和接收的角度，得到当未知发射者为2~9时，接收者的定位
# 适用于3架无人机，选取最近的作解
from lib import *
from _1_1 import main as _1_1
# 给定三个发射坐标点A(x1,y1)B(x2,y2)C(x3,y3)，三个接收的两两角aAB aAC aBC，求满足的点D
# 输入：A,B,C,aAB,aAC,aBC
# 输出：[D1,D2...]（可能多个满足）
from _1_1_3 import main as _1_1_3
from pos1 import *

# 3发射：ABC     1接收：D   余弦定理求3角度 aAB aAC aBC
# 输入：A,B,C,D
# 输出：aAB, aAC, aBC


# 输入：接收的角度a01,a0x,a1x
# 输出：[[(),...（x确定时的解）]*8（2~9下标对应0~7）]
def main(a01, a0x, a1x):
    ans_list = []
    P0 = pos(0)
    P1 = pos(1)
    for x in range(2, 10):
        Px = pos(x)
        ans_list.append(_1_1(P0, P1, Px, a01, a0x, a1x))
    return ans_list


# 从结果中找最近的点作为答案返回
def findans(ans, bE):
    E = pos(bE)
    dmi = inf
    # 找到实际与理想距离最小的，作为实际位置
    for i in range(len(ans)):
        if i + 2 == bE:
            continue  # 自己知道自己不是发射
        for j in ans[i]:
            if dis(j, E) < dmi:
                bmi = i + 2
                pmi = j
                dmi = dis(j, E)
    return bmi, pmi, dmi


# 测试用
def test(fr=3, bE=5, D=pos(5)):
    # 三个发射者
    A = pos(0)
    B = pos(1)
    C = pos(fr)
    # D接收者实际位置
    # D的编号bE
    # bE = bE
    # D = D
    aAB, aAC, aBC = _1_1_3(A, B, C, D)
    ans = main(aAB, aAC, aBC)
    # print(ans)
    bmi, pmi, dmi = findans(ans, bE)
    return fr, bmi, bE, pmi, dmi


if __name__ == '__main__':
    D = tpt(pos(5), (25,0))
    ret = test(D=D)

    print('实际未知发射者编号：', ret[0])
    print('预测未知发射者编号：', ret[1])
    print('期望接收者编号：', ret[2])
    print('期望接收者位置：', pos(ret[2]))
    print('预测接收者位置：', ret[3])
    print('偏差距离：', ret[4])
