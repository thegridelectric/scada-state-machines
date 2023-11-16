from transitions import Machine

class StateMachineBase:
    # Define states
    states = ["Closed", "Open", "Closing", "Opening"]

    def __init__(self, model):
        self.machine = Machine(model=model, states=StateMachineBase.states, initial='Closed')
        
        # Add transitions
        
        
        self.machine.add_transition(trigger='stop_motor', source='Closing', dest='Closed')
        
        self.machine.add_transition(trigger='stop_motor', source='Opening', dest='Open')
        
        self.machine.add_transition(trigger='close_door', source='Open', dest='Closing')
        
        self.machine.add_transition(trigger='open_door', source='Closing', dest='Opening')
        self.machine.add_transition(trigger='open_door', source='Closed', dest='Opening')
