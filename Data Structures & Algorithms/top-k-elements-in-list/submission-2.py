class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}

        for idx in range(len(nums)):
            if hash.get(nums[idx]):
                hash[nums[idx]] += 1
            else:
                hash[nums[idx]] = 1

        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in hash.items():
            buckets[freq].append(num)
        result = []
        for idx in range(len(buckets)-1, -1, -1):
            if k == 0:
                break
            else:
                if buckets[idx]:
                    k -= len(buckets[idx])
                    result += buckets[idx]
                    

        return result
