#User function Template for python3


        # code here
class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        num_islands = 0
        
        # Directions for moving in all 8 directions (up, down, left, right, and 4 diagonals)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        def dfs(r, c):
            # If the current cell is out of bounds or is water ('W'), return
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == 'W':
                return
            
            # Mark the current cell as visited by setting it to water ('W')
            grid[r][c] = 'W'
            
            # Explore all 8 directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)
        
        # Traverse through all the cells in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':  # Found an unvisited land cell
                    num_islands += 1
                    dfs(r, c)  # Start DFS to mark the entire island
        
        return num_islands
