# Last updated: 9/11/2026, 3:10:24 PM
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        l=[]
        p=permutations(digits,r=3)
        for i in p:
            if i[0]!=0:
                if i[-1]%2==0:
                    if i not in l:
                        l.append(i)
        return len(l)