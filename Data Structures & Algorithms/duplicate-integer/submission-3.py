class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n=len(nums)
        i=0
        while(i<n-1):
            if nums[i]== nums[i+1]:
                return True
            i=i+1

        return False
                