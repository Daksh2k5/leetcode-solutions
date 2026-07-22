# Last updated: 7/22/2026, 10:06:59 PM
# thank you modi
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        d={}
4        for i in nums:
5            d[i]=d.get(i,0)+1
6        for i in range(len(nums)):
7            if d[nums[i]]>1:
8                for j in range(i+1,len(nums)):
9                    if nums[j]==nums[i] and abs(i-j)<=k:
10                        return True
11        return False