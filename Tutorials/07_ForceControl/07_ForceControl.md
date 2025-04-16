# 07 - Force Control

In this tutorial we will demonstrate use of the force control mode of Orca motors. 

After giving a force command to the motor, we'll update the code to swap what direction the force is applied periodically.

## Prerequisites
 - [Tutorial 03 - TriggerKinematicMotions](../03_TriggerKinematicMotions/03_TriggerKinematicMotions.md)
 - [Tutorial 06 - CommandStream](../06_CommandStream/06_CommandStream.md)
  
---

We start with the source code from the command stream tutorial, except for a small change. Instead of reading the position value from the stream cache, we'll print out the force value from the stream cache.

```./main.cpp
#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"

using namespace orcaSDK;

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);
	
	motor.enable_stream();

	while (true)
	{
		motor.run();

		std::cout << "Current Sensed Force: " << motor.stream_cache.force << "          \r";
	}

	return 0;
}
```

## Command a Force

To begin, let's give the motor a command to set itself into force mode.

```./main.cpp
	...
	motor.enable_stream();

	motor.set_mode(MotorMode::ForceMode);
	...
```

At this point the motor is ready to receive force commands. Let's give it one.

```./main.cpp
	...
	motor.enable_stream();

	motor.set_mode(MotorMode::ForceMode);

	motor.set_streamed_force_mN(10000);
	...
```

Try running the program, you should notice that the shaft moves. Also your console should be printing something close to the force you commanded. Try opening IrisControls. It should display that you are in force mode, and that it's detecting a force of around 10 newtons.

Now close your program and run it again. This time you may notice that the shaft does not move. Take a look again at IrisControls. It should be displaying that an error has occurred, particularly a "comms timeout". Orca modes that are controlled via a command stream require that regular communication happens with the motor, else it will stop exerting force. This is a safety feature. When actively giving a motor commands, any stops in communication are interpreted as a failure or shutdown of the system at large.

In order to resolve this issue, lets clear errors before beginning. This will allow the program to run again.

```./main.cpp
	...
	motor.clear_errors();

	motor.set_mode(MotorMode::ForceMode);
	...
```

After adding this command in, your program should run as normal again.

## Swap Force Direction

Now let's update the code to swap force direction periodically. We will do this using the Timer object again, similar to how we did during the [Kinematic Motion](../03_TriggerKinematicMotions/03_TriggerKinematicMotions.md) tutorial. A difference here is it will be set up so it expires immediately.

Let's set up the Timer object and make it reset itself every 5 seconds.

```./main.cpp
	...
	Timer switch_force_direction_timer;

	while (true) {
		motor.run();

		if (switch_force_direction_timer.has_expired()) {
			//Switch force direction
			switch_force_direction_timer.set(5000);
		}

		std::cout << "Current Sensed Force: " << motor.stream_cache.force << "          \r";
	}
	...
```

Now all we need to do is include the code that swaps the direction. We'll do that by flipping the sign of a variable and updating the streamed command whenever the timer resets.


```./main.cpp
	...
	Timer switch_force_direction_timer;

	int force_to_command = 10000;

	while (true) {
		motor.run();
		
		if (switch_force_direction_timer.has_expired()) {
			motor.set_streamed_force_mN(force_to_command_mN);
			switch_force_direction_timer.set(5000);
			force_to_command *= -1;
		}

		std::cout << "Current Sensed Force: " << motor.stream_cache.force << "          \r";
	}
	...
```

Now we should have code that applies 10 newtons in either direction, swapping periodically. As a final step, to clean up our code we can remove the initial set_streamed_force_mN() call, since our timer expires immediately, and thus updates our force command immediately.