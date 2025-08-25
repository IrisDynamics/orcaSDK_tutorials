#include "actuator.h"
#include "TutorialHelpers.h"
#include <iostream>

using namespace orcaSDK;

const int auto_zero_error = 8192;
const int auto_zero_enabled = 2;
const int force_newtons = 30;
const int speed_mm_per_sec = 50;

void auto_zero_motor(Actuator motor)
{
    // zero mode - 2: auto zero enabled
    motor.write_register_blocking(ZERO_MODE, auto_zero_enabled);
    // at most 30 N of force is applied to move the motor
    motor.write_register_blocking(AUTO_ZERO_FORCE_N, force_newtons);
    // shaft speed moves up to 50 mmps while completing auto zeroing
    motor.write_register_blocking(AUTO_ZERO_SPEED_MMPS, speed_mm_per_sec);
    // motor will sleep after completing auto zeroing
    motor.write_register_blocking(AUTO_ZERO_EXIT_MODE, MotorMode::SleepMode);

    motor.set_mode(MotorMode::AutoZeroMode);
}

int main() {
    Actuator motor{ "MyMotorName" };

    int serial_port = obtain_serial_port_number();

    motor.open_serial_port(serial_port);

    motor.set_mode(MotorMode::SleepMode);

    auto_zero_motor(motor);

    while (true) {
        auto error_check = motor.get_errors();

        if (error_check.value & auto_zero_error) {
            std::cout << "\nAuto Zeroing Failed." << std::endl;
            return 0;
        }
        else if (motor.get_mode().value != MotorMode::AutoZeroMode) {
            std::cout << "\nAuto Zeroing Complete!" << std::endl;
            return 0;
        }
    }

    return 0;
}
