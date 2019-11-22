class StateMachine:
    def __init__(self):
        self.handlers = {}
        self.startState = None
        self.endStates = []
        self.time=0

    def add_state(self, name, handler, end_state=0):
        name = name.upper()
        self.handlers[name] = handler
        if end_state:
            self.endStates.append(name)

    def set_start(self, name):
        self.startState = name.upper()

    def run(self, cargo):
        try:
            handler = self.handlers[self.startState]
        except:
            raise InitializationError("must call .set_start() before .run()")
        if not self.endStates:
            raise InitializationError("at least one state must be an end_state")
        while True:
            (newState, cargo, self.time) = handler(cargo,self.time)
            if len(cargo) == 0:
                # self.time=0
                if newState.upper() in self.endStates:
                    print("reached ", newState)
                    return newState
                else:
                    print("Error:", newState, "is geen endstate.")
                    return newState
            else:
                handler = self.handlers[newState.upper()]