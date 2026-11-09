class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = [[False for col in grid[0]] for row in grid]
        max_area = float("-inf")
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if not visited[row][col]:
                    stack = [(row, col)]
                    area = 0
                    while stack:
                        r, c = stack.pop()
                        if not visited[r][c] and grid[r][c]:
                            visited[r][c] = True
                            area += 1
                            # visit children
                            if r > 0:
                                stack.append((r - 1, c))
                            if r < len(grid) - 1:
                                stack.append((r+1, c))
                            if c > 0:
                                stack.append((r, c - 1))
                            if c < len(grid[0]) - 1:
                                stack.append((r, c + 1))
                        else:
                            visited[r][c] = True
                        max_area = max(max_area, area)

        return max_area 


        