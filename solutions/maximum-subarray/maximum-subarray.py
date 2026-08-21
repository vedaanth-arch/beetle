class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=nums[0]
        current_sum=0
        for num in nums:
            if current_sum<0:# Step 1: If current_sum turned negative, reset it to 0
                current_sum=0
            current_sum+=num
            max_sum=max(max_sum,current_sum)# Step 3: Update max_sum if the current_sum is higher
        return max_sum


        '''Here firstly subarray have to be found(subarray can contain any number of elements) so the code has to firstly iterate through complete nums n thn keep adding to current_sums and comparing to max_sum
        and thn compare n give return value'''