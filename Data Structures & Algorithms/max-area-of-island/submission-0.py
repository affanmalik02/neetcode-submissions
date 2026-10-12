class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        area = 0

        def dfs(x, y):
            if not (x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])):
                return 0
            if grid[x][y] == 0:
                return 0
            if (x, y) in visited:
                return 0

            
            visited.add((x, y))
            ret = 1
            ret += dfs(x, y+1)
            ret += dfs(x+1, y)
            ret += dfs(x-1, y)
            ret += dfs(x, y-1)

            return ret
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                area = max(area, dfs(i, j))

        return area

        