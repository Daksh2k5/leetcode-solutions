# Last updated: 11/14/2026, 12:10:18 PM
1class Solution:
2    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
3        ans = 10**9
4        flag = False
5        
6        for i in range(len(nums)):
7            curr = 0
8            for j in range(i, min(len(nums), i + r)):
9                curr += nums[j]
10                if j - i + 1 >= l and curr > 0:
11                    if curr < ans:
12                        ans = curr
13                    flag = True
14                    
15        return ans if flag else -1