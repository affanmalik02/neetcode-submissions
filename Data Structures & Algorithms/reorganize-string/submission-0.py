import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        hm = {}
        maxHeap = []

        for char in s:
            hm[char] = hm.get(char, 0) + 1

        for key, count in hm.items():
            maxHeap.append((-count, key))

        heapq.heapify(maxHeap)

        prev = None
        ret = "" 

        while maxHeap or prev != None:
            if prev and not maxHeap:
                return ""

            count, char = heapq.heappop(maxHeap)
            ret += char
            count += 1

            if prev != None:
                heapq.heappush(maxHeap, prev)
                prev = None

            if count != 0:
                prev = (count, char)

        return ret