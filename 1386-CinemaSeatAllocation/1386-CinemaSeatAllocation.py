# Last updated: 8/30/2026, 11:52:13 PM
class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        d={}
        count=0
        for i in reservedSeats:
            if i[1]!=1 or i[1]!=10:     
                d[i[0]]=d.get(i[0],0b1111111111)& ~(1<<((i[1])-1))
        for i in d:
            if d[i] & 0b0000011110 == 0b0000011110:
                count += 1
                d[i]=d[i]&0b1111100001

            if d[i] & 0b0111100000 == 0b0111100000:
                count += 1
                d[i]=d[i]&0b1000011111

            if d[i] & 0b0001111000 == 0b0001111000:
                count += 1

        count= count + (n-len(d))*2
        return(count)