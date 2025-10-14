from pyorcasdk import Actuator
import sys

motor = Actuator( "MyMotorName" )

serial_port = int(input("Please input the serial port of your connected motor. "))

serial_port_error = motor.open_serial_port(serial_port)

motor_errors_result = motor.get_errors()

if motor_errors_result.error:
	print("Failed to read active errors: " + motor_errors_result.error.what())
	sys.exit(1)

print("Active motor errors: " + motor_errors_result.value)

if (motor_errors_result.value & 1024):
    print("There is definitely an invalid supply voltage error!")