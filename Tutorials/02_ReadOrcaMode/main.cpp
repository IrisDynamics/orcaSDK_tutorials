#include "actuator.h" 
#include "TutorialHelpers.h"

std::string motor_mode_to_string(int mode_val) {
	switch (mode_val) {
	case MotorMode::SleepMode:
		return "Sleep";
	case MotorMode::ForceMode:
		return "Force";
	case MotorMode::PositionMode:
		return "Position";
	case MotorMode::HapticMode:
		return "Haptics";
	case MotorMode::KinematicMode:
		return "Kinematic";
	default:
		return "Unknown";
	}
}

int main() {
	Actuator motor{ 0, "MyMotorName" };

	int com_port = obtain_serial_port_number();

	motor.set_new_serial_port(com_port);
	motor.open_serial_port();

	while (true) {
		std::cout << "Current Mode: " << motor_mode_to_string(motor.get_mode().value) << "                 \r";
	}

	return 0;
}