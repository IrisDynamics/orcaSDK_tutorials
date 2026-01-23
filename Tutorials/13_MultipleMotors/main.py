from pyorcasdk import Actuator, MotorMode


KINEMATIC_STATUS = 319
NUM_ORCAS = 2


def trigger_motion(motors, motion_id):
    """
    Activates Kinematic mode,
    Triggers the chosen motion,
    And reads the KINEMATIC_STATUS register to determine if the motion has finished for multiple motors.

    Args:
        motors (Actuator): The connected ORCA motors.
        motion_id (int): The user's chosen motion_id.
    """
    motions_completed = [False, False]
    printed_complete = [False, False]

    for motor in motors:
        motor.trigger_kinematic_motion(0)
        motor.set_mode(MotorMode.KinematicMode)
        motor.trigger_kinematic_motion(motion_id)

    while all(motions_completed) != True:
        for index, motor in enumerate(motors):
            kin_status = motor.read_register_blocking(KINEMATIC_STATUS).value

            motion_complete = kin_status >> 15
            motion_number = kin_status & 0x7FFF

            if motion_complete == 0:
                motions_completed[index] = True

                if not printed_complete[index]:
                    print(f"Motor {index} Motion {motion_number} Complete!")
                    printed_complete[index] = True

def sleep_orca(motors):
    """
    Puts motors into Sleep Mode.
    """
    for motor in motors:
        motor.set_mode(MotorMode.SleepMode)


def main():
    active_motion = None

    try:
        motors = [Actuator(f"ORCA{i + 1}") for i in range(NUM_ORCAS)]

        print(
            f"\nTesting {NUM_ORCAS} ORCAs\n"
            if NUM_ORCAS > 1
            else f"\nTesting {NUM_ORCAS} ORCA\n"
        )

        for i in range(NUM_ORCAS):
            com_port = int(input(f"COM port (RS422) for ORCA {i + 1}: "))
            error = motors[i].open_serial_port(com_port)

            if error:
                print(f"Error: {error.what()} \n")
            else:
                print(f"Motor {i + 1} connected successfully! \n")

        menu = [
            "\n   INPUT    | DESCRIPTION",
            "   ----------------------------------",
            "   0 - 32    | Motion ID to activate",
            "   s         | Sleep ORCAs",
            "   q         | Quit program",
        ]
        print("\n".join(menu))

        while True:
            active_motion = input("\n>> Enter input: ")

            try:
                active_motion = int(active_motion)
            except ValueError:
                active_motion = active_motion.lower()

            match active_motion:
                case int() if 0 <= active_motion <= 32:
                    trigger_motion(motors, active_motion)
                case "s":
                    sleep_orca(motors)
                case "q":
                    break

    except ValueError:
        print(f"\nPlease enter a valid number \n")


if __name__ == "__main__":
    main()
