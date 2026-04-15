from pyorcasdk import Actuator, MotorMode


KINEMATIC_STATUS = 319
NUM_ORCAS = 2

def sleep_orca(motors):
    for motor in motors:
        motor.set_mode(MotorMode.SleepMode)

motors = [Actuator(f"ORCA{i + 1}") for i in range(NUM_ORCAS)]

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
        parsed_str = active_motion.lower()

        if isinstance(active_motion, str) and active_motion in ("s", "q"):
            active_motion = parsed_str
        else:
            active_motion = int(active_motion)

            match active_motion:
                case int() if 0 <= active_motion <= 32:
                    for motor in motors:
                        motor.trigger_kinematic_motion(0)
                        motor.set_mode(MotorMode.KinematicMode)
                        motor.trigger_kinematic_motion(active_motion)
                case "s":
                    sleep_orca(motors)
                case "q":
                    sleep_orca(motors)
                    break
                
    except ValueError:
        print(f'Invalid input: {active_motion}')

    except KeyboardInterrupt:
        print("\nSIGINT received! Sleeping Motor(s)")
        sleep_orca(motors)


