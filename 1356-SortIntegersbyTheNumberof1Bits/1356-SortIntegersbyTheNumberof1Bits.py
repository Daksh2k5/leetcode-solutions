# Last updated: 10/4/2026, 2:08:36 AM
1class Solution:
2    def sortByBits(self, arr: list[int]) -> list[int]:
3        return sorted(arr, key=lambda x: (bin(x).count("1"), x))
4