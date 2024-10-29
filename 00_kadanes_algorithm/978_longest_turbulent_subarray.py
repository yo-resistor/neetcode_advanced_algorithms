from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        return 0
    
def main():
    sol = Solution()
    
    arr = [9,4,2,10,7,8,8,1,9]
    print(sol.maxTurbulenceSize(arr))
    
    arr = [4,8,12,16]
    print(sol.maxTurbulenceSize(arr))
    
    arr = [100]
    print(sol.maxTurbulenceSize(arr))
    
if __name__ == "__main__":
    main()