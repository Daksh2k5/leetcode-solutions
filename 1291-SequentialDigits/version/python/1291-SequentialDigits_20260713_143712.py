# Last updated: 7/13/2026, 2:37:12 PM
1class Solution:
2    def sequentialDigits(self, low: int, high: int) -> List[int]:
3        ans = []
4        s = "123456789"
5        minl = len(str(low))
6        maxl = len(str(high))
7        for length in range(minl, maxl + 1):
8            for start in range(10 - length):
9                ss = s[start : start + length]
10                if low <= int(ss) <= high:
11                    ans.append(int(ss))
12                elif int(ss) > high:
13                    break
14        return ans