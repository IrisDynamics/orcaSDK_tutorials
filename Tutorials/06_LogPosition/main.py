from pyorcasdk import Actuator
from time import time

motor = Actuator( "MyMotorName" )

serial_port = int(input("Please input the serial port of your connected motor. "))

motor.open_serial_port(serial_port)

with open("position_log.txt", "w") as log:
    start_time = time()

    while True:
        position = motor.get_position_um().value
        elapsed_time_seconds = time() - start_time
        log.write("{}: {}\n".format(
            round(elapsed_time_seconds, 4), 
            position)
            )
        print("Current Position: " + str(position), end="        \r")