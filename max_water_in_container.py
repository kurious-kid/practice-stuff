class Solution:
	def maxArea(self, height: List[int]) -> int:
		max_so_far = 0
		area = 0
		i, j = 0, len(height) - 1

		while (i <= j):
			if (height[i] >= height[j]):
				area = (j - i) * (height[j])
				j = j - 1

			else:
				area = (j - i) * (height[i])
				i = i + 1

			if area > max_so_far:
				max_so_far = area

		return max_so_far