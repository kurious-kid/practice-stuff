class Solution:
	def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
		the_map = {}
		the_stack = []

		for each_element in nums2:
			while (not (len(the_stack) == 0) and (the_stack[-1] < each_element)):
				the_map[str(the_stack.pop(-1))] = each_element

			the_stack.append(each_element)

		for i in range(len(nums1)):
			if (str(nums1[i]) not in the_map):
				nums1[i] = -1

			else:
				nums1[i] = the_map[str(nums1[i])]

		return nums1