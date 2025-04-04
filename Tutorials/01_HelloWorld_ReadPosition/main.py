from pyorcasdk import Actuator, MotorMode


def main():
    motor = Actuator("MyMotorName")

    serial_port = "/dev/ttyUSB0"

    motor.open_serial_port(serial_port, 10000000)

    motor.get_force_mN()

    

    while(True):
        print(motor.get_position_um().value + "         \r")

if __name__ == "__main__":
    main()