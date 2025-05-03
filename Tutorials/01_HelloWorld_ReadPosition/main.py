from pyorcasdk import Actuator

motor = Actuator( "MyMotorName" )

serial_port = int(input("Please input the serial port of your connected motor. "))

motor.open_serial_port(serial_port)

while True:
    print("Current Position: " + str(motor.get_position_um().value), end="        \r")