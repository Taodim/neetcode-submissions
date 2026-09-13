class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start, end = 0, len(nums) -1

        while start <= end:
                    
            midIndex = int((start + end) // 2)
            print(start, midIndex, end)    
                              
            if nums[midIndex] > target:
                print("returned left half")
                end = midIndex - 1
            
            elif nums[midIndex] < target:
                print("returned right half")
                start = midIndex + 1
            
            else:
                return midIndex

        
        return -1
            

  
