# Last updated: 8/9/2026, 12:35:37 PM
class Solution:
    def minimumPushes(self, word: str) -> int:
        if len(word)<=8:return len(word)
        elif len(word)>8 and len(word)<=16:
            return 8+((len(word)-8)*2)
        elif len(word)>16 and len(word)<=24:
            return 8+((len(word)-8)*2) + len(word)-16
        elif len(word)==25:
            return 8+((len(word)-8)*2) + len(word)-15
        else:
            return 8+((len(word)-8)*2) + len(word)-14