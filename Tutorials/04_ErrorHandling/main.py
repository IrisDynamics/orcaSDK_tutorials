from pyorcasdk import Actuator
import time

def main():
    motor = Actuator("MyMotorName")

    serial_port = int(input("Please input the serial port of your connected motor: "))

    err = motor.open_serial_port(serial_port)

    if (err):
        print("Error Detected! Message: " + err.what())
    else:
        print("Serial port opened successfully!")
    
    res = motor.get_position_um()

    if (res.error):
        print("Error Getting Position! Message: " + res.error.what())
    else:
        print(res.value)


if __name__ == "__main__":
    main()