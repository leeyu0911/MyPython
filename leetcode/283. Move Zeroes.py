'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
'''

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        z_pointer = 0
        non_z_pointer = 0
        # i = 0
        while z_pointer < len(nums) and non_z_pointer < len(nums):
            # i += 1
        # for i in range(len(nums)):
            try:
                if nums[non_z_pointer] == 0:
                    non_z_pointer += 1
                if nums[z_pointer] != 0:
                    z_pointer += 1
                if nums[non_z_pointer] != 0 and nums[z_pointer] == 0 and (non_z_pointer > z_pointer):
                    nums[non_z_pointer], nums[z_pointer] = nums[z_pointer], nums[non_z_pointer]
                    non_z_pointer += 1
                    z_pointer += 1
                elif nums[non_z_pointer] != 0 and nums[z_pointer] == 0 and (non_z_pointer < z_pointer):
                    non_z_pointer += 1
            except IndexError:
                break
        # print(i)


nums = [0,1,0,3,12]
Solution.moveZeroes(0, nums)
print(nums)

nums = [0,0,1]
Solution.moveZeroes(0, nums)
print(nums)

nums = [0,0,0,1,2,3,0,0]
Solution.moveZeroes(0, nums)
print(nums)

nums = [1,0]
Solution.moveZeroes(0, nums)
print(nums)

nums = [1,0,1]
Solution.moveZeroes(0, nums)
print(nums)