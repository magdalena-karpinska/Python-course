# This elevator is telling the people that it's moving, but in reality it always stays in the same floor.
# 1. Update the current_floor property so that the elevator moves whenever it's called to do so. 

class Elevator:
    def __init__(self):
        self.current_floor = 0

    def go_to_floor(self, floor):
        if self.current_floor == floor:
            print(f"Elevator is in floor {floor}")
        else:
            print(f"Going to floor {floor}")
            self.current_floor = floor
     

elevator = Elevator()
elevator.go_to_floor(3)
elevator.go_to_floor(3)