class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = 0
        b = len(s)-1
        while(a<=b):
            achar = s[a]
            bchar = s[b]
            if not achar.isalnum() or not bchar.isalnum():
                if not achar.isalnum():  
                    a+=1
                if not bchar.isalnum():
                    b-=1
                continue
            
            if achar.lower()!=bchar.lower():
                return False
            a+=1
            b-=1
        return True
            
        