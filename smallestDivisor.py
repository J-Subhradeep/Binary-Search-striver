nums = [1,2,5,9]
threshold = 6
import math
def divisorByD(nums,d):
    res  =0
    for i in nums:
        res += math.ceil(i/d)
    return res
class Solution:
    def smallestDivisor(self, nums, threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = high
        while high>=low:
            mid = low + (high-low)//2

            '''check if the divisor is valid or not'''
            if(divisorByD(nums,mid)<=threshold):
                ans = mid
                high = mid -1
            else:
                low  = mid+1
        return ans

print(Solution().smallestDivisor(nums,threshold))