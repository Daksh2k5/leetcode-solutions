# Last updated: 11/28/2026, 1:16:39 PM
1class Solution:
2    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
3        n = len(arr)
4        count = 0
5        
6        for i in range(n):
7            for j in range(i + 1, n):
8                for k in range(j + 1, n):
9                    if (abs(arr[i] - arr[j]) <= a and 
10                        abs(arr[j] - arr[k]) <= b and 
11                        abs(arr[i] - arr[k]) <= c):
12                        count += 1
13                        
14        return count