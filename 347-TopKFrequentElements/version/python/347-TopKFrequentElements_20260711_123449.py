# Last updated: 7/11/2026, 12:34:49 PM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        d={}
4        ans=[]
5        for i in nums:
6            if i not in d:
7                d[i]=1
8            else:
9                d[i]+=1
10        for i in range(k):
11            ans.append(max(d,key=d.get))
12            d[max(d,key=d.get)]=0
13
14        return ans