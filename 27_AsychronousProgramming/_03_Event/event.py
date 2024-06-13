class Event:
    def __init__(self) -> None:
        self.listners = []

    def register(self, listner):
        self.listners.append(listner)

    def unregister(self, listner):
        self.listners.remove(listner)

    def notify(self, *args, **kwargs):
        for listner in self.listners:
            listner(*args, **kwargs)
