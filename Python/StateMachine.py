from StateMachineActions import StateMachineActions
from StateMachineBase import StateMachineBase


class StateMachine(StateMachineActions):
    def __init__(self):
        self.state_machine = StateMachineBase(self)