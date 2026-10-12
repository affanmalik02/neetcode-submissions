class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s))
            encoded += ";"
            encoded += s
        return encoded

    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != ";":
                j += 1
            size = int(s[i:j])
            i = j + 1
            j = i + size
            strs.append(s[i:j])
            i = j
            
        return strs