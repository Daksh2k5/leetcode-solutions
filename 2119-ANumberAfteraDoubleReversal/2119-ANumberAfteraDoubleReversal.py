# Last updated: 8/19/2026, 10:50:18 AM
1class Solution:
2    def isSameAfterReversals(self, num: int) -> bool:
3        return (num%10!=0) if num!=0 else True