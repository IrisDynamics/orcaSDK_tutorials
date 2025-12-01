#include <iostream>

#include "orcaSDK/actuator.h"

using namespace orcaSDK;

int main() {
    Actuator motors[2]{ 
        { "ORCA" }, 
        { "ORCA2" } 
    };

    int serial_port;
    const int NUM_MOTORS = sizeof(motors) / sizeof(motors[0]);

    for (int i = 0; i < NUM_MOTORS; i++) {
        // for print formatting 
        if (i > 0) {
            std::cout << "\n\n";
        }
        std::cout << "Please input the serial port of your connected motor. " << motors[i].name << ": ";

        std::cin >> serial_port;

        auto error = motors[i].open_serial_port(serial_port);

        motors[i].enable_stream()

        if (error) {
            std::cout << "Error: " << error.what() << "\n";
        }
        else {
            std::cout << motors[i].name << " connected succesfully.";
        }
    }

    while (true) {

        for (int i = 0; i < NUM_MOTORS; i++) {
            motors[i].run();

            std::cout << "\nMotor " [i] << "Current Position: " << motors[i].get_stream_cache.position
            << "     \r";
        }
    }
    return 0;
}
