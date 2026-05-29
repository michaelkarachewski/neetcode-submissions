from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        mp = defaultdict(list)
        for index,num in enumerate(nums):
            mp[num].append(index)
        
        output = set()
        for x in range(len(nums)):
            for y in range(x+1,len(nums)):
                targetval = 0 - (nums[x]+nums[y])
                if targetval in mp:
                    l = mp[targetval]
                    for index in l:
                        if index!=x and index!=y:
                            newlist = [nums[x],nums[y],nums[index]]
                            newlist.sort()
                            tup = tuple(newlist)
                            output.add(tup)

        outputlist = []
        for x in output:
            outputlist.append(list(x))
        return outputlist

        