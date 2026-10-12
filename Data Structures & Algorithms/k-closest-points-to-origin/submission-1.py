import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for point in points:
            euclidean = (math.sqrt(abs(0 - point[0]) ** 2 + (abs(0 - point[1])) ** 2) )
            minHeap.append((euclidean, point))

        heapq.heapify(minHeap)

        ret = []

        for i in range(k):
            ret.append(heapq.heappop(minHeap)[1])

        return ret
        
