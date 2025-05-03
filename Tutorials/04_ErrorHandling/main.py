from pyorcasdk import Actuator

motor = Actuator( "MyMotorName" )

serial_port = int(input("Please input the serial port of your connected motor. "))

serial_port_error = motor.open_serial_port(serial_port)

if serial_port_error:
    print("Error Detected! Message: " + serial_port_error.what())
else:
    print("Serial Port Opened Successfully")

position_result = motor.get_position_um()

if position_result.error:
    print("Error Getting Position! Message: " + position_result.error.what())
else:
    print("Current Position: " + str(position_result.value))