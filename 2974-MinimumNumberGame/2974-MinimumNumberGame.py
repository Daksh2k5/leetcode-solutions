# Last updated: 11/25/2026, 9:56:27 PM
1class Solution:
2    def numberGame(self, nums: List[int]) -> List[int]:
3        ans= sorted(nums)
4        for i in range(0,len(ans),2):
5            ans[i],ans[i+1]=ans[i+1],ans[i]
6        return ans