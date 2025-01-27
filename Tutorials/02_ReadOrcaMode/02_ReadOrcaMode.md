# 02 - Read Orca Mode

In this tutorial we will adjust the basic app to display whatever mode the Orca is currently in.

We begin with the source code from tutorial 1:

```./main.cpp
#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"

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
```

To access the current motor mode, we'll just update one line. Instead of asking for the motor's position, we'll instead ask for its mode. The function that we will use is Actuator::get_mode(). The updated line of code looks like this:

```./main.cpp
	std::cout << "Current Mode: " << motor.get_mode().value << "              \r";
```

Try running the program. Try opening IrisControls and switch between Kinematic, Haptic, and Sleep modes! 

You may notice that instead of printing any string, like "Sleep Mode" or "Force Mode" it is instead printing a number. This is because each mode is encoded in the motor as an integer. There is an enum in the SDK called MotorMode that shows which mode corresponds to which integer. Let's add a helper function which converts these integers into names:

```./main.cpp
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
```

This function is defined using a switch statement with one definition for each common motor mode. Let's apply it to our printing statement:

```./main.cpp
...
	std::cout << "Current Mode: " << motor_mode_to_string(motor.get_mode().value) << "                 \r";
...
```

Our program should now give nicer, more readable output.