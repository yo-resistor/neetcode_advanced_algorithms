from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ref: https://leetcode.com/problems/maximum-subarray/
        # if the previous sum is negative, we do not need to add that to the current value
        # if the previous sum is positive, we add that to the current value
        # adding a negative previous sum is same as adding zero
        max_sum = nums[0]
        cur_sum = 0
        
        for num in nums:
            # see whether the previous sum is negative or not
            cur_sum = max(cur_sum, 0)
            # add current value to the previous sum
            cur_sum += num
            # update the maximum sum if the current sum is bigger
            max_sum = max(max_sum, cur_sum)
        
        return max_sum
    
def main():
    sol = Solution()
    
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(sol.maxSubArray(nums))
    
    nums = [1]
    print(sol.maxSubArray(nums))
    
    nums = [5,4,-1,7,8]
    print(sol.maxSubArray(nums))
    
if __name__ == "__main__":
    main()