# Last updated: 10/5/2026, 12:27:26 PM
1class Solution:
2    def countDigits(self, num: int) -> int:
3        count=0
4        for i in str(num):
5            if num%int(i)==0:
6                count+=1
7        return count