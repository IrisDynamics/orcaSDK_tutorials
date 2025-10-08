from pyorcasdk import Actuator

motor = Actuator( "MyMotorName" )

serial_port = int(input("Please input the serial port of your connected motor. "))

motor.open_serial_port(serial_port)

motor.enable_stream()

while True:
    motor.run()

    print("Current Position: " + str(motor.get_stream_data().position), end="        \r")