import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            maxHeap.append(stone*-1)
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            x = -1*heapq.heappop(maxHeap)
            y = -1*heapq.heappop(maxHeap)

            if x != y:
                heapq.heappush(maxHeap, -1*abs(y-x))

        if len(maxHeap) == 1:
            return -1*heapq.heappop(maxHeap)
        
        return 0