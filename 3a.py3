# -*- coding: utf-8 -*-
#python3

import sys

def main():
    n=int(input())
    a=list(map(float,input().split()))
    b=list(map(float,input().split()))
    x="%.3f"%sum(a)
    y="%.3f"%sum(b)
    if x>y:
        print('SUM(A)>SUM(B)')
    elif x<y: 
        print('SUM(A)<SUM(B)')
    else:
        print('SUM(A)=SUM(B)')
    #print(x,y)
if __name__ == '__main__':
    main()
