class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}
        for i,x in enumerate(nums):
            vals[x] = i
        for i, n in enumerate(nums):
            comp = target - n
            if comp in vals and vals[comp] != i:
                return [i, vals[comp]]
        return []
            
    
