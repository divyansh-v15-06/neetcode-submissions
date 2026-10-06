class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res=-1
        n =len(nums)
        left=0
        right=n-1
       
        while left<=right:
            mid=(left+right)//2
            if nums[mid] <target: left=mid+1
            elif nums[mid]==target: return mid
            else: right=mid-1
        return -1    
        