# Last updated: 8/9/2026, 12:36:40 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in range(k):
            ans.append(max(d,key=d.get))
            d[max(d,key=d.get)]=0

        return ans