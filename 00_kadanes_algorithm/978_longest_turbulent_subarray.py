from typing import List

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        L, R = 0, 1
        max_count = 1
        count = 1
        prev = ""
        
        while R < len(arr):
            if arr[R - 1] > arr[R] and prev != ">":
                count += 1
                max_count = max(count, max_count)
                R += 1
                prev = ">"
            elif arr[R - 1] < arr[R] and prev != "<":
                count += 1
                max_count = max(count, max_count)
                R += 1
                prev = "<"    
            else:
                R = R + 1 if arr[R] == arr[R - 1] else R
                L = R - 1
                count = 1
                prev = ""
        
        return max_count
    
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