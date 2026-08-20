class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newset=set(nums)
        return len(newset)<len(nums)
        
    