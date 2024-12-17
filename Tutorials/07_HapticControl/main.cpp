#include "actuator.h"
#include "TutorialHelpers.h"
#include "tools/timer.h"
#include <cmath>

int main() {
	Actuator motor{ 0, "MyMotorName" };

	int com_port = obtain_serial_port_number();

	motor.set_new_serial_port(com_port);
	motor.open_serial_port();

	motor.clear_errors(); // Orca motors raise an error when communication stops during haptics mode

	motor.enable_stream();

	motor.set_mode(MotorMode::HapticMode); //Switch to haptic mode

	motor.update_haptic_stream_effects(Actuator::ConstF + Actuator::Spring0);

	motor.set_spring_effect( //Update spring parameters
		0,		//Spring ID (0 or 1)
		200,	//Spring strength
		40000	//Center position
	);

	Timer sin_wave_time_generator;
	constexpr float sin_wave_progression_per_ms = 0.01f; //Going to update constant force using a sin wave 
	constexpr int force_max_mN = 25000;

	while (true) {
		motor.run();

		float sin_input_progress = sin_wave_time_generator.time_elapsed() * sin_wave_progression_per_ms;

		motor.set_constant_force(std::sin(sin_input_progress) * force_max_mN); //Update constant force

		std::cout << "Current sensed force: " << motor.stream_cache.force <<  "                    \r";
	}

	return 0;
}