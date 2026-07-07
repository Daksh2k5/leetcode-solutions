# Last updated: 7/7/2026, 10:11:29 PM
# naive approach
1class Solution:
2    def sumAndMultiply(self, n: int) -> int:
3        if n==0:
4            return 0
5        n=str(n)
6        print(n)
7        q=""
8        sum=0
9        for i in n:
10            if i != "0":
11                q=q+i
12                sum=sum+int(i)
13        return(int(q)*sum)
14