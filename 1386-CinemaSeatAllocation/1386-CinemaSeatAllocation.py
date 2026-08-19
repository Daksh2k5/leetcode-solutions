# Last updated: 8/19/2026, 3:16:10 PM
1class Solution:
2    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
3        d={}
4        count=0
5        for i in reservedSeats:
6            if i[1]!=1 or i[1]!=10:     
7                d[i[0]]=d.get(i[0],0b1111111111)& ~(1<<((i[1])-1))
8        for i in d:
9            if d[i] & 0b0000011110 == 0b0000011110:
10                count += 1
11                d[i]=d[i]&0b1111100001
12
13            if d[i] & 0b0111100000 == 0b0111100000:
14                count += 1
15                d[i]=d[i]&0b1000011111
16
17            if d[i] & 0b0001111000 == 0b0001111000:
18                count += 1
19
20        count= count + (n-len(d))*2
21        return(count)