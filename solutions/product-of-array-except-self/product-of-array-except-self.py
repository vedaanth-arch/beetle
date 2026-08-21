class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        right=[1]*n
        ans=[1]*n

        for i in range(1,n):
            left[i]=left[i-1]*nums[i-1]
        
        for i in range(n-2,-1,-1):
            right[i]=right[i+1]*nums[i+1]
        for i in range(n):
            ans[i]=left[i]*right[i]
        return ans
        
        '''Here firstly left side of nums is taken n Multiplied by the previous element and stored in left 
        and similar in right side n thn everything is multiplied'''