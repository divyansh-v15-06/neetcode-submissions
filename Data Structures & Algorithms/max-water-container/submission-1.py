class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        i =0
        j=len(heights)-1
        maxwater=0
        while i<j:
            water = (j - i) * min(heights[i], heights[j])
            maxwater=max(maxwater,water)
            if heights[i]<=heights[j]:
                i+=1
            elif heights[i]>heights[j]:
                j-=1

        return maxwater 
        