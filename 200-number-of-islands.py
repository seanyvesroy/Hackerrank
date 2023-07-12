class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:    
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.explore(grid,i,j)
                    count += 1     
        return count

    def explore(self, grid: List[List[str]], i, j):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != '1':
            return
        grid[i][j] = '2'
        self.explore(grid,i + 1,j)
        self.explore(grid,i,j + 1)
        self.explore(grid,i - 1,j)
        self.explore(grid,i,j - 1)