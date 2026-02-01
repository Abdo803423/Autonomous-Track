from task_6_1 import Thermostat
cpu_monitor = Thermostat()
cpu_monitor.set_temperature(150)
print(cpu_monitor.get_temperature , cpu_monitor._target_temp)