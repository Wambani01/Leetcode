#!/usr/bin/python3
import time

class Solution:
    def two_sum(target, nums):
        return [index for index, value in enumerate(nums) if (target - value) in nums]

if __name__ == "__main__":
    start = time.time()
    nums = [7, 8, 3, 9, 66, 0]
    print(Solution.two_sum(7, nums))
    end = time.time()
    print("The time is: {}".format(end - start))
