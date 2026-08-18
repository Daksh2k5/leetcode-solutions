# Last updated: 8/18/2026, 10:16:03 AM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        if len(nums)==0:
4            return 0
5        nums=sorted(set(nums))
6        print(nums)
7        count=1
8        mlen=0
9        for i in range(len(nums)-1):
10            if nums[i]+1==nums[i+1]:
11                count+=1
12                mlen=max(mlen,count)
13            else:
14                count=1
15
16        return mlen if mlen!=0 else 1
17