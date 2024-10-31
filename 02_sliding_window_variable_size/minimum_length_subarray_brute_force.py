def brute_force(nums, target):
    L = 0
    min_count = float("inf")
    
    for L in range(len(nums)):
        total = 0
        for R in range(L, len(nums)):
            total += nums[R]
            if total >= target:
                min_count = min(min_count, R - L + 1)
                break
            
    return 0 if min_count == float("inf") else min_count

def sliding_window(nums, target):
    L = 0
    min_count = float("inf")
    total = 0
    
    for R in range(len(nums)):
        total += nums[R]
        while total >= target:
            min_count = min(min_count, R - L + 1)
            total -= nums[L]
            L += 1
    
    return 0 if min_count == float("inf") else min_count

def main():
    nums = [2, 3, 1, 2, 4, 3]
    print(sliding_window(nums, target=6))
    
if __name__ == "__main__":
    main()