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
                elif nums[non_z_pointer] != 0 and nums[z_pointer] == 0 and (non_z_pointer < z_pointer):  # 感覺條件判斷可以更簡短一些
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


# https://leetcode.com/problems/move-zeroes/discuss/563197/Python-simple-solution-Faster-than-73.17
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first_zero = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[first_zero], nums[i] = nums[i], nums[first_zero]
                first_zero += 1


# https://leetcode.com/explore/other/card/30-day-leetcoding-challenge/528/week-1/3286/discuss/562750/Python-O(n)-solution
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first_zero_index = -1
        for i in range(len(nums)):
            if nums[i] == 0 and first_zero_index == -1:
                first_zero_index = i
            if nums[i] != 0 and first_zero_index != -1:
                nums[i], nums[first_zero_index] = nums[first_zero_index], nums[i]
                first_zero_index = first_zero_index + 1