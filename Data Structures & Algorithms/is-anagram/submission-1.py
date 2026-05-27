class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ss = "".join(sorted(s))
        st = "".join(sorted(t))

        for index in range(len(s)):
            if ss[index]!=st[index]:
                return False
        return True
        