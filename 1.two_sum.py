class Solution:
    def twoSum(self, nums, target):
        #outer loop of the soln
        for a in range(len(nums)):
            #inner loop that enables the subsequent additions
            for b in range(a + 1, len(nums)):
                sum = nums[a] + nums[b]
                if sum == target:
                    return [a, b] 
