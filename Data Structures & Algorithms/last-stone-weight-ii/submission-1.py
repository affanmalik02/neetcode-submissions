class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stoneSum = sum(stones)
        target = stoneSum // 2
        dp = {}

        def recursion(i, total):
            if total >= target or i >= len(stones):
                return abs(total - (stoneSum - total))
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(recursion(i + 1, total), recursion(i + 1, total + stones[i]))
            return dp[(i, total)]

        return recursion(0, 0)

