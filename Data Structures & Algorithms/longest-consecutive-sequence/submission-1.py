class Solution:
    def recurse(self, num, mp):
        if num not in mp:
            return 0
        if mp[num]!=-1:
            return mp[num]
        
        x = self.recurse(num+1,mp)
        mp[num]=x+1
        return x+1

    def longestConsecutive(self, nums: List[int]) -> int:
        mp = {}
        for num in nums:
            mp[num] = -1

        output = 0
        for num in nums:
            output = max(output,self.recurse(num,mp))
        print(mp)
        return output

        