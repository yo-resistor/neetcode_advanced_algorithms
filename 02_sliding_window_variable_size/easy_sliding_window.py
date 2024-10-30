def sliding_window(nums):
    if len(nums) <= 0:
        return 0
    
    L = 0
    count = 0
    max_count = 0
    
    for R in range(len(nums)):
        if nums[L] == nums[R]:
            count +=1
        else:
            L = R
            count = 1
        
        max_count = max(count, max_count)
    
    return max_count

def sliding_window_neetcode(nums):
    length = 0
    L = 0
    
    for R in range(len(nums)):
        if nums[L] != nums[R]:
            L = R
        
        length = max(length, R - L + 1)
        
def main():
    nums = [4, 2, 2, 3, 3, 3]
    print(sliding_window(nums))
    
    nums = [1]
    print(sliding_window(nums))
    
    nums = []
    print(sliding_window(nums))

if __name__ == "__main__":
    main()