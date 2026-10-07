# Last updated: 10/7/2026, 7:13:40 PM
1class Solution:
2    def validMountainArray(self, arr: list[int]) -> bool:
3        m=arr.index(max(arr))
4        if m == 0 or m==len(arr)-1 or len(arr)<3:
5            return False
6        l1=arr[:m+1]
7        l2=arr[m:][::-1]
8        for i in range(1,len(l1)):
9            if l1[i-1]>=l1[i]:
10                return False
11        for i in range(1,len(l2)):
12            if l2[i-1]>=l2[i]:
13                return False
14        return True