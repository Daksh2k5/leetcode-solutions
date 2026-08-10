# Last updated: 8/9/2026, 12:35:42 PM
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        dic={"neg":0,'pos':0}
        for i in nums:
            if i < 0:
                dic["neg"]+=1
            if i>0:
                dic['pos']+=1
        return(max(dic.values()))