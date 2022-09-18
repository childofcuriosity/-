# 功能：给出2个已知的发射者01和2个未知的发射者xy的5个角度(用不到axy)，推测两个编号，定位接收者位置
from lib import *
from _1_2_1 import main as _1_2_1
# 输入：接收的角度a01,a0x,a1x
# 输出：[[(),...（x确定时的解）]*8（2~9下标对应0~7）]
from _1_1_3 import main as _1_1_3
from pos1 import *

# 3发射：ABC     1接收：D   余弦定理求3角度 aAB aAC aBC
# 输入：A,B,C,D
# 输出：aAB, aAC, aBC

# 输入：a01,a0x,a1x,a0y,a1y
# 输出：[(D,bx,by),...]（D是定位，b是编号，...多解）
def main(a01, a0x, a1x, a0y, a1y):
    ans_x = _1_2_1(a01, a0x, a1x)
    ans_y = _1_2_1(a01, a0y, a1y)
    ans_list = []
    for i in range(len(ans_x)):
        for j in range(len(ans_y)):
            if i == j:
                continue  # 发射的两个不相同
            # 相容
            for Pi in ans_x[i]:
                for Pj in ans_y[j]:
                    if simp(Pi, Pj):
                        ans_list.append((Pi, i + 2, j + 2))
                        break
    return ans_list


if __name__ == '__main__':
    # 四个发射者
    A = pos(0)
    B = pos(1)
    C = pos(4)
    D = pos(7)
    # 一个接收者
    E = 100, 100
    # 期望的位置
    bE = 2
    aAB, aAC, aBC = _1_1_3(A, B, C, E)
    aAB, aAD, aBD = _1_1_3(A, B, D, E)
    ans = main(aAB, aAC, aBC, aAD, aBD)
    print(ans)
    dmi = inf
    # 找到实际与理想距离最小的，作为实际位置
    for i in ans:
        if dis(i[0],  pos(bE)) < dmi:
            pmi = i
            dmi = dis(i[0], pos(bE))
    print('预测未知发射者编号：', pmi[1],pmi[2])
    print('预测接收者位置：', pmi[0])
    print('期望接收者位置：', pos(bE))
    print('偏差距离：', dmi)
