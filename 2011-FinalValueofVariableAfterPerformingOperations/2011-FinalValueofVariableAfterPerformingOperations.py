# Last updated: 9/15/2026, 4:45:14 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for i in operations:
            if i =="--X" or i == "X--":
                x-=1
            else:
                x+=1
        return x