# Last updated: 9/15/2026, 5:58:42 PM
1class Solution:
2    def characterReplacement(self, s: str, k: int) -> int:
3        count = {}
4        res = 0
5        l = 0
6        max_freq = 0
7        
8        for r in range(len(s)):
9            count[s[r]] = count.get(s[r], 0) + 1
10            max_freq = max(max_freq, count[s[r]])
11            
12            if (r - l + 1) - max_freq > k:
13                count[s[l]] -= 1
14                l += 1
15                
16            res = max(res, r - l + 1)
17            
18        return res