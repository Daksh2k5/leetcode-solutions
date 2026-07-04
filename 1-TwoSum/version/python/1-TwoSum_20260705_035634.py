# Last updated: 7/5/2026, 3:56:34 AM
# hash table
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        dic={}
4        for i in range(len(nums)):
5            dic[i]=nums[i]
6        for i in range(len(dic)):
7            x= target-dic[i]
8            if ( x in nums) and nums.index(x)!=i :
9                return[i,nums.index(x)]