# Last updated: 8/19/2026, 10:50:18 AM
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return (num%10!=0) if num!=0 else True