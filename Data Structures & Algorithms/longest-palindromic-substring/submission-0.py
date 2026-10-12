class Solution:
    def longestPalindrome(self, s: str) -> str:
        retIndex = 0
        retLen = 0

        for i in range(len(s)):
            l = i
            r = i

            # odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > retLen:
                    retIndex = l
                    retLen = r - l + 1
                l -= 1
                r += 1

            l = i
            r = i + 1

            # odd length
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > retLen:
                    retIndex = l
                    retLen = r - l + 1
                l -= 1
                r += 1

        return s[retIndex:retIndex + retLen]

