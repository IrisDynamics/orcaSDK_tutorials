#include "actuator.h"
#include "TutorialHelpers.h"
#include <iostream>

using namespace orcaSDK;

constexpr int force_newtons = 30;
constexpr int speed_mm_per_sec = 50;

void auto_zero_motor(Actuator motor)
{
    // zero mode - 2: auto zero enabled
    motor.write_register_blocking(ORCAReg::ZERO_MODE, ORCAReg::ZERO_MODE_Values::AUTO_ZERO_ENABLED);
    // at most 30 N of force is applied to move the motor
    motor.write_register_blocking(ORCAReg::AUTO_ZERO_FORCE_N, force_newtons);
    // shaft speed moves up to 50 mmps while completing auto zeroing
    motor.write_register_blocking(ORCAReg::AUTO_ZERO_SPEED_MMPS, speed_mm_per_sec);
    // motor will sleep after completing auto zeroing
    motor.write_register_blocking(ORCAReg::AUTO_ZERO_EXIT_MODE, MotorMode::SleepMode);

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

        if (error_check.value & ORCAReg::ERROR_0_Values::AUTO_ZERO_FAILED_Mask) {
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
