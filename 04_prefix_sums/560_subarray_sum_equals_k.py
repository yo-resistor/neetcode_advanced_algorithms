from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        hash_map = {0: 1}
        result = 0
        
        for num in nums:
            prefix += num
            
            if (prefix - k) in hash_map:
                result += hash_map[prefix - k]

            if prefix in hash_map:
                hash_map[prefix] += 1
            else:
                hash_map[prefix] = 1
            
        return result
        
def main():
    sol = Solution()
    
    nums = [1,1,1]
    k = 2
    print(sol.subarraySum(nums, k))
    
    nums = [1,2,3]
    k = 3
    print(sol.subarraySum(nums, k))
    
if __name__ == "__main__":
    main()