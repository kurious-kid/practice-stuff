class MyStack:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.queue_1 = []
		self.queue_2 = []

	def push(self, x: int) -> None:
		"""
		Push element x onto stack.
		"""
		# print("in push")
		if (len(self.queue_2) == 0):
			self.queue_1.append(x)

		else:
			self.queue_2.append(x)

	# self.printstack()

	def pop(self) -> int:
		"""
		Removes the element on top of the stack and returns that element.
		"""
		# print("in pop")
		if (len(self.queue_2) == 0):
			for i in range(len(self.queue_1) - 1):
				self.queue_2.append(self.queue_1.pop(0))
			# self.printstack()
			return self.queue_1.pop(0)

		else:
			for i in range(len(self.queue_2) - 1):
				self.queue_1.append(self.queue_2.pop(0))
			# self.printstack()
			return self.queue_2.pop(0)

	def top(self) -> int:
		"""
		Get the top element.
		"""
		# print("in top")
		if (len(self.queue_2) == 0):
			length = len(self.queue_1)
			for i in range(length):
				if (len(self.queue_1) == 1):
					temp = self.queue_1.pop(0)
					self.queue_2.append(temp)
					# self.printstack()
					return temp
				else:
					self.queue_2.append(self.queue_1.pop(0))
				# self.printstack()


		else:
			length = len(self.queue_2)
			for i in range(length):
				if (len(self.queue_2) == 1):
					temp = self.queue_2.pop(0)
					self.queue_1.append(temp)
					# self.printstack()
					return temp
				else:
					self.queue_1.append(self.queue_2.pop(0))
				# self.printstack()

	def empty(self) -> bool:
		"""
		Returns whether the stack is empty.
		"""
		# print("in empty")
		if (len(self.queue_1) == 0 and len(self.queue_2) == 0):
			return True
		else:
			return False

	def printstack(self):
		print("############queue_1########")
		print(self.queue_1)
		print("###########################")

		print("$$$$$$$$$$$$$$queue_2$$$$$$$$$")
		print(self.queue_2)
		print("$$$$$$$$$$$$$$$$$$$$$$$")

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()