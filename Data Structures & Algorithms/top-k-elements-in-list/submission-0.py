class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        ans={}
        i=0
        while(i<n):
            ans[nums[i]]=ans.get(nums[i],0)+1
            i=i+1
        
        final=[]
        for num,cnt in ans.items():
            final.append([cnt,num])
        final.sort()
        res=[]
        while len(res)<k:
            res.append(final.pop()[1]) 
        return res
