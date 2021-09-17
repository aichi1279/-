n = int(input())

charge = 1000 -(n%1000)
if charge==1000:
    print(0)
else:
    print(charge)
