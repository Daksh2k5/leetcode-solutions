# Last updated: 11/5/2026, 12:07:20 PM
1class Solution:
2    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
3        ans = 0
4        for x in arr1:
5            flag = True
6            for y in arr2:
7                if abs(x - y) <= d:
8                    flag = False
9                    break
10            if flag:
11                ans += 1      
12        return ans
13        