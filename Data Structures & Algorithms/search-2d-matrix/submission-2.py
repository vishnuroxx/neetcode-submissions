class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search the rows
        left, right = 0, len(matrix) - 1
        targetRow = -1 
        while left <= right:
            mid = (left + right) // 2
            
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                targetRow = mid
                break
            elif matrix[mid][0] > target:
                right = right - 1
            else:
                left = left + 1
  
        if targetRow == -1:
            return False

        arr = matrix[targetRow]
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True 
            elif arr[mid] > target:
                right = right - 1
            else:
                left = left + 1
        return False 

        