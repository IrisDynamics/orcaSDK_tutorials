#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	OrcaError serial_port_error = motor.open_serial_port(serial_port);

	if (serial_port_error)
	{
		std::cout << "Error Detected! Message: " << serial_port_error.what() << "\n";
	}
	else
	{
		std::cout << "Serial port opened successfully!\n";
	}

	OrcaResult<int32_t> position_result = motor.get_position_um();

	if (position_result.error)
	{
		std::cout << "Error Getting Position! Message: " << position_result.error.what() << "\n";
	}
	else
	{
		std::cout << "Motor Position: " << position_result.value << "\n";
	}

	return 0;
}