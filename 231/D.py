N,M = map(int,input().split())

root_hash = {}
for _ in range(M):
    A,B = map(int,input().split())

    #root_Aについての記録
    if A in root_hash:
        root_hash[A].append(B)
    else:
        root_hash[A] = [B]

    #root_Bについての記録
    if B in root_hash:
        root_hash[B].append(A)
    else:
        root_hash[B] = [A]


#idを付与させることで、同一の組み合わせが存在するかを確認
double_check = {}
for key in root_hash.keys():
    indic = sorted(list(set(root_hash[key])))
    id = ",".join([str(_) for _ in indic])
    #print(id)
    #id付与 OK
    if id in double_check:
        double_check[id] += 1
    else:
        double_check[id] = 1

    if len(set(root_hash[key]))>2:
        print("No")
        exit()


for key in double_check.keys():
    if len(key) >= 2 and double_check[key]>=2:
        print("No")
        exit()
    elif len(key)==1 and double_check[key]>=3:
        print("No")
        exit()

print("Yes")
