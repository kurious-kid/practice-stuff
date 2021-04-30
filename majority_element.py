class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		if (len(nums) == 1):
			return nums[0]

		the_table = {}
		max_times = int(len(nums) / 2)
		max_index = None
		for each_element in nums:
			if str(each_element) not in the_table:
				the_table[str(each_element)] = 1
			else:
				the_table[str(each_element)] += 1
				if (the_table[str(each_element)] > max_times):
					max_index = each_element
					break
		return max_index