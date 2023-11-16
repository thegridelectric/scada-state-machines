from StateMachine import StateMachine

def test_state_machine():
    machine = StateMachine()

    assert machine.state == "Closed"

# <MachineState><Name>Closed</Name><FromTransitions><FromTransition><FromStateName>Closed</FromStateName><ActionName>Open Door</ActionName><ToStateName>Opening</ToStateName></FromTransition></FromTransitions><ToTransitions><ToTransition><FromStateName>Closing</FromStateName><ActionName>Stop Motor</ActionName><ToStateName>Closed</ToStateName></ToTransition></ToTransitions></MachineState>.

        
    machine.open_door()
    assert machine.state == "Opening"
# <MachineState><Name>Opening</Name><FromTransitions><FromTransition><FromStateName>Opening</FromStateName><ActionName>Stop Motor</ActionName><ToStateName>Open</ToStateName></FromTransition></FromTransitions><ToTransitions><ToTransition><FromStateName>Closing</FromStateName><ActionName>Open Door</ActionName><ToStateName>Opening</ToStateName></ToTransition><ToTransition><FromStateName>Closed</FromStateName><ActionName>Open Door</ActionName><ToStateName>Opening</ToStateName></ToTransition></ToTransitions></MachineState>.

        
    machine.stop_motor()
    assert machine.state == "Open"
# <MachineState><Name>Open</Name><FromTransitions><FromTransition><FromStateName>Open</FromStateName><ActionName>Close Door</ActionName><ToStateName>Closing</ToStateName></FromTransition></FromTransitions><ToTransitions><ToTransition><FromStateName>Opening</FromStateName><ActionName>Stop Motor</ActionName><ToStateName>Open</ToStateName></ToTransition></ToTransitions></MachineState>.

        
    machine.close_door()
    assert machine.state == "Closing"
# <MachineState><Name>Closing</Name><FromTransitions><FromTransition><FromStateName>Closing</FromStateName><ActionName>Stop Motor</ActionName><ToStateName>Closed</ToStateName></FromTransition><FromTransition><FromStateName>Closing</FromStateName><ActionName>Open Door</ActionName><ToStateName>Opening</ToStateName></FromTransition></FromTransitions><ToTransitions><ToTransition><FromStateName>Open</FromStateName><ActionName>Close Door</ActionName><ToStateName>Closing</ToStateName></ToTransition></ToTransitions></MachineState>.

        
    machine.stop_motor()
    assert machine.state == "Closed"    
    print("All tests passed!")

if __name__ == "__main__":
    test_state_machine()
