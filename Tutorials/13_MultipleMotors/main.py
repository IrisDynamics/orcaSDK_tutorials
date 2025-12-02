from pyorcasdk import Actuator, MotorMode


KINEMATIC_STATUS = 319
NUM_ORCAS = 2


def digit_input(user_input):
    """
    Tests whether the entered input is a number, if not the attempted conversion raises a ValueError.

    Args:
        user_input: The input entered by the user.
    """
    return int(user_input)


def trigger_motion(motors, motion_id):
    """
    Activates Kinematic mode,
    Triggers the chosen motion,
    And reads the KINEMATIC_STATUS register to determine if the motion has finished for multiple motors.

    Args:
        motors (Actuator): The connected ORCA motors.
        motion_id (int): The user's chosen motion_id.
    """
    motion_complete = None
    motions_complete = 0

    for motor in motors:
        motor.set_mode(MotorMode.KinematicMode)
        motor.trigger_kinematic_motion(motion_id)

    while motion_complete != 0:
        for motor in motors:
            kin_status = motor.read_register_blocking(KINEMATIC_STATUS).value
            # the last bit of this register indicates whether the motion has completed
            motion_complete = kin_status >> 15
            # AND with 0b011111111111111 determines the active motion
            motion_number = kin_status & 0x7FFF
            if motion_complete == 0:
                motions_complete += 1
                if motions_complete == NUM_ORCAS:
                    print(f"Motion {motion_number} Complete!")


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
            com_port = digit_input(input(f"COM port (RS422) for ORCA {i + 1}: "))
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
                active_motion = digit_input(active_motion)
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
