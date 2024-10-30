def brute_force(nums, k) -> bool:
    L = 0
    window = set()
    
    for R in range(len(nums)):
        if R - L >= k:
            window.remove(nums[L])
            L += 1
        
        if nums[R] in window:
            return True
        
        window.add(nums[R])
        
    return False

def main():
    nums = [1, 2, 3, 2, 3, 3]
    print(brute_force(nums, 3))
    
if __name__ == "__main__":
    main()