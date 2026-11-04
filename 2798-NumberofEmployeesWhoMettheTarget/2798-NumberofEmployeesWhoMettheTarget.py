# Last updated: 11/4/2026, 5:07:20 PM
1class Solution:
2    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
3        ans=0
4        for i in hours:
5            if i>=target:
6                ans+=1
7        return ans