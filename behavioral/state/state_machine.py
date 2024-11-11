from state import SoldOutState, NoQuarterState, HasQuarterState, SoldState

'''
The State Pattern allows an object to alter its behaviour when its internal state changes.
The object will appear to change its class 
'''

class GumballMachine:
	def __init__(self, count):
		self.sold_out_state = SoldOutState(self)
		self.no_quarter_state = NoQuarterState(self)
		self.has_quarter_state = HasQuarterState(self)
		self.sold_state = SoldState(self)

		self.count = count
		self.state = self.sold_out_state if count == 0 else self.no_quarter_state

	def insert_quarter(self):
		self.state.insert_quarter()

	def eject_quarter(self):
		self.state.eject_quarter()

	def turn_crank(self):
		self.state.turn_crank()
		self.state.dispense()

	def set_state(self, state):
		self.state = state

	def release_ball(self):
		if self.count > 0:
			print("A gumball comes rolling out the slot...")
			self.count -= 1

	def refill(self, count):
		self.count += count
		print(f"Machine refilled; new count is {self.count}.")
		self.set_state(self.no_quarter_state)

	def __str__(self):
		return f"Gumball Machine [Inventory: {self.count}, State: {self.state.__class__.__name__}]"
