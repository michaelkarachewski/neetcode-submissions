from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()

        mp = defaultdict(int)
        for index,num in enumerate(nums):
            mp[num] = index
        
        lastxval = None
        lastyval = None

        #visited = set()
        output = []
        for x in range(len(nums)):
            if nums[x] == lastxval:
                continue
            else:
                lastxval = nums[x]
            for y in range(x+1,len(nums)):
                if nums[y] == lastyval:
                    continue
                else:
                    lastyval = nums[y]
                '''if (nums[x],nums[y]) not in visited:
                    visited.add((nums[x],nums[y]))'''
                   
                targetval = 0 - (nums[x]+nums[y])
                #print(nums[x],nums[y],targetval)
                if targetval in mp:
                    lastindex = mp[targetval]
                    if lastindex>x and lastindex>y:
                        newlist = [nums[x],nums[y],nums[lastindex]]
                        output.append(newlist)
                        

        return output 

        