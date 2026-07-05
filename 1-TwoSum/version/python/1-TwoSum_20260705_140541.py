# Last updated: 7/5/2026, 2:05:41 PM
# one-pass, using list instead of hash table
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        l=[]
4        for i in range(len(nums)):
5            if target-nums[i] in l:
6                return [i,l.index(target-nums[i])]
7            else:
8                l.append(nums[i])
9        return []
10