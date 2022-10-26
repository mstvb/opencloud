

from opencloud.states import StateTemplate
from enum import Enum



class MessageType(Enum):

	TYPE_ERROR = '[ERROR] This State cannot using !!'
	NOT_FOUND = '[ERROR] Cannot found in States !!'
	NOT_START = '[ERROR] This State cannot starting !!'
	NOT_STOP = '[ERROR] Cannot stop a State !!'


class StateLoader:


	def __init__(self):
		self.states = dict() # VAL INFO - States with Name saved
		self.states_id = list() # VAL INFO - States with ID saved
		self.current_state = False # VAL INFO - Current State
		self.active = False # VAL INFO - Status of StateLoader


	def addState(self, state):
		if "start" and "stop" in dir(state): # IF STATEMENT - Check if Class has start / stop function
			self.states[state.name] = state # SET - add State to Dict for State Name
		else:
			raise Exception(MessageType.TYPE_ERROR.value)


	def setState(self, stateName: str, auto_start: bool = True):
		if stateName in self.states:
			self.stopState()
			self.current_state = self.states[stateName]
			if auto_start:
				self.active = True
				self.current_state.start()
			elif not auto_start:
				pass
		else:
			raise Exception(MessageType.NOT_FOUND.value)


	def startState(self):
		if self.current_state is not False and not self.active:
			self.current_state.start()
			self.active = True
		else:
			raise Exception(MessageType.NOT_START.value)


	def stopState(self):
		if self.current_state is not False and self.active:
			self.current_state.stop()
			self.active = False
		else:
			raise Exception(MessageType.NOT_STOP.value)


	def isExisted(self, stateName):
		return True if self.states[stateName] else False


	def isActive(self):
		return self.active