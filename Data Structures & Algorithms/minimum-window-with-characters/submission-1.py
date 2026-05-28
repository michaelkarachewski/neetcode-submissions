from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        a = 0
        b = 0

        smap = defaultdict(int)
        smapoverflow = defaultdict(int)
        tmap = defaultdict(int)

        for char in t:
            tmap[char] += 1

        minlen = float("inf")
        outputa = -1
        outputb = -1

        while b < len(s):

            # expand right
            c = s[b]

            if c in tmap:
                if smap[c] < tmap[c]:
                    smap[c] += 1
                else:
                    smapoverflow[c] += 1

            # valid window
            while smap == tmap:

                # update answer
                if (b - a + 1) < minlen:
                    minlen = b - a + 1
                    outputa = a
                    outputb = b

                # shrink left
                leftc = s[a]

                if leftc in tmap:

                    # remove overflow first
                    if smapoverflow[leftc] > 0:
                        smapoverflow[leftc] -= 1

                    # then remove required count
                    else:
                        smap[leftc] -= 1

                a += 1

            b += 1

        if outputa == -1:
            return ""

        return s[outputa:outputb + 1]