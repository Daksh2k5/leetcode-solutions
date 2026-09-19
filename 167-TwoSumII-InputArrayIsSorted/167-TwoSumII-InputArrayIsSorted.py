# Last updated: 9/4/2026, 12:18:33 PM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low=0
        high=len(numbers)-1
        while low<high:
            q= numbers[high]+numbers[low]
            if q<target:
                low+=1
            if q>target:
                high-=1
            if q == target:
                return [low+1,high+1]