# Last updated: 8/31/2026, 7:47:20 PM
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans=[]
        for i in order:
            if i in friends:
                ans.append(i)
        return ans