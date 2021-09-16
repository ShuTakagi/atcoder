from fractions import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations

N = int(input())

H = N // 3600
M = (N - H * 3600) // 60
S = (N - H * 3600 - M * 60)

print(str(H) + ":" + str(M) + ":" + str(S))
