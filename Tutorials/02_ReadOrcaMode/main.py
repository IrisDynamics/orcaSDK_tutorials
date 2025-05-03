from pyorcasdk import Actuator, MotorMode

def motor_mode_to_string(mode_val):
    match mode_val:
        case MotorMode.SleepMode:
            return "Sleep"
        case MotorMode.ForceMode:
            return "Force"
        case MotorMode.PositionMode:
            return "Position"
        case MotorMode.HapticMode:
            return "Haptics"
        case MotorMode.KinematicMode:
            return "Kinematic"
        case _:
            return "Unknown"


motor = Actuator( "MyMotorName" )

serial_port = int(input("Please input the serial port of your connected motor. "))

motor.open_serial_port(serial_port)

while True:
    print("Current Mode: " + motor_mode_to_string(motor.get_mode().value), end="        \r")