class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ret = []
        nums.sort()
        visited = set()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum == 0:
                    if (nums[i], nums[l], nums[r]) not in visited:
                        ret.append((nums[i], nums[l], nums[r]))
                        visited.add((nums[i], nums[l], nums[r]))
                    l += 1
                elif threeSum < 0:
                    l += 1
                else:
                    r -= 1

        return ret
                        
