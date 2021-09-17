a,b,w = map(int,input().split())
w *= 1000

ok = []

for i in range(10**6 +1):
    if a*i <= w <= b*i:
        ok.append(i)

if len(ok)==0:
    print("UNSATISFIABLE")
else:
    print(str(min(ok))+" "+str(max(ok)))
