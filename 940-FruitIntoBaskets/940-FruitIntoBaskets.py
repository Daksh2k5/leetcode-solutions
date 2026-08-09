# Last updated: 8/9/2026, 12:36:09 PM
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        ans = 0

        for right in range(len(fruits)):
            fruit = fruits[right]

            if fruit in count:
                count[fruit] += 1
            else:
                count[fruit] = 1

            while len(count) > 2:
                leftFruit = fruits[left]
                count[leftFruit] -= 1

                if count[leftFruit] == 0:
                    del count[leftFruit]

                left += 1

            ans = max(ans, right - left + 1)

        return ans