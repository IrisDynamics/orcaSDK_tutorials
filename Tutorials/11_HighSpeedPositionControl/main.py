from pyorcasdk import Actuator, MotorMode
from time import time
from math import sin, pi

motor = Actuator( "MyMotorName" )
SINE_OFFSET = 35000
AMPLITUDE = 25000
FREQUENCY = 0.5

serial_port = int(input("Please input the serial port of your connected motor. "))

motor.open_serial_port(serial_port, 1000000, 80)

motor.set_mode(MotorMode.SleepMode)

motor.enable_stream()

motor.set_mode(MotorMode.PositionMode)

def get_sine_target() -> int:
    curr_time = time()
    two_pi_ft = 2 * pi * FREQUENCY * curr_time
    position_target = (AMPLITUDE * sin(two_pi_ft)) + SINE_OFFSET
    return int(position_target)

while True:
    motor.run()

    motor.set_streamed_position_um(get_sine_target())
    
    print("Current Position: " + str(motor.get_stream_data().position), end="        \r")