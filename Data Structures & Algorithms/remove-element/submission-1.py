class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #traverse through array, and hold a pointer to how much of the array we've filled up with non-val values
        k = 0;
        for index, num in enumerate(nums): 
            if num != val:
                nums[k] = num
                k+=1
        return k
        
