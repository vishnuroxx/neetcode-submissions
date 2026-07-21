class Solution:
    def subsetsHelper(self, arr, temp, ptr, n, result):
        if ptr > n:
            result.append(temp)
            return
        else:
            # choose or we dont choose
            choose = temp.copy()
            choose.append(arr[ptr])
            self.subsetsHelper(arr, choose, ptr + 1, n, result)
            self.subsetsHelper(arr, temp, ptr + 1, n, result)


    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.subsetsHelper(nums, [], 0, len(nums) - 1, result)

        return result