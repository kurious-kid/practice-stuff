class MyQueue:

	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self.stack_1 = []
		self.stack_2 = []

	def push(self, x: int) -> None:
		"""
		Push element x to the back of queue.
		"""
		if (len(self.stack_1) == 0):
			self.stack_2.append(x)

		else:
			self.stack_1.append(x)

	def pop(self) -> int:
		"""
		Removes the element from in front of queue and returns that element.
		"""
		to_be_popped = None
		if (len(self.stack_1) == 0):
			length = len(self.stack_2)

			for i in range(length):
				if (i == (length - 1)):
					to_be_popped = self.stack_2.pop()
				else:

					self.stack_1.append(self.stack_2.pop())

			for i in range(length - 1):
				self.stack_2.append(self.stack_1.pop())

		return to_be_popped

	def peek(self) -> int:
		"""
		Get the front element.
		"""
		the_peek = None
		if (len(self.stack_1) == 0):
			length = len(self.stack_2)
			for i in range(length):
				if (i == (length - 1)):
					the_peek = self.stack_2.pop()
					self.stack_1.append(the_peek)
				else:

					self.stack_1.append(self.stack_2.pop())

			for i in range(length):
				self.stack_2.append(self.stack_1.pop())

		return the_peek

	def empty(self) -> bool:
		"""
		Returns whether the queue is empty.
		"""
		if ((len(self.stack_1) == 0) and (len(self.stack_2) == 0)):
			return True
		return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()