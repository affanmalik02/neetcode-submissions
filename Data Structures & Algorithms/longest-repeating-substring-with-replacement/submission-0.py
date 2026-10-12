class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        ret = 0

        l = 0
        maxfreq = 0

        for i in range(len(s)):
            hm[s[i]] = hm.get(s[i], 0) + 1
            maxfreq = max(maxfreq, hm[s[i]])

            while  (i - l + 1) - maxfreq > k:
                hm[s[l]] -= 1
                l += 1
            ret = max(ret, i - l + 1) 
        
        return ret