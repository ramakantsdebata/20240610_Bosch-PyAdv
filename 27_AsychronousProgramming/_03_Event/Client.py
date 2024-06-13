from subject import Subject

def listner1(state):
    print(f"Listner 1 received state change {state}")

def listner2(state):
    print(f"Listner 2 received state change {state}")


if __name__ == '__main__':
    subject = Subject()
    subject.on_state_change(listner1)
    subject.on_state_change(listner2)

    subject.state = "New State 1"
    subject.state = "New State 2"

    subject.remove_listner(listner1)

    subject.state = "New State 3"