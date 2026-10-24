# Last updated: 10/24/2026, 11:24:34 AM
1class Solution:
2    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
3        days=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
4        temp=sum(days[0:int(arriveAlice[:2])-1])
5        temp+=int(arriveAlice[3:])
6        arriveAlice=temp
7        temp=sum(days[0:int(leaveAlice[:2])-1])
8        temp+=int(leaveAlice[3:])
9        leaveAlice=temp
10        temp=sum(days[0:int(arriveBob[:2])-1])
11        temp+=int(arriveBob[3:])
12        arriveBob=temp
13        temp=sum(days[0:int(leaveBob[:2])-1])
14        temp+=int(leaveBob[3:])
15        leaveBob=temp
16        # print(arriveAlice,leaveAlice,arriveBob,leaveBob)
17        # print(min(leaveAlice,leaveBob),max(arriveAlice,arriveBob))
18        return (max(0,min(leaveAlice,leaveBob)-max(arriveAlice,arriveBob)+1))