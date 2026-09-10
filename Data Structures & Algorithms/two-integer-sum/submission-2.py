class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTracker = {}
        hashTracker[nums[0]] = 0
        for i in range(1, len(nums)):
            dif = target - nums[i]
            if dif in hashTracker:
                return [hashTracker[dif], i]
            else: 
                hashTracker[nums[i]] = i
        return [0,0]


            