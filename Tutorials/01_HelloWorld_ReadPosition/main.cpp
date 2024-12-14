#include "actuator.h"
#include "TutorialHelpers.h"

int main() {
	Actuator motor{ 0, "MyMotorName" };

	int com_port = obtain_serial_port_number();

	motor.set_new_serial_port(com_port);
	motor.open_serial_port();
	
	while (true)
	{
		std::cout << "Current motor position: " << motor.get_position_um().value << "          \r";
	}

	return 0;
}