# Last updated: 9/11/2026, 3:10:24 PM
1class Solution:
2    def totalNumbers(self, digits: List[int]) -> int:
3        l=[]
4        p=permutations(digits,r=3)
5        for i in p:
6            if i[0]!=0:
7                if i[-1]%2==0:
8                    if i not in l:
9                        l.append(i)
10        return len(l)