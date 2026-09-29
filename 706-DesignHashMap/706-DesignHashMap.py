# Last updated: 9/29/2026, 4:05:23 PM
1class MyHashMap:
2
3    def __init__(self):
4        self.d=[]
5
6    def put(self, key: int, value: int) -> None:
7        flag=0
8        for i in self.d:
9            if i[0]==key:
10                self.d.remove(i)
11                self.d.append([key,value])
12                flag=1
13                break
14        if flag==0:
15            self.d.append([key,value])
16            
17    def get(self, key: int) -> int:
18        for i in self.d:
19            if i[0]==key:
20                return i[1]
21        return -1
22    def remove(self, key: int) -> None:
23        for i in self.d:
24            if i[0]==key:
25                self.d.remove(i)