# Last updated: 11/27/2026, 5:24:55 PM
1class Solution:
2    def shuffle(self, nums: List[int], n: int) -> List[int]:
3        ans=[]
4        for i in range(n):
5            ans.append(nums[i])
6            ans.append(nums[n+i])
7        return ans