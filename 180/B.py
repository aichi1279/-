#!/usr/bin/env python3
import sys
import math


def main():
    n=0
    n=int(input())

    list=[]
    maxi=0
    sum=0
    uq = 0.0

    str=input()
    str_list=str.split(" ")

    for i in range(n):
        list.append(int(str_list[i]))
        uq += (list[i] * list[i])
        if maxi<list[i]:
            maxi= list[i]
        if list[i]<0:
            sum += list[i] *(-1)
            continue
        sum += list[i]

    print(sum)
    print('{:.17g}'.format(math.sqrt(uq))) 
    print(maxi)


if __name__ == '__main__':
    main()
