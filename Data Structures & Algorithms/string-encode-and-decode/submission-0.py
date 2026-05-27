class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for string in strs:
            l = len(string)
            lengthasstring = str(l)
            output=output+lengthasstring+"#"
            for c in string:
                output+=c
        print(output)
        return output


    def decode(self, s: str) -> List[str]:
        output = []
        index=0
        while(index<len(s)):
            #read until pound
            length = ""
            print("index",index)
            while(index<len(s) and s[index]!="#"):
                length+=s[index]
                index+=1
            l = int(length)
            print("length",l)
            newstring = s[index+1:index+1+l]
            output.append(newstring)
            index=index+l+1
            #get next x characters
        return output

