class Vehicle :
    def __init__(self):
        self._speed = 0.0
    def set_speed(self, s):
        self._speed = s
    def show_speed(self):
        print("Current Speed :" +str(self._speed))