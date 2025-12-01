from pyorcasdk import Actuator

motors = [Actuator("ORCA"), Actuator("ORCA2")]

for i, motor in enumerate(motors):
    serial_port = int(input(f"Please input the serial port of your connected motor. "))
    error = motors[i].open_serial_port(serial_port)

    motors[i].enable_stream()

    if error:
        print(f"Error: {error.what()} \n")
    else:
        print(f"Motor at index {i} connected succesfully.")
        
while True:
    motors[0].run()

    print("Current Position: " + str(motors[0].get_stream_data().position))
