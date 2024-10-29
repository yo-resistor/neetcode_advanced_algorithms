from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        return 0
    
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