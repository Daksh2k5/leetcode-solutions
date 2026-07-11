# Last updated: 7/11/2026, 4:55:29 PM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        if not strs:
4            return ""
5        pref = strs[0]
6        check = len(pref)
7        for j in range(len(strs)):
8            count = 0
9            for i in range(1, len(pref) + 1):
10                if pref[:i] in strs[j][:i]:
11                    count += 1
12            if count < check:
13                check = count
14        return pref[:check]
15