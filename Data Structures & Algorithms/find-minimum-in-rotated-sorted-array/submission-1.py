class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        curr = float("inf")

        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[right]:
                return nums[left]
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
 
        return curr

    #     iNVARIANT -> RIGHT > LEFT 


    #                         Case 1: Left < Right -> IDEAL
    #                         Case 2: Left > Right 
    #                                 2.1 Mid > Left -> left = mid + 1
    #                                 2.2 Mid < Left 
    #                                             -> Mid < Right -> right = mid 
    #                                             -> Mid > Right -> right = mid - 1 
    #     /
    #    /
    #   /
    #  /
    #     /
    #    /
    #   /