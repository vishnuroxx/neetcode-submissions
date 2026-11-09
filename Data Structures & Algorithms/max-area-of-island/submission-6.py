class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for col in grid[0]] for row in grid]
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not visited[row][col] and grid[row][col]:
                    stack = [(row, col)]
                    area = 0
                    while stack:
                        
                        r, c = stack.pop()
                        
                        if not visited[r][c]:
                            area += 1
                            visited[r][c] = True
                            # visit children
                            if r > 0:
                                stack.append((r - 1, c)) if not visited[r - 1][c] and grid[r - 1][c] else None
                            if r < len(grid) - 1:
                                stack.append((r+1, c)) if not visited[r + 1][c] and grid[r + 1][c] else None
                            if c > 0:
                                stack.append((r, c - 1)) if not visited[r][c - 1] and grid[r][c - 1] else None
                            if c < len(grid[0]) - 1:
                                stack.append((r, c + 1)) if not visited[r][c + 1] and grid[r][c + 1] else None

                            
                        
                        max_area = max(max_area, area)

        return max_area 


        