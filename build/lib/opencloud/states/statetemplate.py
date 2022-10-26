

import types


class StateTemplate:
	def __init__(self, state_name: str, start_function, stop_function, start_message: str, stop_message: str):
		if state_name:
			if isinstance(state_name, str):
				self.name = state_name
		else:
			pass


		if not start_message:
			self.start_message = f'{self.name} started'
		else:
			self.start_message = start_message


		if not stop_message:
			self.stop_message = f'{self.name} stopped'
		else:
			self.stop_message = stop_message
			

		if isinstance(start_function, types.FunctionType):
			self.start_function = start_function
		else:
			self.start_function = lambda: 0


		if isinstance(stop_function, types.FunctionType):
			self.stop_function = stop_function
		else:
			self.stop_function = lambda: 0


	def start(self):
		print(self.start_message)
		self.start_function()


	def stop(self):
		print(self.stop_message)
		self.stop_function()


	def getStateName(self):
		return self.name