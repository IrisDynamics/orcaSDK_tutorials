from pyorcasdk import Actuator, MotorMode
import time

def main():
    motor = Actuator("MyMotorName")

    serial_port = int(input("Please input the serial port of your connected motor: "))

    motor.open_serial_port(serial_port)

	#Motion that moves to position 50000 in 1000 milliseconds, then triggers motion 1
    motor.set_kinematic_motion(0, 50000, 1000, 0, 1, True, 1)
	#Motion that moves to position 10000 in 1000 milliseconds
    motor.set_kinematic_motion(1, 10000, 1000, 0, 1, False)

    motor.set_mode(MotorMode.KinematicMode)

    start = time.time()

    while (True):
        now = time.time()
        if (now - start > 500):
            motor.trigger_kinematic_motion(0)
            start = time.time()
        
        print(motor.get_position_um().value + "         \r")



if __name__ == "__main__":
    main()