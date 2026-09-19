# Last updated: 9/19/2026, 2:31:08 PM
1# The guess API is already defined for you.
2# @param num, your guess
3# @return -1 if num is higher than the picked number
4#          1 if num is lower than the picked number
5#          otherwise return 0
6# def guess(num: int) -> int:
7
8class Solution:
9    def guessNumber(self, n: int) -> int:
10        low=0
11        high=n+1
12        while low<=high:
13            i=(high+low)//2
14            # print(i)
15            if guess(i) == -1:
16                high=i
17            if guess(i) == 1:
18                low=i
19            if guess(i) == 0:
20                return i
21