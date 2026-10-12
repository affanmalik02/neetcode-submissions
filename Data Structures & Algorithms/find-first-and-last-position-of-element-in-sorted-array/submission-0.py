class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binarySearch(target):
            l = 0 
            r = len(nums) - 1

            while l <= r:
                m = (r + l) // 2
                if nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            return l
        
        l = binarySearch(target)
        r = binarySearch(target+1)-1

        if l <= r:
            return [l, r]

        return [-1, -1]


    