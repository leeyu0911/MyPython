'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''


class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        if k < len(nums) and k > 0:
            n1 = nums[-k:len(nums):1]
            n2 = nums[0:len(nums) - k:1]
            nums[:] = n1 + n2
            return nums

        elif k > len(nums) and k % len(nums) != 0:
            k = k % len(nums)
            n1 = nums[-k:len(nums):1]
            n2 = nums[0:len(nums) - k:1]
            nums[:] = n1 + n2
            return nums

        '''
        A little important thing to be cautious:

        nums[:] = nums[n-k:] + nums[:n-k] 
        can't be written as:

        nums = nums[n-k:] + nums[:n-k]
        on the OJ.

        The previous one can truly change the value of old nums, 
        but the following one just changes its reference to a new nums not the value of old nums.
        '''

if __name__ == "__main__":
    print(Solution.rotate(123, [1, 2, 3, 4, 5, 6, 7], 3))
    n1 = [1, 2, 3]
    n2 = [0, 4, 5]
    n3 = n1.insert(len(n1), "n2")
    print(n3)
    nums = [1, 2, 3, 4]
    print(nums[0:1])

'''
34 / 34 个通过测试用例
状态：通过
执行用时：32 ms
内存消耗：13.8 MB
'''