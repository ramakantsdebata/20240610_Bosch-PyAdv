from event import Event

class Subject:
    def __init__(self) -> None:
        self._event = Event()
        self._state = None

    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self._event.notify(self._state)

    def on_state_change(self, listner):
        self._event.register(listner)

    def remove_listner(self, listner):
        self._event.unregister(listner)