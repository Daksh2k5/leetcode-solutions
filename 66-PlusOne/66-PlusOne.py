# Last updated: 8/9/2026, 12:37:32 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=""
        for i in digits:
            n+=str(i)
        n=int(n)
        n+=1
        n=str(n)
        ans=[int(x) for x in n]
        return ans