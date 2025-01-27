#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"

using namespace orcaSDK;

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);
	
	while (true)
	{
		std::cout << "Current Position: " << motor.get_position_um().value << "          \r";
	}

	return 0;
}