class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for r in range(len(matrix)):
            for j in range(len(matrix[0])):
                if r < j:
                    matrix[r][j], matrix[j][r] = matrix[j][r], matrix[r][j]
        for row in matrix:
            row.reverse()
        
                


        