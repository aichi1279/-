#!python3

def judge(a, b): # a->win , b->lose
    if a=="G" and b=="C":
        return 0
    elif a=="C" and b=="P":
        return 0
    elif a=="P" and b=="G":
        return 0
    elif a==b:
        return -1

    return 1

def main():
    N, M = map(int,input().split())
    S = [input() for i in range(2*N)]
    rank = [[0,i] for i in range(2*N)]

    for m in range(M):
        for n in range(N):
            player1 = rank[2*n][1]
            player2 = rank[2*n+1][1]
            result = judge(S[player1][m],S[player2][m])
            if result != -1: rank[2*n+result][0] -= 1
        rank.sort()
        for line in rank:
            print(line,end=" ")


    for _,i in rank: print(i+1)


if __name__ == '__main__':
    main()
