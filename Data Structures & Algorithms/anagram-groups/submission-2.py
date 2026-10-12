class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)
        for s in strs:
            cur = [0] * 26
            for i in s:
                cur[ord(i) % 26] += 1
            hm[tuple(cur)].append(s)

        return list(hm.values())