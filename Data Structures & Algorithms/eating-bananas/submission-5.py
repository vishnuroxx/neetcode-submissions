class Solution:
    import math
    def isSuccessful(self, piles, k, h) -> bool:
        hours_taken = 0
        for pile in piles: 
            hours_taken += math.ceil(pile / k)
        return hours_taken <= h
        
                
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) 
        while left <= right:
            mid = (left + right) // 2
            if self.isSuccessful(piles, mid, h):
                if mid == 1 or not self.isSuccessful(piles, mid-1, h):
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1

        