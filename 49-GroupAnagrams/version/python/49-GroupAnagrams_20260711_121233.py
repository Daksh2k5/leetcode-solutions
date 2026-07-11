# Last updated: 7/11/2026, 12:12:33 PM
# I made minor tweaks but they did not end up making a substancial improvement
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
14        # for i in l:
15        #     if i not in l1:
16        #         l1.append(i)
17        l1 = list({tuple(sorted(d.items())): d for d in l}.values())
18        for i in l1:
19            l1=[]
20            for j in range(len(strs)):
21                if l[j]== i:
22                    l1.append(strs[j])
23            ans.append(l1)
24        return ans
