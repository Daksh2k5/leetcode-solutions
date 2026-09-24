# Last updated: 9/24/2026, 11:54:17 PM
1class Solution:
2    def lemonadeChange(self, bills: list[int]) -> bool:
3        five=0
4        ten=0
5        for i in bills:
6            # print(i,wallet)
7            if i == 5:
8                five+=1
9            if i == 10:
10                if five>0:
11                    ten+=1
12                    five-=1
13                else:
14                    return False
15            if i == 20:
16                if five>=3 or (five>=1 and ten>=1):
17                    # wallet[20]+=1
18                    if (five>=1 and ten>=1):
19                        five-=1
20                        ten-=1
21                    else:
22                        five-=3
23                else:
24                    return False
25        return True