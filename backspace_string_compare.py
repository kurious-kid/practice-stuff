class Solution:
	def backspaceCompare(self, s: str, t: str) -> bool:
		stack_for_s = []
		stack_for_t = []

		for i in range(len(s)):
			if (len(stack_for_s) == 0 and (s[i] == '#')):
				continue

			else:
				if (s[i] == '#'):
					stack_for_s.pop()

				else:
					stack_for_s.append(s[i])

		# print("prinitng stack_for_s: \n", stack_for_s)

		for i in range(len(t)):
			if (len(stack_for_t) == 0 and (t[i] == '#')):
				continue

			else:
				if (t[i] == '#'):
					stack_for_t.pop()

				else:
					stack_for_t.append(t[i])

		# print("prinitng stack_for_t: \n", stack_for_t)

		if (len(stack_for_s) != len(stack_for_t)):
			return False

		else:
			for i in range(len(stack_for_s)):
				if (stack_for_s[i] != stack_for_t[i]):
					return False

			return True

