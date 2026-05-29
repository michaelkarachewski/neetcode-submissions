class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # move lower one

        a=0
        b=len(heights)-1

        output = 0
        while(a<b):
            output = max(output, min(heights[a],heights[b])*(b-a))
            if heights[a]<heights[b]:
                a+=1
            elif heights[a]>heights[b]:
                b-=1
            else:
                a+=1
                b-=1
        return output
            
        