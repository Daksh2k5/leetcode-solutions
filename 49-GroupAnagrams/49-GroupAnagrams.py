# Last updated: 8/9/2026, 12:37:42 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        ans=[]
        l1=[]
        for i in strs:
            dic={}
            for j in i:
                if j not in dic:
                    dic[j]=1
                else:
                    dic[j]+=1
            l.append(dic)
        # for i in l:
        #     if i not in l1:
        #         l1.append(i)
        l1 = list({tuple(sorted(d.items())): d for d in l}.values())
        for i in l1:
            l1=[]
            for j in range(len(strs)):
                if l[j]== i:
                    l1.append(strs[j])
            ans.append(l1)
        return ans