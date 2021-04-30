class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		index = 0
		value = nums[0]

		for i in range(len(nums)):
			if (nums[i] == value):
				index += 1
			else:
				if (index == 0):
					value = nums[i]

				else:
					index -= 1

		return value