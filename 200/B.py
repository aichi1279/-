N, D, H =map(int, input().split())

maxi_d = 0
maxi_h = 0
index = 10**9
for i in range(N):
    d, h = map(int,input().split())
    tmp_index = (H-h)*(10**4)/(D-d)
    if tmp_index < index:
        index = tmp_index
        maxi_h = h
        maxi_d = d


a = ((maxi_h-H)/(maxi_d-D))
a *= 10**4
if a==0:
    print(H)
else:
    b = H - (a*D/(10**4))
    print(max(b,0.0))
