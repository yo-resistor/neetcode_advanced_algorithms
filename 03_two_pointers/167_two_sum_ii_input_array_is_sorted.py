from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        
        while L < R:
            if numbers[L] + numbers[R] > target:
                R -= 1
            elif numbers[L] + numbers[R] < target:
                L += 1
            else:
                return [L + 1, R + 1]
    
def main():
    sol = Solution()
    
    numbers = [2,7,11,15]
    target = 9
    print(sol.twoSum(numbers, target))
    
    numbers = [2,3,4]
    target = 6
    print(sol.twoSum(numbers, target))
    
    numbers = [-1,0]
    target = -1
    print(sol.twoSum(numbers, target))
    
if __name__ == "__main__":
    main()