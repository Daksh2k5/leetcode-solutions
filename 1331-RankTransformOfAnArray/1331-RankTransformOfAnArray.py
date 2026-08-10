# Last updated: 8/9/2026, 12:35:55 PM
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ans=sorted(set(arr))
        d={}
        for i in range(len(ans)):
            d[ans[i]]=i+1
        for i in range(len(arr)):
            arr[i]=d[arr[i]]
        return arr