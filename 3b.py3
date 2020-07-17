# -*- coding: utf-8 -*-

import sys

def main():
    import math
    x, y = map(int,input().split())
    if y!=0:
        print(math.ceil(x/y))
    result = 0
if __name__ == '__main__':
    main()