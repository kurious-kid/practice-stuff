class Solution:
	def nextGreaterElements(self, nums: List[int]) -> List[int]:
		the_stack = []
		the_output = [-1] * len(nums)

		for i in range(len(nums) * 2):
			while (len(the_stack) != 0 and (nums[the_stack[-1]] < nums[i % len(nums)])):
				the_output[the_stack.pop(-1)] = nums[i % len(nums)]

			if (i < len(nums)):
				the_stack.append(i)

		return the_output