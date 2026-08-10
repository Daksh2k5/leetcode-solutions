# Last updated: 8/9/2026, 12:35:58 PM
class Solution(object):
    def tribonacci(self, n):
        l=[0,1,1]
        n1=0
        n2=1
        n3=1
        if n==0:
            return n1
        if n==1:
            return n2
        if n==2:
            return n3
        for i in range(1,n):
            q=l[-1]+l[-2]+l[-3]
            l.append(q)
        return l[-2]
        