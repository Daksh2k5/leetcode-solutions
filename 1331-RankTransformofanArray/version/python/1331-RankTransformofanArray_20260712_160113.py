# Last updated: 7/12/2026, 4:01:13 PM
1class Solution:
2    def arrayRankTransform(self, arr: List[int]) -> List[int]:
3        ans=sorted(set(arr))
4        d={}
5        for i in range(len(ans)):
6            d[ans[i]]=i+1
7        for i in range(len(arr)):
8            arr[i]=d[arr[i]]
9        return arr