# Last updated: 8/27/2026, 9:53:42 AM
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        end=len(s)
        start=0
        ans=[]
        for i in s:
            if i == "I":
                ans.append(start)
                start+=1
            else:
                ans.append(end)
                end-=1
        if s[-1]=="I":
            ans.append(ans[-1]+1)
        else:
            ans.append(ans[-1]-1)
        return ans