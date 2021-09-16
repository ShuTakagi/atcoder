from itertools import accumulate, product, permutations, combinations
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from collections import Counter, deque, defaultdict
from fractions import gcd
a, b, c = map(int, input().split(' '))


def solve(a, b, c):
    if c - b > 0:
        if b - a > 0:
            return "Yes"
    return "No"


print(solve(a, b, c))
