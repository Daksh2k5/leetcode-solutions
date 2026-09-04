# Last updated: 9/4/2026, 12:18:33 PM
1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3        low=0
4        high=len(numbers)-1
5        while low<high:
6            q= numbers[high]+numbers[low]
7            if q<target:
8                low+=1
9            if q>target:
10                high-=1
11            if q == target:
12                return [low+1,high+1]