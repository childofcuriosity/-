# 功能：柱搜索通解（考虑误差版）
# （初始状态S0）初始时刻无人机的位置略有偏差，
# （择优返回）多次调整，
# （动作A1）每次选择编号为 FY00 的无人机和圆周上最多 3 架无人机发射信号，
# （备选状态）其余无人机根据接收到的方向信息，调整到理想位置（每次调整的时间忽略不计），
# 使得 9 架无人机最终均匀分布在某个圆周上。
from lib import *
from _1_1 import main as _1_1
# 给定三个发射坐标点A(x1,y1)B(x2,y2)C(x3,y3)，三个接收的两两角aAB aAC aBC，求满足的点D
# 输入：A,B,C,aAB,aAC,aBC
# 输出：[D1,D2...]（可能多个满足）
from _1_1_3 import main as _1_1_3
from pos2 import *

# 3发射：ABC     1接收：D   余弦定理求3角度 aAB aAC aBC
# 输入：A,B,C,D
# 输出：aAB, aAC, aBC

# 状态数
ns = 15


# 给定接收者i和发射的飞机三元组a，求预测定位到理想位置的向量iv返回
# 3个发射者与该飞机点得到仿真角度_1_1_3
# 仿真角度代入理想的发射者位置得到预测定位（2个，取离理想位置较近的那一个）_1_1
# 求预测定位到理想位置的向量iv返回
# 输入：pos_list, i, a
# 输出：iv
def getiv(pos_list, i, a, N2):
    _3a = _1_1_3(pos_list[a[0]], pos_list[a[1]], pos_list[a[2]], pos_list[i])
    # 给角度a01,a02,a12一个正态分布(0,N2)的误差，表示传感器接收夹角的随机误差
    a01, a02, a12 = anor(_3a, N2)
    # A,B,C=pos(a[0]),pos(a[1]),pos(a[2])
    # if simp(A,B) or simp(A,C) or simp(B,C):
    #     print(A,B,C)
    Piok = _1_1(pos(a[0]), pos(a[1]), pos(a[2]), a01, a02, a12)
    if not Piok:
        print(pos_list[a[0]], pos_list[a[1]], pos_list[a[2]], pos_list[i])
        print(pos(a[0]), pos(a[1]), pos(a[2]), a01, a02, a12)
        _3a = _1_1_3(pos_list[a[0]], pos_list[a[1]], pos_list[a[2]], pos_list[i])
        # 给角度a01,a02,a12一个正态分布(0,N2)的误差，表示传感器接收夹角的随机误差
        a01, a02, a12 = anor(_3a, N2)
        # A,B,C=pos(a[0]),pos(a[1]),pos(a[2])
        # if simp(A,B) or simp(A,C) or simp(B,C):
        #     print(A,B,C)
        Piok = _1_1(pos(a[0]), pos(a[1]), pos(a[2]), a01, a02, a12)
    dmi = inf
    for Pi in Piok:
        if dis(Pi, pos(i)) < dmi:
            dmi = dis(Pi, pos(i))
            imi = Pi
    vi = tst(pos(i), imi)
    return vi


# 给定实际pos_list和发射的飞机三元组a，给出其他飞机离预测理想位置的距离tov
# 对每一个飞机，如果在a中，就是(0,0)表示不知道，否则用getiv求预测定位到理想位置的向量
# 输入：pos_list,a
# 输出：tov
def tranv(pos_list, a, N2):
    ans_list = []
    for i in range(ns):
        if i in a or inlinel([pos(i), pos(a[0]), pos(a[1]), pos(a[2])]):
            i_v = (0, 0)
        else:
            i_v = getiv(pos_list, i, a, N2)
        ans_list.append(i_v)
    return tuple(ans_list)


# 给定当前状态q与动作a，给出理想位置ex与加权参数beta，求下一状态s
# 模拟得到角度——last_pos和a得接收角度
# 猜测到理想位置的向量——按理想的发射位置，3机此，4机选01x两个平均
# 决定速度和长度——加权求得
# 输入：q, a, ex, beta
# 输出：s
def tran(q, a, ex, alpha, beta, bm, N2):
    last_pos = q[1]
    last_v = q[2]
    if len(a) == 3:
        tov = tranv(last_pos, a, N2)
    else:
        tov = tmn(tpt(tpt(tranv(last_pos, (a[0], a[1], a[2]), N2), tranv(last_pos, (a[0], a[1], a[3]), N2)),
                      tranv(last_pos, (a[0], a[2], a[3]), N2)), 1 / 3)
        tov = list(tov)
        tov[a[1]] = tov[a[2]] = tov[a[3]] = (0, 0)
        tov = tuple(tov)

    t1 = tmn(last_v, 1 - beta)
    t2 = tmn(tov, beta)
    v = tmn(tpt(t1, t2), 1 / (1 - (1 - beta) ** bm))
    va = tmn(v, alpha)
    now_pos = tpt(last_pos, va)
    g = grade(ex, now_pos)
    return g, now_pos, v


# 柱搜索的动作集合
# 输出：动作集合
def get_actions():
    ans = []
    for i in range(1, ns):
        for j in range(i + 1, ns):
            ans.append((0, i, j))
            for k in range(j + 1, ns):
                ans.append((0, i, j, k))
    return ans


# 柱搜索迭代优化
# 柱搜索的状态(分数，实际点元组((,)...),实际点速度向量元组((,)...))
# 输入：ex[理想点元组], raw[实际点元组]，epoch迭代的轮数，width保留的较优状态个数，beta加权参数
# 输出：[状态...]（从0到epoch）
def bean(ex, raw, epoch=5, width=30, alpha=1, beta=1, N1=0, N2=0):
    # M:(子状态，(父状态,动作))的字典。
    M = dict()
    # Q:基础状态列表
    Q = [(grade(ex, raw), raw, tuple((0, 0) for i in range(len(raw))))]
    # A:动作列表
    A = get_actions()
    for i in range(1, epoch + 1):
        # S:备选(子状态，(父状态,动作))列表
        S = []
        for q in Q:
            # 给q[1]一个正态分布(0,N1)的误差，表示上一次到这一次接收信号间的随机误差（除0号）
            # q用来寻找父节点
            q1_ = tpn(tnor(q[1], N1), nor(N1))
            q1_ = list(q1_)
            q1_[0] = (0, 0)
            q1_ = tuple(q1_)
            q_ = (q[0], q1_, q[2])
            for a in A:
                S.append((tran(q_, a, ex, alpha, beta, i, N2), (q, a)))
        S.sort(key=xkey)
        S = S[:width]
        for s in S:
            M[s[0]] = s[1]
        Q = [s[0] for s in S]
    ans_list = [(Q[0], tuple())]
    while ans_list[-1][0] in M:
        ans_list.append(M[ans_list[-1][0]])
    ans_list = ans_list[::-1]
    return ans_list


if __name__ == '__main__':
    ex = tuple(pos(i) for i in range(ns))
    # t分布t(19)，样本方差s=5.100611312091458
    s = 5.100611312091458
    n = 19
    raw = tt(ex, s, n)
    raw = list(raw)
    raw[0] = (0, 0)
    raw = tuple(raw)
    epoch, width, alpha, beta, N1, N2 = 16, 5, 1, 1, 1, 0.00001
    ans = bean(ex, raw, epoch=epoch, width=width, alpha=alpha, beta=beta, N1=N1, N2=N2)
    print(ans)
    to_excel(ans, '_2_.xlsx')

# 参数：epoch*width，alpha, beta
