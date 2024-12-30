#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"
#include "tools/log.h"

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);

	Log log{ Log::TimestampType::DurationSinceOpening };
	OrcaError error = log.open("tutorial_log");
	if (error) // Check to make sure we were able to open the file correctly
	{
		std::cout << error.what(); // Print out what went wrong
		return -1;
	}

	while (true) {
		int32_t current_position = motor.get_position_um().value;
		std::string curr_position_str = "Current Position: " + std::to_string(current_position);

		log.write(curr_position_str);
		std::cout << curr_position_str << "                    \r";
	}

	return 0;
}