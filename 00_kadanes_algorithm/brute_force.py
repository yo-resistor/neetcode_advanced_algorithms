def brute_force(nums):
    # this method is using two pointers
    max_sum = nums[0]
    
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            max_sum = max(max_sum, cur_sum)
            
    return max_sum

def main():
    nums = [4, -1, 2, -7, 3, 4]
    print(brute_force(nums))
    
if __name__ == "__main__":
    main()