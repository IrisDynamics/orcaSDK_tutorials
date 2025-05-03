from pyorcasdk import Actuator, MotorMode
from time import time

motor = Actuator( "MyMotorName" )

serial_port = int(input("Please input the serial port of your connected motor. "))

motor.open_serial_port(serial_port)

motor.set_kinematic_motion(0, 50000, 1000, 0, 1, True, 1)
motor.set_kinematic_motion(1, 10000, 1000, 0, 1, False)
motor.set_mode(MotorMode.KinematicMode)

time_between_trigger_seconds = 5.0
last_trigger_kinematic_motion_time = time()

while True:
    if time() - last_trigger_kinematic_motion_time > time_between_trigger_seconds:
        motor.trigger_kinematic_motion(0)
        last_trigger_kinematic_motion_time = time()
    print("Current Position: " + str(motor.get_position_um().value), end="        \r")