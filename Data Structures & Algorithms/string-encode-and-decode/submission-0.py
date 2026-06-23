class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        
        for i in strs:
            length = len(i)
            store = str(length) + "#" + i
            s += store 
        return s

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0 

        while i < len(s):
            j = i
            while s[j] != "#":
                j +=1
            strs = int(s[i:j])
            new = s[j+1:j+1+strs]
            result.append(new)

            i = j + 1 + strs
        return result
