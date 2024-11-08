from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_prod, postfix_prod = 1, 1
        result = [1] * len(nums)
        
        for idx in range(len(nums)):
            result[idx] *= prefix_prod
            prefix_prod *= nums[idx]
            result[len(nums) - 1 - idx] *= postfix_prod
            postfix_prod *= nums[len(nums) - 1 - idx]
        
        return result
        
def main():
    sol = Solution()
    
    nums = [1,2,3,4]
    print(sol.productExceptSelf(nums))
    
    nums = [-1,1,0,-3,3]
    print(sol.productExceptSelf(nums))
    
if __name__ == "__main__":
    main()