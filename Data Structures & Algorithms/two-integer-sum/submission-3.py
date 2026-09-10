class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTracker = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in hashTracker:
                return [hashTracker[dif], i]
            else: 
                hashTracker[nums[i]] = i
        return []