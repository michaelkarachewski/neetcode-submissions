class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for curstring in strs:
            sorted_str = "".join(sorted(curstring))
            if sorted_str in mp:
                mp[sorted_str].append(curstring)
            else:
                mp[sorted_str] = [curstring]
        output = []
        for key in mp:
            output.append(mp[key])
        return output
            


        