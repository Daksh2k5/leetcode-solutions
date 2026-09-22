# Last updated: 9/22/2026, 11:39:04 PM
1class MinStack:
2
3    def __init__(self):
4        self.s=[]
5        self.ms=[]
6
7    def push(self, value: int) -> None:
8        self.s.append(value)
9        if not self.ms:
10            self.ms.append(value)
11        else:
12            self.ms.append(min(value,self.ms[-1]))
13
14    def pop(self) -> None:
15        self.s.pop()
16        self.ms.pop()
17
18    def top(self) -> int:
19        return self.s[-1]
20
21    def getMin(self) -> int:
22        return self.ms[-1]
23
24
25# Your MinStack object will be instantiated and called as such:
26# obj = MinStack()
27# obj.push(value)
28# obj.pop()
29# param_3 = obj.top()
30# param_4 = obj.getMin()