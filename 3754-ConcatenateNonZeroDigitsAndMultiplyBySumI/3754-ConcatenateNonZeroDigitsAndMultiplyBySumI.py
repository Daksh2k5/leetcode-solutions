# Last updated: 8/9/2026, 12:35:18 PM
class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        n=str(n)
        print(n)
        q=""
        sum=0
        for i in n:
            if i != "0":
                q=q+i
                sum=sum+int(i)
        return(int(q)*sum)
