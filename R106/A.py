#!/usr/bin/env python3
import math
import sys

def main():

    n=int(input())

    for a in range(1,int(math.log(10**18,3))+1):
        for b in range(1,int(math.log(10**18,5))+1):
            if 3**a+5**b==n:
                print(a,b)
                sys.exit()



    print(-1)

if __name__ == '__main__':
    main()
