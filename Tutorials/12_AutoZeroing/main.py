from pyorcasdk import Actuator, MotorMode
import pyorcasdk.orca_registers as orca_reg

FORCE_NEWTONS = 30
SPEED_MM_PER_SEC = 50


def auto_zero_motor(motor):
    # zero mode - 2: auto zero enabled
    motor.write_register_blocking(orca_reg.ZERO_MODE, orca_reg.ZERO_MODE_AUTO_ZERO_ENABLED)
    # at most 30 N of force is applied to move the motor
    motor.write_register_blocking(orca_reg.AUTO_ZERO_FORCE_N, FORCE_NEWTONS)
    # shaft speed moves up to 50 mmps while completing auto zeroing
    motor.write_register_blocking(orca_reg.AUTO_ZERO_SPEED_MMPS, SPEED_MM_PER_SEC)
    # motor will sleep after completing auto zeroing
    motor.write_register_blocking(orca_reg.AUTO_ZERO_EXIT_MODE, MotorMode.SleepMode)

    motor.set_mode(MotorMode.AutoZeroMode)


motor = Actuator("MyMotorName")

serial_port = int(input("Please input the serial port of your connected motor. "))
serial_port_error = motor.open_serial_port(serial_port)

motor.set_mode(MotorMode.SleepMode)

auto_zero_motor(motor)

while True:
    error_check = motor.get_errors()
    # check if auto zero error is present, as part of greater check, in case other errors are encountered
    if error_check.value & orca_reg.ERROR_0_AUTO_ZERO_FAILED_Mask:
        print("Auto Zeroing Failed.")
        break
    elif motor.get_mode().value != MotorMode.AutoZeroMode:
        print("Auto Zeroing Complete!")
        break
