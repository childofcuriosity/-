# 功能：画点图
import matplotlib.pyplot as plt
from lib import *
import numpy as np
import pandas as pd
from pos2 import *

# 画图
def main():
    # 高 宽 写字顺序1~高*宽
    # plt.subplot(247,projection='polar')
    ns = 15
    # df = pd.read_excel('有误差（历史动量比例误差0.09999999999999998，位置误差1，角度误差1e-05）.xlsx')
    df = pd.read_excel('_2_.xlsx')
    # for i in range(8):
    #     posn = 111
    #     sp = plt.subplot(posn, projection='polar')
    #     if i == 0:
    #         sp.set_title('initial position', y=-0.15, fontsize=14)
    #     else:
    #         sp.set_title('after %d adjustment' % i, y=-0.15, fontsize=14)
    #     rho = [df[x][i] for x in range(2, 2 + ns)]
    #     th = [df[x][i] for x in range(2 + ns, 2 + 2 * ns)]
    #     colors = np.linspace(50, 100, num=ns)
    #     plt.scatter(th, rho, c=colors, cmap='viridis')
    #     plt.show()
    plt.subplot(111)
    for i in range(ns):
        x = df[i+2]
        y = df[i+2+ns]
        colors = np.linspace(100, 0, num=len(df))
        s = np.linspace(1, 1, num=len(df))
        plt.scatter(x, y, c=colors, s=s, cmap='viridis')
        plt.plot(x, y, "r:", linewidth=1)
        # plt.show()
    plt.show()
    # for i in range(1):
    #     plt.subplot(111)
    #     i = 3
    #     rho = df[i + 2]
    #     th = df[i + 2 + ns]
    #     Ps = [(a[0],a[1])for a in zip(rho,th)]
    #     Ps = [cotran(x) for x in Ps]
    #     Ps = [tst(x,pos(i)) for x in Ps]
    #     # Ps = Ps[2:]
    #     x = [a[0] for a in Ps]
    #     y = [a[1] for a in Ps]
    #     colors = np.linspace(100, 0, num=len(Ps))
    #     s = np.linspace(20, 10, num=len(Ps))
    #     plt.scatter(x, y, c=colors, s=s, cmap='viridis')
    #     plt.plot(x, y, "r:", linewidth=2)
    #     plt.show()
    # plt.show()
    #
    # print(df)
    # colors = np.linspace(0, 100, num=len(tr))
    # plt.scatter(y, x, c=colors, cmap='viridis')
    # plt.scatter([0], [0], s=[100], color='black')
    # plt.plot([0, Pmi[1]], [0, Pmi[0]], linewidth=3, color='red')


if __name__ == '__main__':
    main()
