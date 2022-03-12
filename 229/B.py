A,B = input().split()

max_len = max(len(A),len(B))
if len(A) < max_len or len(B) < max_len:
    A = ("0"*(max_len-len(A))) + A
    B = ("0"*(max_len-len(B))) + B

for i in range(max_len):
    a = int(A[i])
    b = int(B[i])
    if a+b >=10:
        print("Hard")
        exit()

print("Easy")
