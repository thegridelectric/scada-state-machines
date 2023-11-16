import importlib

class StateMachineActions:
    def _invoke_handler(self, state_name, action):
        module_name = f"handlers.{state_name}Handler"
        handler_module = importlib.import_module(module_name)
        handler_function = getattr(handler_module, action, None)
        if handler_function:
            handler_function()


    def on_enter_Closed(self):
        self._invoke_handler('Closed', 'on_enter')
    def on_enter_Open(self):
        self._invoke_handler('Open', 'on_enter')
    def on_enter_Closing(self):
        self._invoke_handler('Closing', 'on_enter')
    def on_enter_Opening(self):
        self._invoke_handler('Opening', 'on_enter')