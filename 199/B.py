n = int(input())
A_list = list(map(int,input().split()))
B_list = list(map(int,input().split()))

maxi = max(A_list)
#print(maxi)
mini = min(B_list)
#print(mini)

if mini-maxi<0:
    print(0)
else:
    print(mini-maxi+1)
