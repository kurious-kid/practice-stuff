class Solution:
    
    def do_binary_search(self, low, high, array, target):
        
        # print("printing low")
        # print(low)
        # print("prinintg high")
        # print(high)
        mid = int (low + (high - low)/2)
        # print("printig the value of mid")
        # print(mid)
        
        if(array[mid] == target):
            # print("returning mid")
            # print(mid)
            return mid
        
        elif(low > high):
            return low
        
        elif(target < array[mid]):
            return self.do_binary_search(low, mid - 1, array, target)
            
        elif(target > array[mid]):
            return self.do_binary_search(mid + 1, high, array, target)
        
        
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        
        result = self.do_binary_search(low, high, nums, target)
        
        return result
        
