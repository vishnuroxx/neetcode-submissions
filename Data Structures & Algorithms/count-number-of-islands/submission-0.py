class Solution:
    from collections import deque 
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    visited[i][j] = True
                    # run bfs
                    q = deque([(i, j)])
                    while q:
                        row, col = q.popleft()
                        # visit children 
                        if row > 0:
                            if grid[row-1][col] == '1' and not visited[row - 1][col]:
                                visited[row - 1][col] = True
                                q.append((row-1, col))

                        if row < len(grid) - 1:
                            if grid[row+1][col] == '1' and not visited[row + 1][col]:
                                visited[row + 1][col] = True
                                q.append((row+1, col))
                        
                        if col > 0:
                            if grid[row][col - 1] == '1' and not visited[row][col - 1]:
                                visited[row][col - 1] = True
                                q.append((row, col - 1))

                        if col < len(grid[0]) - 1:
                            if grid[row][col + 1] == '1' and not visited[row][col + 1]:
                                visited[row][col + 1] = True
                                q.append((row, col + 1))
        return count 
                        


                        
                    
        