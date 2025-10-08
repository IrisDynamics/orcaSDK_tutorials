from pyorcasdk import Actuator, MotorMode
from time import time

motor = Actuator( "MyMotorName" )

serial_port = int(input("Please input the serial port of your connected motor. "))

motor.open_serial_port(serial_port)

motor.clear_errors()

motor.enable_stream()

motor.set_mode(MotorMode.ForceMode)

force_switch_time = 5.000 
force_to_command_mN = 10000

last_force_switch_time = time()

while True:
    motor.run()

    if (time() - last_force_switch_time) > force_switch_time:
        motor.set_streamed_force_mN(force_to_command_mN)
        last_force_switch_time = time()
        force_to_command_mN *= -1
    
    print("Current Position: " + str(motor.get_stream_data().position), end="        \r")