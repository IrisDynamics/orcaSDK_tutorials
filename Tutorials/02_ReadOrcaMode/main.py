from pyorcasdk import Actuator, MotorMode

def main():
    motor = Actuator("MyMotorName")

    serial_port = int(input("Please input the serial port of your connected motor: "))

    motor.open_serial_port(serial_port)

    motor_mode_to_string_map = {
        MotorMode.SleepMode:        "Sleep",
        MotorMode.ForceMode:        "Force",
        MotorMode.PositionMode:     "Position",
        MotorMode.HapticMode:       "Haptic",
        MotorMode.KinematicMode:    "Kinematic",
    }

    while(True):
        print(motor_mode_to_string_map[motor.get_position_um().value] + "         \r")

if __name__ == "__main__":
    main()