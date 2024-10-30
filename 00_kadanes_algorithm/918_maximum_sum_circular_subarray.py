from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_max, curr_min = 0, 0
        glob_max, glob_min = nums[0], nums[0]
        total = 0
        
        for num in nums:
            total += num
            curr_max = max(curr_max + num, num)
            curr_min = min(curr_min + num, num)
            glob_max = max(glob_max, curr_max)
            glob_min = min(glob_min, curr_min)
            
        return max(glob_max, total - glob_min) if glob_max > 0 else glob_max
    
def main():
    sol = Solution()
    
    nums = [1,-2,3,-2]
    print(sol.maxSubarraySumCircular(nums))
    
    nums = [5,-3,5]
    print(sol.maxSubarraySumCircular(nums))
    
    nums = [-3,-2,-3]
    print(sol.maxSubarraySumCircular(nums))
    
if __name__ == "__main__":
    main()