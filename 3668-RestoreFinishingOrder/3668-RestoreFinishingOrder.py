# Last updated: 8/31/2026, 7:47:20 PM
1class Solution:
2    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
3        ans=[]
4        for i in order:
5            if i in friends:
6                ans.append(i)
7        return ans