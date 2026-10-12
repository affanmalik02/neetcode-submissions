class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0 or (i, j) in visited:
                return 0
            else:
                visited.add((i,j))
                return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        
        maxArea = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxArea = max(maxArea, dfs(i, j))

        return maxArea
