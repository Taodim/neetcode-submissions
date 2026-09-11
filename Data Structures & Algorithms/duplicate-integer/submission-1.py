class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSetTracker = set()
        for i in range(len(nums)):
            if nums[i] in hashSetTracker:
                return True
            hashSetTracker.add(nums[i])
        return False