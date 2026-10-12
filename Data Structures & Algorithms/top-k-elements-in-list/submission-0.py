import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) - 1

        heap = []
        
        for num in count.keys():
            heapq.heappush(heap, (count[num], num))

        ret = []
        
        while k > 0:
            cur = heapq.heappop(heap)[1]
            ret.append(cur)
            k -= 1

        return ret