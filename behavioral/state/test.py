from state_machine import GumballMachine


def run_tests():
	gumball_machine = GumballMachine(5)

	print(gumball_machine)
	gumball_machine.insert_quarter()
	gumball_machine.turn_crank()

	print(gumball_machine)
	gumball_machine.insert_quarter()
	gumball_machine.eject_quarter()
	gumball_machine.turn_crank()

	print(gumball_machine)
	gumball_machine.insert_quarter()
	gumball_machine.turn_crank()
	gumball_machine.insert_quarter()
	gumball_machine.turn_crank()
	gumball_machine.eject_quarter()

	print(gumball_machine)
	gumball_machine.refill(2)
	gumball_machine.insert_quarter()
	gumball_machine.turn_crank()

	print(gumball_machine)


if __name__ == "__main__":
	run_tests()
