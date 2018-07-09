"""
Solved onsite.
Runtime beats 99.54 % of python submissions.
"""


class Solution(object):
    def mark_as_visited(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == "1":
            grid[i][j] = "-1"
            self.mark_as_visited(grid, i + 1, j)
            self.mark_as_visited(grid, i - 1, j)
            self.mark_as_visited(grid, i, j + 1)
            self.mark_as_visited(grid, i, j - 1)
    
    
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        number_of_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    number_of_islands += 1
                    self.mark_as_visited(grid, i, j)
        return number_of_islands