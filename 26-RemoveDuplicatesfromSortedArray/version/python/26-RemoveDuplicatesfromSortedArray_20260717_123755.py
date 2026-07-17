# Last updated: 7/17/2026, 12:37:55 PM
#somewhat better runtime
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        s=sorted(set(nums))
4        for i in range(len(nums)):
5            nums.pop()
6        for i in s:
7            nums.append(i)
8        return (len(nums))
