class Solution:
	def calPoints(self, ops: List[str]) -> int:

		the_stack = []

		for i in range(len(ops)):
			if (ops[i] == "+"):
				# print("prinitng stack before doing +\n")
				# print(the_stack)
				element_2 = the_stack.pop()
				element_1 = the_stack.pop()

				# print("element_1\n", element_1, "element_2\n", element_2)

				new_element = element_1 + element_2
				# print("new_element\n", new_element)

				the_stack.append(element_1)
				the_stack.append(element_2)
				the_stack.append(new_element)
			# print("the stack:\n", the_stack)

			elif (ops[i] == "D"):
				element = the_stack.pop()
				new_element = element * 2
				the_stack.append(element)
				the_stack.append(new_element)
			# print("the stack:\n", the_stack)

			elif (ops[i] == "C"):
				the_stack.pop()
			# print("the stack:\n", the_stack)

			else:
				the_stack.append(int(ops[i]))
			# print("the stack:\n", the_stack)

		return sum(the_stack)

