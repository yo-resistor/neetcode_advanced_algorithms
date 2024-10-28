def sliding_window(nums):
    # https://www.notion.so/0-Kadane-s-Algorithm-129e0c5aec4081bda0d5c9524727da9a?pvs=4
    # if the previous sum is negative, we move the left pointer to the right pointer location
    # assumption: there is only one result with no ties
    max_sum = nums[0]
    cur_sum = 0
    max_L, max_R = 0, 0
    L, R = 0, 0
    
    for R in range(len(nums)):
        # if the previous sum is negative, move the left pointer to the right pointer's location
        if cur_sum < 0:
            L = R
        
        # update the current sum by adding current value to the previous sum    
        cur_sum += nums[R]
        
        # if the current sum is higher than the maximum sum, update it to the maximum sum
        # update the max_L, max_R pointers as well
        if cur_sum > max_sum:
            max_sum = cur_sum
            max_L, max_R = L, R
            
    return [max_L, max_R]

def main():
    nums = [4, -1, 2, -7, 3, 4]
    print(sliding_window(nums))
    
if __name__ == "__main__":
    main()