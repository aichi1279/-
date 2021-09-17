import numpy as np

def main():

    A, B, C = map(int,input().split())

    list=[]
    for a in range(1,(A+1)%998244353):
        for b in range(1,(B+1)%998244353):
            list.append([a,b])

    sub_list = [i for i in range(1,(C+1)%998244353)]
    sum=0
    for ls in list:
        for sub in sub_list:
            sum += ls[0]*ls[1]*sub


    print(sum%998244353)
    
if __name__ == '__main__':
    main()
