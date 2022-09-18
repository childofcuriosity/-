# 一些共用的库，基础功能
from math import *
from numpy.random import normal
import pandas as pd
import numpy as np

# 点(x,y)
# 极坐标(rho,th)
# 圆(O,r) O是圆心点
# 射线(x,y)
# 向量(x,y)
# 柱搜索的状态(分数，实际点元组((,)...),实际点速度向量元组((,)...))

# eps
eps = 1e-3
# inf
inf = 1e8

# R第一问圆的半径
R = 100


# 两点求欧氏距离
# 输入:p1,p2（是元组xy）
# 输出:d
def dis(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1 / 2)


# 二维向量a,b的叉乘，正负可判断向量方向
# 输入：a,b
# 输出：axb
def cplus(a, b):
    return a[0] * b[1] - a[1] * b[0]


# 向量a,b的点乘
# 输入：a,b
# 输出：a·b
def poiplus(a, b):
    return a[0] * b[0] + a[1] * b[1]


# 向量a的大小
# 输入：a
# 输出：|a|
def vlen(a):
    return (a[0] ** 2 + a[1] ** 2) ** (1 / 2)


# 射线a,b的夹角，
# 输入：a,b
# 输出：a,b夹角
def angle(a, b):
    c = poiplus(a, b) / (vlen(a) * vlen(b))
    return acos(c)


# 符号函数
# 输入：x
# 输出：-1，0，1之一
def sgn(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


# 射线a与b的夹角，a在b逆正顺负
# 输入：a,b
# 输出：a与b夹角带正负
def K(a, b):
    # if vlen(a) * vlen(b) == 0:
    #     print(a,b)
    if poiplus(a, b) / (vlen(a) * vlen(b)) == -1:  # 特判反向，是pi不是0
        return pi
    ans = angle(a, b) * sgn(cplus(b, a))
    return ans


# 向量的形成，始A终B
# 输入:A,B
# 输出：v
def vinit(A, B):
    return B[0] - A[0], B[1] - A[1]


# 判断三点是否共线
# 输入：A,B,C
# 输出：bool
def inline(A, B, C):
    return abs(cplus(vinit(A, B), vinit(A, C))) < eps


# 判断列表中是否有三点共线
# 输入：pl[P1,P2,P3,P4]
# 输出：bool
def inlinel(pl):
    for i in range(len(pl)):
        for j in range(i + 1, len(pl)):
            for k in range(j + 1, len(pl)):
                if inline(pl[i], pl[j], pl[k]):
                    return True
    return False


# 三边求角余弦定理
# 输入:d1,d2,d3
# 输出:a, 是d1的对角
def costh(d1, d2, d3):
    if abs(d1 - d2 - d3) < eps:
        return pi
    if abs(d2 - d1 - d3) < eps or abs(d3 - d1 - d2) < eps:
        return 0
    c = (d2 ** 2 + d3 ** 2 - d1 ** 2) / (2 * d2 * d3)
    return acos(c)


# 判断两个点是否一样
# 输入：A,B
# 输出：bool
def simp(A, B):
    return abs(A[0] - B[0]) < eps and abs(A[1] - B[1]) < eps


# 角度a，求弧度b
# 输入:a
# 输出:b
def angtran(a):
    return a * pi / 180


# 弧度b，求角度a
# 输入:b
# 输出:a
def tranang(b):
    return b * 180 / pi


# 点p在容器v里
# 输入：p,v
# 输出：bool
def pinv(p, v):
    for i in v:
        if simp(i, p):
            return True
    return False


# 极坐标转直角坐标
# 输入：P(rho,th)
# 输出：x,y
def cotran(P):
    return P[0] * cos(P[1]), P[0] * sin(P[1])


# 极坐标转直角坐标
# 输入：(x,y)
# 输出：(rho,th)
def tranco(P):
    if simp(P, (0, 0)):
        return (0, 0)
    rho = dis((0, 0), P)
    th = K(P, (1, 0))
    if th + eps < 0: th += 2 * pi
    th = tranang(th)
    return rho, th


# 给两个点群的距离打分。
# 输入：L1,L2
# 输出：avg_d：两两点的欧式距离平均
def grade(L1, L2):
    sum_d = 0
    for P in zip(L1, L2):
        sum_d += dis(P[0], P[1])
    return sum_d / len(L1)


# 在排序状态x时的key
# 输入:x
# 输出:key
def xkey(x):
    return x[0][0]


# 元组a乘数b
# 输入：a,b
# 输出：ans
def tmn(a, b):
    if isinstance(a[0], tuple):
        return tuple(tmn(x, b) for x in a)
    return tuple(x * b for x in a)


# 元组a加元组b
# 输入：a,b
# 输出：ans
def tpt(a, b):
    if isinstance(a[0], tuple):
        return tuple(tpt(x[0], x[1]) for x in zip(a, b))
    return tuple(x[0] + x[1] for x in zip(a, b))


# 元组a加数n
# 输入：a,n
# 输出：ans
def tpn(a, n):
    if isinstance(a[0], tuple):
        return tuple(tpn(x, n) for x in a)
    return tuple(x + n for x in a)


# 元组减法
# 输入：a,b
# 输出：ans
def tst(a, b):
    if isinstance(a[0], tuple):
        return tuple(tst(x[0], x[1]) for x in zip(a, b))
    return tuple(x[0] - x[1] for x in zip(a, b))


# 截断正态分布(0,N)，绝对值不超过3N
# 输入：N
# 输出：ans
def nor(N):
    ans = normal(0, N, 1)[0]
    while abs(ans) > 3 * N:
        ans = normal(0, N, 1)[0]
    return ans


# 向元组t的每个元素加一个nor误差
# 输入：t,N
# 输出:t_
def tnor(t, N):
    if isinstance(t[0], tuple):
        return tuple(tnor(x, N) for x in t)
    return tuple(x + nor(N) for x in t)


rng = np.random.RandomState(123456789)


# t分布
# 输入: s, n
# 输出：ans
def ttt(s, n):
    return s * rng.standard_t(n)


# 向元组t的每个元素加一个s*t(n)分布误差
# 输入：t, s, n
# 输出：t_
def tt(t, s, n):
    if isinstance(t[0], tuple):
        return tuple(tt(x, s, n) for x in t)
    return tuple(x + ttt(s, n) for x in t)


# 判断两个浮点数相等
# 输入:a,b
# 输出:bool
def eq(a, b):
    return abs(a - b) < eps


# 测量的三个角度_3a加正态分布误差，保持角度关系
# 输入：_3a,N
# 输出：_3a_
def anor(_3a, N):
    s = tnor((0, 0, 0), N)
    if eq(_3a[0] + _3a[1] + _3a[2], pi / 2):
        _3a = (_3a[0] + (2 * s[0] - s[1] - s[2]) / 4, _3a[1] + (2 * s[1] - s[0] - s[2]) / 4,
               _3a[2] + (2 * s[2] - s[0] - s[1]) / 4)
    if eq(_3a[0] - _3a[1] - _3a[2], 0):
        _3a = (_3a[0] + (2 * s[0] + s[1] + s[2]) / 4, _3a[1] + (2 * s[1] + s[0] - s[2]) / 4,
               _3a[2] + (2 * s[2] + s[0] - s[1]) / 4)
    if eq(_3a[1] - _3a[0] - _3a[2], 0):
        _3a = (_3a[1], _3a[0], _3a[2])
        _3a = (_3a[0] + (2 * s[0] + s[1] + s[2]) / 4, _3a[1] + (2 * s[1] + s[0] - s[2]) / 4,
               _3a[2] + (2 * s[2] + s[0] - s[1]) / 4)
        _3a = (_3a[1], _3a[0], _3a[2])
    if eq(_3a[2] - _3a[0] - _3a[1], 0):
        _3a = (_3a[2], _3a[1], _3a[0])
        _3a = (_3a[0] + (2 * s[0] + s[1] + s[2]) / 4, _3a[1] + (2 * s[1] + s[0] - s[2]) / 4,
               _3a[2] + (2 * s[2] + s[0] - s[1]) / 4)
        _3a = (_3a[2], _3a[1], _3a[0])
    return _3a
