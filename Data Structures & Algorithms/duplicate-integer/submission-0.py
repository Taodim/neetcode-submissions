class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashTracker = {}
        for i in range(len(nums)):
            if nums[i] in hashTracker:
                return True
            hashTracker[nums[i]] = 1
        return False