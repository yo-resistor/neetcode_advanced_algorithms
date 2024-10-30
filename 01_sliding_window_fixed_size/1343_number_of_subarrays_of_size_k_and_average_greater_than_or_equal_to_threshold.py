from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        total = 0.0
        count = 0
        
        for R in range(len(arr)):
            # if R is out of window, remove L pointer value
            # and move L pointer to the right by 1
            if R - L + 1 > k:
                total -= arr[L]
                L += 1
            
            # default action: add R pointer value to total
            total += arr[R]
            
            # for k size window subarrays,
            # if mean is greater or equal to the threshold, increase the count number
            if R - L + 1 == k and total / k >= threshold:
                count += 1
            
        return count
    
def main():
    sol = Solution()
    
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    print(sol.numOfSubarrays(arr, k, threshold))
    
    arr = [11,13,17,23,29,31,7,5,2,3]
    k = 3
    threshold = 5
    print(sol.numOfSubarrays(arr, k, threshold))
    
if __name__ == "__main__":
    main()