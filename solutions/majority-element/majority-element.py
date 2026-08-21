class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts={}
        majority_limit=len(nums)//2
        for num in nums:
            counts[num]=counts.get(num,0)+1
            if counts[num]>majority_limit:
                return num

'''so majority element, dictionary is used , so firstly one dictionary is kept n thn  one loop is also kept n checked tht  numbers count is more than n/2 return tht number'''