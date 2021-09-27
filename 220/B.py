K = int(input())
A,B = input().split()

ans_A, ans_B = 0,0
A_len, B_len = len(A), len(B)

for i in range(A_len):
    ans_A += int(A[i]) * K**(A_len-i-1)

for i in range(B_len):
    ans_B += int(B[i]) * K**(B_len-i-1)



print(ans_A*ans_B)
