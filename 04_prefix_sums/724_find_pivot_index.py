from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # corner case:
        if len(nums) < 1:
            return -1
        
        # prefix_sum constructor
        prefix_sum = []
        total = 0
        for num in nums:
            total += num
            prefix_sum.append(total)
            
        # checker
        for ptr in range(len(nums)):
            prev_sum = prefix_sum[ptr - 1] if ptr > 0 else 0
            if (prefix_sum[-1] - nums[ptr]) / 2 == prev_sum:
                return ptr
        
        return -1
    
    
def main():
    sol = Solution()
    
    nums = [1,7,3,6,5,6]
    print(sol.pivotIndex(nums))
    
    nums = [1,2,3]
    print(sol.pivotIndex(nums))
    
    nums = [2,1,-1]
    print(sol.pivotIndex(nums))
    
if __name__ == "__main__":
    main()