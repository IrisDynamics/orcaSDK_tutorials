#include "actuator.h"
#include "TutorialHelpers.h"
#include "tools/log.h"

int main() {
	Actuator motor{ 0, "MyMotorName" };

	int com_port = obtain_serial_port_number();

	motor.set_new_serial_port(com_port);
	motor.open_serial_port();

	motor.enable_stream(); //Begin streaming

	Log log{ Log::TimestampType::DurationSinceOpening };
	OrcaError error = log.open("tutorial_log");
	if (error)
	{
		std::cout << error.what();
		return -1;
	}

	while (true) {
		motor.run(); // Adds a stream command if there isn't already outgoing data

		int32_t current_position = motor.stream_cache.position; //Using the stream cache, not a read
		std::string curr_position_str = "Current Position: " + std::to_string(current_position);

		log.write(curr_position_str);
		std::cout << curr_position_str << "                    \r";
	}

	return 0;
}