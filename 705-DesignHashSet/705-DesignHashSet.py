# Last updated: 9/29/2026, 2:53:31 PM
1class MyHashSet:
2
3    def __init__(self):
4        self.hash=[]
5
6    def add(self, key: int) -> None:
7        if key not in self.hash:
8            self.hash.append(key)
9
10    def contains(self, key: int) -> bool:
11        return key in self.hash
12
13
14    def remove(self, key: int) -> None:
15        if key in self.hash:
16            self.hash.remove(key)
17
18        
19
20
21# Your MyHashSet object will be instantiated and called as such:
22# obj = MyHashSet()
23# obj.add(key)
24# obj.remove(key)
25# param_3 = obj.contains(key)