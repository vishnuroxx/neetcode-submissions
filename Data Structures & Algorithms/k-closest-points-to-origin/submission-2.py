class Solution:
    import math
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        heapq.heapify(max_heap)

        for point in points:
            heapq.heappush(max_heap, (-math.sqrt(point[0] ** 2 + point[1] ** 2), point))
        
        while len(max_heap) > k:
            heapq.heappop(max_heap)
        
        return [p for _, p in max_heap]
