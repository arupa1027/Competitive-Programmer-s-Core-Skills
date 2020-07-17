# -*- coding: utf-8 -*-

import sys

def main():
    #import numpy as np
    n=int(input())
    sum1=0
    sum2=0
    arr=list(map(float,input().split()))
    for i in arr:
        sum1+=i
        sum2+=(1/i)
    #s="%.9Lf"%sum
    print("%.10Lf"%(sum1+sum2))
if __name__ == '__main__':
    main()