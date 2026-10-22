class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array
        
        for i in range(len(nums) - 2):
            # Optimization: If the smallest number is > 0, sum can never be 0
            if nums[i] > 0:
                break
                
            # Skip duplicate anchor values to prevent duplicate triplets
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 2: Initialize two pointers
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Skip duplicate values for 'left' and 'right'
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                    
        return res
        '''
        Here for do the solving firstly understand this 
        1.the nums has to be sorted in ascending order 
        2.keep 2 pointer and 1 loop pointer where the loop pointer is defining the 1st number of the nums
        3.left=starting at 2nd number (1st index)
        4.right index starting at comlpete end
        5.now major conditions are checking if all 
        s=nums[i]+nums[left]+nums[right]=0
        if s<0,move the left counter towards right
        if s==0,move both left n right inwards
        and left moved and loop index also moves in with left.
        '''