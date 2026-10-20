# Last updated: 10/20/2026, 12:28:59 PM
1class Solution:
2    def numIdenticalPairs(self, nums: list[int]) -> int:
3        ans=0
4        counter=Counter(nums)
5        for i in counter:
6            n=counter[i]
7            ans+= n * (n - 1) // 2
8        return ans