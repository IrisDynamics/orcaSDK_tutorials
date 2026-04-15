from pyorcasdk import Actuator, MotorMode


KINEMATIC_STATUS = 319

def check_num_orcas():
    num_orcas = int(input(f"How many ORCA motors are you testing? "))
    if num_orcas < 0 or isinstance(num_orcas, str):
        raise ValueError("Can't use a letter or negative number")
    return num_orcas


def trigger_motion(motors, motion_id, num_orcas):
    """
    Activates Kinematic mode,
    Triggers the chosen motion,
    And reads the KINEMATIC_STATUS register to determine if the motion has finished for multiple motors.

    Args:
        motors (Actuator): The connected ORCA motors.
        motion_id (int): The user's chosen motion_id.
    """
    motions_completed = [False] * num_orcas
    printed_complete = [False] * num_orcas

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
                    print(f"Motor {index + 1} Motion {motion_number} Complete!")
                    printed_complete[index] = True
                break

def sleep_orca(motors):
    """
    Puts motors into Sleep Mode.
    """
    for motor in motors:
        motor.set_mode(MotorMode.SleepMode)


def main():
    active_motion = None

    try:
        num_orcas = check_num_orcas()
        motors = [Actuator(f"ORCA{i + 1}") for i in range(num_orcas)]

        print(
            f"\nTesting {num_orcas} ORCAs\n"
            if num_orcas > 1
            else f"\nTesting {num_orcas} ORCA\n"
        )

        for i in range(num_orcas):
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
                parsed_str = active_motion.lower()

                if isinstance(active_motion, str) and active_motion in ("s", "q"):
                    active_motion = parsed_str
                else:
                    active_motion = int(active_motion)

                    match active_motion:
                        case int() if 0 <= active_motion <= 32:
                            trigger_motion(motors, active_motion, num_orcas)
                        case "s":
                            sleep_orca(motors)
                        case "q":
                            sleep_orca(motors)
                            break

            except ValueError:
                print(f'Invalid Input: {active_motion}\n')
            except KeyboardInterrupt:
                print("\nSIGINT received! Sleeping Motor(s)")
                sleep_orca(motors)

    except ValueError as e:
        print(f"\nPlease enter a valid number: {e} \n")


if __name__ == "__main__":
    main()
