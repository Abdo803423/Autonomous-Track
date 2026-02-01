class Thermostat:
    def __init__(self):
        self._target_temp =0.0
    def set_temperature(self, temp):
        if temp > 100:
            print("WARNING: Too Hot")
            self._target_temp = 100.0
        else:
             self._target_temp = temp
    def get_temperature(self):
        return self._target_temp