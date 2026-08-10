# Last updated: 8/9/2026, 12:36:01 PM
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        s = "123456789"
        minl = len(str(low))
        maxl = len(str(high))
        for length in range(minl, maxl + 1):
            for start in range(10 - length):
                ss = s[start : start + length]
                if low <= int(ss) <= high:
                    ans.append(int(ss))
                elif int(ss) > high:
                    break
        return ans