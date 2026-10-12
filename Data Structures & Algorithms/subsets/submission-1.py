class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []

        cur = []
        def dfs(self, root):
            if root >= len(nums):
                ret.append(cur.copy())
                return


            cur.append(nums[root])
            dfs(self, root + 1)

            cur.pop()
            dfs(self, root + 1)

        dfs(self, 0)
        return ret
