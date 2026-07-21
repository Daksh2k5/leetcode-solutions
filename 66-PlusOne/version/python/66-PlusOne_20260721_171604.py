# Last updated: 7/21/2026, 5:16:04 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        n=""
4        for i in digits:
5            n+=str(i)
6        n=int(n)
7        n+=1
8        n=str(n)
9        ans=[int(x) for x in n]
10        return ans