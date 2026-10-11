# Last updated: 10/12/2026, 12:30:36 AM
1class LRUCache:
2    def __init__(self, capacity: int):
3        self.cap = capacity
4        self.lrucache = {}
5        self.recent = []
6
7    def put(self, key: int, value: int) -> None:
8        if key in self.lrucache:
9            self.recent.remove(key)
10        elif len(self.lrucache) >= self.cap:
11            old = self.recent.pop(0)
12            del self.lrucache[old]
13        
14        self.lrucache[key] = value
15        self.recent.append(key)
16
17    def get(self, key: int) -> int:
18        if key not in self.lrucache:
19            return -1
20        self.recent.remove(key)
21        self.recent.append(key)
22        return self.lrucache[key]