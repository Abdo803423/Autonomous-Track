from task_9_1 import Vehicle
class SportsCar(Vehicle):
    def turbo_boost(self):
        self._speed *= 2
        print("TURBO ACTIVATED!")