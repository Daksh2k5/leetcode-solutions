# Last updated: 7/29/2026, 3:14:57 PM
# i'll attempt it with heaps later
1class Solution:
2    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
3        for i in range(k):
4            nums[nums.index(min(nums))]*=multiplier
5        return nums