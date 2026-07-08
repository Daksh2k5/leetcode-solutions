# Last updated: 7/8/2026, 10:32:19 AM
# I'll try binary search later
1class Solution:
2    def maximumCount(self, nums: List[int]) -> int:
3        dic={"neg":0,'pos':0}
4        for i in nums:
5            if i < 0:
6                dic["neg"]+=1
7            if i>0:
8                dic['pos']+=1
9        return(max(dic.values()))
