class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) -1

        while start <= end:
                    
            midIndex = int((start + end) // 2)  
                              
            if nums[midIndex] > target:
                end = midIndex - 1
            
            elif nums[midIndex] < target:
                start = midIndex + 1
            
            else:
                return midIndex

        return -1
            

  
