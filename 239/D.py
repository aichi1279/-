A, B, C, D = map(int,input().split())
takahashi = [key for key in range(A, B+1)]

def IsPrime(num):
    if num < 2:
        return False
    elif num == 2:
         return True
    elif num % 2 == 0:
         return False # 偶数はあらかじめ除く

    sqrtNum = int(num**0.5)+ 1
    for i in range(3, sqrtNum, 2):
        if num % i == 0:
            # 素数ではない
            return False

    # 素数である
    return True

#A+B 以上 C+D以下の素数を探せ！
for key in takahashi:
    #key+C以上の素数を生成して、key+D以下かを判定
    win_cnt = 0
    lose_cnt = 0
    for i in range(C, D+1):
        if IsPrime(key+i):
            lose_cnt += 1
        else:
            win_cnt += 1

    #print(win_cnt, lose_cnt)
    if win_cnt == D-C + 1 :
        print("Takahashi")
        exit()

print("Aoki")
