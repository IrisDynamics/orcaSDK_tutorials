#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"
#include "tools/timer.h"
#include <cmath>

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);

	motor.clear_errors(); // Orca motors raise an error when communication stops during haptics mode

	motor.enable_stream();

	motor.set_mode(MotorMode::HapticMode); //Switch to haptic mode

	motor.update_haptic_stream_effects(Actuator::Osc0 + Actuator::Spring0);

	motor.set_spring_effect( //Update spring parameters
		0,		//Spring ID (0, 1, or 2)
		200,	//Spring strength 
		40000	//Center position
	);

	motor.set_osc_effect(
		0,		//Oscillator ID (0 or 1)
		20,		//Oscillator max force (newtons)
		10,		//Frequency (decihertz),
		0,		//Duty cycle (unimportant for sin wave1)
		Actuator::OscillatorType::Sine
	);

	while (true) {
		motor.run();

		std::cout << "Current Sensed Force: " << motor.stream_cache.force <<  "                    \r";
	}

	return 0;
}