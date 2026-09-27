# Last updated: 9/19/2026, 2:46:17 PM
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        high=n+1
7        low=0
8        while low<=high:
9            i = (high+low)//2
10            if isBadVersion(i)==True and isBadVersion(i-1)==False:
11                return i
12            if isBadVersion(i)== True:
13                high=i
14            else:
15                low=i