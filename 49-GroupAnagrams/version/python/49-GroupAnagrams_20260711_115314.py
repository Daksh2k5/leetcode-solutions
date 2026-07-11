# Last updated: 7/11/2026, 11:53:14 AM
# really poor solution, barely made it through
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3        l=[]
4        ans=[]
5        l1=[]
6        for i in strs:
7            dic={}
8            for j in i:
9                if j not in dic:
10                    dic[j]=1
11                else:
12                    dic[j]+=1
13            l.append(dic)
14        for i in l:
15            if i not in l1:
16                l1.append(i)
17        for i in l1:
18            l2=[]
19            for j in range(len(strs)):
20                if l[j]==i:
21                    l2.append(strs[j])
22            ans.append(l2)
23        return ans