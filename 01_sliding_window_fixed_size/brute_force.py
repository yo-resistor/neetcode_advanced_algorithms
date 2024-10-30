def brute_force(nums, k) -> bool:
    L = 0
    
    for L in range(len(nums)):
        for R in range(L + 1, min(len(nums), L + k)):
            if nums[L] == nums[R]:
                return True
    return False

def main():
    nums = [1, 2, 3, 2, 3, 3]
    print(brute_force(nums, 3))
    
if __name__ == "__main__":
    main()