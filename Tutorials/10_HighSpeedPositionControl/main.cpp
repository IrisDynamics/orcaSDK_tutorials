#define _USE_MATH_DEFINES
#include <iostream>
#include "actuator.h"
#include "tools/timer.h"
#include "TutorialHelpers.h"
#include <cmath>

using namespace orcaSDK;

const int sine_offset = 35000;
const int amplitude = 25000;
const float frequency = 0.5;
const float milliseconds_to_seconds = 1000.0;

static int get_sine_target(const float time_elapsed)
{
    double two_pi_ft = 2 * M_PI * frequency * time_elapsed;
    double position_target = (amplitude * sin(two_pi_ft)) + sine_offset;
    return static_cast<int>(position_target);
}

int main() {
    Actuator motor{ "MyMotorName" };

    int serial_port = obtain_serial_port_number();

    motor.open_serial_port(serial_port, 1000000, 80);

    motor.set_mode(MotorMode::SleepMode);               

    motor.enable_stream();

    motor.set_mode(MotorMode::PositionMode);

    Timer sine_wave_timer;

    while (true) {

        motor.run();

        float time = sine_wave_timer.time_elapsed() / milliseconds_to_seconds;

        motor.set_streamed_position_um(get_sine_target(time));

        std::cout << "Current Position: " << motor.stream_cache.position << "           \r";
    }

    return 0;
}
