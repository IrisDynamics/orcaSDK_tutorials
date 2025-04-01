#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"
#include "tools/timer.h"

using namespace orcaSDK;

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);

	//Motion that moves to position 50000 in 1000 milliseconds, then triggers motion 1
	motor.set_kinematic_motion(0, 50000, 1000, 0, 1, true, 1);
	//Motion that moves to position 10000 in 1000 milliseconds
	motor.set_kinematic_motion(1, 10000, 1000, 0, 1, false);
	motor.set_mode(MotorMode::KinematicMode);

	Timer trigger_kinematic_motion_timer;
	trigger_kinematic_motion_timer.set(5000);

	while (true) {		
		if (trigger_kinematic_motion_timer.has_expired()) {
			motor.trigger_kinematic_motion(0);
			trigger_kinematic_motion_timer.reset();
		}

		std::cout << "Current Position: " << motor.get_position_um().value << "                    \r";
	}

	return 0;
}
