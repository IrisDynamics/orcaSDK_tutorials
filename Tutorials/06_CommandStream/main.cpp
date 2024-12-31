#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);

	motor.enable_stream(); //Begin streaming

	while (true) {
		motor.run(); // Adds a stream command if there isn't already outgoing data

		//Note: Using motor.stream_cache.position rather than motor.get_position_um()
		std::cout << "Current Position: " << motor.stream_cache.position << "             \r";
	}

	return 0;
}