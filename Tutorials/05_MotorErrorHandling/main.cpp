#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"

using namespace orcaSDK;

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);

	OrcaResult<uint16_t> motor_errors_result = motor.get_errors();

	if (motor_errors_result.error)
	{
		std::cout << "Failed to read active errors: " << motor_errors_result.error.what() << "\n";
		return 1;
	}

	std::cout << "Active motor errors: " << motor_errors_result.value << "\n";

	if (motor_errors_result.value & ORCAReg::ERROR_0_Values::VOLTAGE_INVALID_Mask) std::cout << "There is definitely an invalid supply voltage error!" << "\n";

	return 0;
}