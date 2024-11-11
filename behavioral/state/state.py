from abc import ABC, abstractmethod


# State Interface
class State(ABC):
	@abstractmethod
	def insert_quarter(self):
		pass

	@abstractmethod
	def eject_quarter(self):
		pass

	@abstractmethod
	def turn_crank(self):
		pass

	@abstractmethod
	def dispense(self):
		pass


# Concrete States
class SoldOutState(State):
	def __init__(self, gumball_machine):
		self.gumball_machine = gumball_machine

	def insert_quarter(self):
		print("Machine is sold out. You can't insert a quarter.")

	def eject_quarter(self):
		print("You can't eject. No quarter inserted.")

	def turn_crank(self):
		print("You turned, but there's no gumballs.")

	def dispense(self):
		print("No gumball dispensed.")


class NoQuarterState(State):
	def __init__(self, gumball_machine):
		self.gumball_machine = gumball_machine

	def insert_quarter(self):
		print("Quarter inserted.")
		self.gumball_machine.set_state(self.gumball_machine.has_quarter_state)

	def eject_quarter(self):
		print("No quarter to eject.")

	def turn_crank(self):
		print("You turned, but there's no quarter.")

	def dispense(self):
		print("You need to pay first.")


class HasQuarterState(State):
	def __init__(self, gumball_machine):
		self.gumball_machine = gumball_machine

	def insert_quarter(self):
		print("You can't insert another quarter.")

	def eject_quarter(self):
		print("Quarter returned.")
		self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)

	def turn_crank(self):
		print("You turned the crank...")
		self.gumball_machine.set_state(self.gumball_machine.sold_state)

	def dispense(self):
		print("No gumball dispensed.")


class SoldState(State):
	def __init__(self, gumball_machine):
		self.gumball_machine = gumball_machine

	def insert_quarter(self):
		print("Please wait, we're already giving you a gumball.")

	def eject_quarter(self):
		print("Sorry, you already turned the crank.")

	def turn_crank(self):
		print("Turning twice doesn't get you another gumball!")

	def dispense(self):
		self.gumball_machine.release_ball()
		if self.gumball_machine.count > 0:
			self.gumball_machine.set_state(self.gumball_machine.no_quarter_state)
		else:
			print("Oops, out of gumballs!")
			self.gumball_machine.set_state(self.gumball_machine.sold_out_state)
