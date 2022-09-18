# 功能：给定三个发射者01x和一个接收者D，求位置判断正确的临界
from lib import *
from _1_2_1 import main as _1_2_1
# 输入：接收的角度a01,a0x,a1x
# 输出：[[(),...（x确定时的解）]*8（2~9下标对应0~7）]
from _1_2_1 import findans
# 从结果中找最近的点作为答案返回
from _1_2_1 import test
# 测试用
from pos1 import *



# 给定实际发射0,1,fr和接收to，在to的角度th方向的mid长度看是否3个定位可行
def ok3(fr, to, th, mid):
    # D接收者实际位置
    D = tpt(pos(to),cotran((mid,th)))
    ret = test(fr, to, D)
    # try:
    #     ret=test(fr,to,D)
    # except:
    #     print(fr, to, D)
    #     ret = test(fr, to, D)
    return simp(D,ret[3])



# 给定实际发射0,1,fr和接收to，在to的角度th方向找到临界值
def jgth(fr, to, th):
    l=0
    r=25
    while (r-l)>eps:
        mid = (r+l)/2
        if ok3(fr,to,th,mid):
            l=mid
        else:
            r=mid
    return l


# 给定实际发射0,1,fr和接收to，在角度[be,ed]分nt(>=2)个方向，得到各方向的临界值，返回最小值
# 输入:fr,to,nt,be,ed
# 输出:mi_list[(r,th)...],ep【精度】
def rangejudge(fr, to, be=0, ed=2 * pi, nt=4):
    if be==0 and ed == 2*pi:
        ed-=  (2 * pi)/nt
    ep = (ed - be) / (nt - 1)
    ang = [be + ep*i for i in range(nt)]
    mi_list = []
    for th in ang:
        ret=jgth(fr, to, th)
        mi_list.append((ret, th))
    return mi_list,ep


# 给定实际发射0,1,fr和接收to，返回最小值，各方向临界值
# 输入：fr,to
# 输出：Pmi,mi_list[(r,th)...]
def judge(fr,to):
    lth=0
    rth=2*pi
    Pmi=None
    mi=inf
    mi_list=[]
    while rth-lth>eps:
        ret=rangejudge(fr,to,lth,rth)
        ep=ret[1]
        ret_list=ret[0]
        for i in ret_list:
            mi_list.append(i)
            if i[0]<mi:
                Pmi=i
                mi=i[0]
        rth=Pmi[1]+ep
        lth=Pmi[1]-ep
    return Pmi,mi_list



# 判断这个队形下的最小值
# 先枚举每个队形， 求出临界的结果，再求其中最小值
# 输出：最小临界值dmi,最小临界极坐标Pmi，发射fr,接收to，临界点列表tr
def main():
    dmi = inf
    Pmi = None
    fr = None
    to = None
    tr = None
    for i in range(2, 10):  # 发射
        for j in range(2, 10):  # 接收
            if i == j:
                continue
            # i=3
            # j=5
            ret = judge(i, j)
            if dmi > ret[0][0]:
                dmi = ret[0][0]
                Pmi = ret[0]
                tr = ret[1]
                fr = i
                to = j
    return dmi,Pmi, fr, to, tr


if __name__ == '__main__':
    ans = main()
    print('最小临界值dmi', ans[0])
    print('最小临界极坐标Pmi', ans[1])
    print('发射fr', ans[2])
    print('接收to', ans[3])
    print('临界点列表tr', ans[4])

