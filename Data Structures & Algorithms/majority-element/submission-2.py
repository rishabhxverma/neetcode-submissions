class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        major_boundary = len(nums) / 2 - len(nums) % 2
        for num in nums:
            if num in counts: 
                counts[num] += 1
            else:
                counts[num] = 0
            if counts[num] >= major_boundary:
                return num
        
        return -1