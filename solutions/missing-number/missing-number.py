class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        ES=n*(n+1)//2
        AS=sum(nums)
        return ES-AS

''' 
nums are given upon [0,n] where n can be any number , so to find this we have to do n(n+1)/2 so now first n is calculated n thn n(n+1)/s is done n thn subtracted which is returned 
'''