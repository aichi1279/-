N,M = [int(key) for key in input().split()]
AB_ls = [[int(key) for key in input().split()] for _ in range(M)]

P_list = [key in ragne(1,N+1)]

#考察：計算量を減らすために、制約条件を満たした数列の生成手法がメイン？
#最後に最小値を求める
