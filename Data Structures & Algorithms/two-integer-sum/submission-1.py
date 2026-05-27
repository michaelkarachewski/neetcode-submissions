class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for index,num in enumerate(nums):
            if num in mp and 2*num==target:
                return [mp[num],index]
            mp[num]=index
        
        for index,num in enumerate(nums):
            if target-num!=num and target-num in mp:
                return [min(index,mp[target-num]), max(index,mp[target-num])]
        