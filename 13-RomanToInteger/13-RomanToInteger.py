# Last updated: 8/9/2026, 12:38:03 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        s=[x for x in s]
        ans=0
        val={
    "I"        :     1,
    "V"        :     5,
    "X"        :     10,
    "L"        :     50,
    "C"         :    100,
    "D"         :    500,
    "M"        :     1000,
        }
        for i in range(len(s)):
            try:
                if s[i]=="I" and s[i+1]=="V":
                    ans+=4
                    s[i+1]="O"
                elif s[i]=="I" and s[i+1]=="X":
                    ans+=9
                    s[i+1]="O"
                elif s[i]=="X" and s[i+1]=="L":
                    ans+=40
                    s[i+1]="O"
                elif s[i]=="X" and s[i+1]=="C":
                    ans+=90
                    s[i+1]="O"
                elif s[i]=="C" and s[i+1]=="D":
                    ans+=400
                    s[i+1]="O"
                elif s[i]=="C" and s[i+1]=="M":
                    ans+=900
                    s[i+1]="O"
                elif s[i]=="O":
                    ans+=0
                else:
                    ans+=val[s[i]]
            except IndexError:
                    ans+=val[s[i]]
        return ans