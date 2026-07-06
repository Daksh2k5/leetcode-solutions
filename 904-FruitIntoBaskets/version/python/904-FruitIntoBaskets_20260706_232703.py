# Last updated: 7/6/2026, 11:27:03 PM
1class Solution:
2    def totalFruit(self, fruits: List[int]) -> int:
3        count = {}
4        left = 0
5        ans = 0
6
7        for right in range(len(fruits)):
8            fruit = fruits[right]
9
10            if fruit in count:
11                count[fruit] += 1
12            else:
13                count[fruit] = 1
14
15            while len(count) > 2:
16                leftFruit = fruits[left]
17                count[leftFruit] -= 1
18
19                if count[leftFruit] == 0:
20                    del count[leftFruit]
21
22                left += 1
23
24            ans = max(ans, right - left + 1)
25
26        return ans