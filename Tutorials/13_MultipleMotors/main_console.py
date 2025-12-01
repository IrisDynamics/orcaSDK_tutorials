from pyorcasdk import Actuator, MotorMode
from colorama import init, Fore


KINEMATIC_STATUS = 319


def digit_input(user_input):
    """
    Tests whether the entered input is a number, if not the attempted conversion raises a ValueError.

    Args:
        user_input: The input entered by the user.
    """
    return int(user_input)


def configure_motions(motors):
    """
    This function can be used to configure motions one and two.
    If this function is not used, the motor activates its saved motions.
    """
    for motor in motors:
        motor.set_kinematic_motion(0, 50000, 1000, 0, 1, False)
        motor.set_kinematic_motion(1, 10000, 1000, 0, 1, False)


def trigger_motion(motors, motion_id):
    """
    Activates Kinematic mode,
    Triggers the chosen motion,
    And reads the KINEMATIC_STATUS register to determine if the motion has finished for multiple motors.

    The last bit of the kinematic status register indicates whether the motion has completed.

    Args:
        motors (Actuator): The connected ORCA motors.
        motion_id (int): The user's chosen motion_id.
    """
    motion_complete = None

    for motor in motors:
        motor.set_mode(MotorMode.KinematicMode)
        motor.trigger_kinematic_motion(motion_id)

    while motion_complete != 0:
        for motor in motors:
            kin_status = motor.read_register_blocking(KINEMATIC_STATUS).value
            motion_complete = kin_status >> 15
            if motion_complete == 0:
                print("Motion Complete!")
                break


def sleep_orca(motors):
    """
    Puts motors into Sleep Mode.
    """
    for motor in motors:
        motor.set_mode(MotorMode.SleepMode)


def main():
    init()  # for colorama
    active_motion = None

    try:
        num_orcas = digit_input(
            input(Fore.GREEN + "How many motors would you like to test?: ")
        )

        motors = [Actuator(f"ORCA{i + 1}") for i in range(num_orcas)]

        print(
            Fore.WHITE + f"Testing {num_orcas} ORCAs\n"
            if num_orcas > 1
            else f"Testing {num_orcas} ORCA\n"
        )

        for i in range(num_orcas):
            com_port = digit_input(
                input(Fore.GREEN + f"COM port (RS422) for ORCA {i + 1}: ")
            )
            error = motors[i].open_serial_port(com_port)

            if error:
                print(Fore.WHITE + f"Error: {error.what()} \n")
            else:
                print(Fore.WHITE + f"Motor {i + 1} connected successfully! \n")

        # This is optional, but can be used to configure motor parameters
        configure_motions(motors)

        menu = [
            "\n   COMMAND   | DESCRIPTION",
            "   ----------------------------------",
            "   0 - 32    | Motion ID to activate",
            "   s         | Sleep ORCAs",
            "   q         | Quit program",
        ]
        print("\n".join(menu))

        while True:
            active_motion = input(Fore.GREEN + "\n>> Enter command: ")

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
