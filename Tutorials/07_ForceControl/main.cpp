#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"
#include "tools/timer.h"

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);

	motor.clear_errors(); // Orca motors raise an error when communication stops during force mode

	motor.enable_stream();

	motor.set_mode(MotorMode::ForceMode); //Switch to force mode

	Timer force_switch_timer;

	int force_to_command_mN = 10000;

	while (true) {
		motor.run();

		if (force_switch_timer.has_expired())
		{
			motor.set_streamed_force_mN(force_to_command_mN);
			force_switch_timer.set(5000);
			force_to_command_mN *= -1; // Flip the force direction
		}

		std::cout << "Current Sensed Force: " << motor.stream_cache.force << "                    \r";
	}

	return 0;
}