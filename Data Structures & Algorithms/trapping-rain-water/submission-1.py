class Solution:
    def trap(self, height: List[int]) -> int:
        prefix =[0]*len(height)
        suffix=[0]*len(height)
        water=0
        for i in range(1,len(height)):
            prefix[i]=max(height[i-1],prefix[i-1])
        for i in range(len(height)-2,-1,-1):
            suffix[i]=max(height[i+1],suffix[i+1])
        for i in range(1,len(height)):
            h=min(suffix[i],prefix[i])
            wi=max(0,h-height[i])
            water=water+wi

        return water