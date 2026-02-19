import sys
input = sys.stdin.readline

from decimal import *
a, b = map(int, input().split())
getcontext().prec = 32
result = Decimal(a) / Decimal(b)
print(result)
