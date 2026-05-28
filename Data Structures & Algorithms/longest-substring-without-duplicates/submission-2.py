class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = 0
        b = 0
        set1 = set()
        output = 0
        while b<len(s):
            #expand right
            while(b<len(s) and s[b] not in set1):
                set1.add(s[b])
                b+=1
            output = max(output,b-a)
            while(a<b and b<len(s) and s[a]!=s[b]):
                set1.remove(s[a])
                a+=1
            
            a+=1
            b+=1
        output = max(output,b-a)
        return output
            
        