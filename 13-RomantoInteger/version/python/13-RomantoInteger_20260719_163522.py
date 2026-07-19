# Last updated: 7/19/2026, 4:35:22 PM
1class Solution:
2    def romanToInt(self, s: str) -> int:
3        s=[x for x in s]
4        ans=0
5        val={
6    "I"        :     1,
7    "V"        :     5,
8    "X"        :     10,
9    "L"        :     50,
10    "C"         :    100,
11    "D"         :    500,
12    "M"        :     1000,
13        }
14        for i in range(len(s)):
15            try:
16                if s[i]=="I" and s[i+1]=="V":
17                    ans+=4
18                    s[i+1]="O"
19                elif s[i]=="I" and s[i+1]=="X":
20                    ans+=9
21                    s[i+1]="O"
22                elif s[i]=="X" and s[i+1]=="L":
23                    ans+=40
24                    s[i+1]="O"
25                elif s[i]=="X" and s[i+1]=="C":
26                    ans+=90
27                    s[i+1]="O"
28                elif s[i]=="C" and s[i+1]=="D":
29                    ans+=400
30                    s[i+1]="O"
31                elif s[i]=="C" and s[i+1]=="M":
32                    ans+=900
33                    s[i+1]="O"
34                elif s[i]=="O":
35                    ans+=0
36                else:
37                    ans+=val[s[i]]
38            except IndexError:
39                    ans+=val[s[i]]
40        return ans