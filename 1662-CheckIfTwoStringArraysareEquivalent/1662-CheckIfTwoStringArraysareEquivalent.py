# Last updated: 11/9/2026, 3:20:47 PM
1class Solution:
2    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
3        arr1=""
4        arr2=""
5        for i in word1:
6            arr1+=i
7        for i in word2:
8            arr2+=i
9        return arr1==arr2