# Last updated: 10/6/2026, 10:38:26 PM
1class Solution:
2    def calPoints(self, ops: list[str]) -> int:
3        record=[]
4        for i in ops:
5            if i == "C":
6                record.pop()
7                pass
8            elif i == "+":
9                record.append(int(record[-2])+int(record[-1]))
10                pass
11            elif i == "D":
12                record.append(int(record[-1])*2)
13                pass
14            else:
15                record.append(int(i))
16        if len(record)!=0:
17            return sum(record)
18        else:
19            return 0