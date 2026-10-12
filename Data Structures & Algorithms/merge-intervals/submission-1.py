class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        merged = [intervals[0]]

        for i in range(1, len(intervals)):
            prev = merged[-1]
            cur = intervals[i]

            if cur[0] <= prev[1]:
                merged[-1][1] = max(merged[-1][1], cur[1])
            else:
                merged.append(cur)
        return merged
                
