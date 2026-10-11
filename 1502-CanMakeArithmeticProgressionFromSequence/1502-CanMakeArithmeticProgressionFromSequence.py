# Last updated: 10/11/2026, 10:37:33 PM
1class Solution:
2    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
3        arr.sort()
4        l=[]
5        for i in range(1,len(arr)):
6            l.append(arr[i]-arr[i-1])
7        for i in range(1,len(l)):
8            if l[i]!=l[i-1]:
9                return False
10        return True
11