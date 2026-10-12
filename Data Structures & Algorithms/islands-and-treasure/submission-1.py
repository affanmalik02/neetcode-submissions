class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(x, y, distance):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return
            if grid[x][y] == -1:
                return
            if grid[x][y] < distance:
                return

            grid[x][y] = distance
            dfs(x + 1, y, distance + 1)
            dfs(x - 1, y, distance + 1)
            dfs(x, y + 1, distance + 1)
            dfs(x, y - 1, distance + 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    dfs(i, j, 0)