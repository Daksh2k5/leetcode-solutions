# Last updated: 10/14/2026, 10:30:49 AM
1class Solution:
2    def maxSumOfSquares(self, num: int, sum: int) -> str:
3        sys.set_int_max_str_digits(2147483647)
4        ans=""
5        if sum<=9:
6            return str(sum*(10**(num-1)))
7        a=9
8        while sum>0:
9            if sum>=a:
10                sum=sum-a
11                ans+=str(a)
12            else:
13                a-=1
14
15        if len(ans)>num:
16            return ""
17        
18        ans=int(ans)
19        return str(ans * (10**(num-len(str(ans)))))