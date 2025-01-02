# Trigger Kinematic Motions

In this tutorial we will set up an app that sets up and periodically triggers a small set of kinematic motions.

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

## Set up the kinematic motions

First we will set up our kinematic motions as we desire. We will define two motions with one linking into the other. This is the code for setting up these motions:

```./main.cpp
    ...
	motor.set_kinematic_motion(0, 50000, 1000, 0, 1, true, 1);
	motor.set_kinematic_motion(1, 10000, 1000, 0, 1, false);
    ...
```

That is a lot of parameters. Within those numbers is the definition for an Orca kinematic motion. Let's break down each parameter for the first motion:

```
	motor.set_kinematic_motion(
        0,     //The motion ID to be updated
        50000, //The position that this motion should move to
        1000,  //The time in milliseconds that the motion should take
        0,     //The delay in milliseconds after completing this motion before starting the next
        1,     //The motion shape (minimized power vs jerk)
        true,  //Whether this motion should link into another automatically
        1      //The motion ID that should be automatically linked to
    );    
```

Now describing this function call in english. We edit motion 0, to move to position 50000um in 1000ms, then without delay begin motion 1. The second statement is similar, but moves to position 10000um and doesn't link to another motion.

Next we need to switch to kinematic mode:

```./main.cpp
    ...
    motor.set_mode(MotorMode::KinematicMode);
    ...
```

This command switches the mode of operation. Switching to kinematic mode automatically executes the home motion of the motor. Try running the code and see what it does. If your motor's home motion hasn't been changed, it should execute the motions that we just defined.

## Repeat the kinematic motions

Now let's update the app to repeat the motion periodically. To do so we're going to use our library's Timer object. This object is an abstraction for simple timer operations. Here is the code that creates and sets up this object.

```./main.cpp
    ...
	Timer trigger_kinematic_motion_timer;
	trigger_kinematic_motion_timer.set(5000);
    ...
```

The first line constructs a Timer object, and the second begins the timer, with a time of 5000ms.

Now we need to check the Timer, and act on it when it expires.

```./main.cpp
    ...
    while (true) {
		if (trigger_kinematic_motion_timer.has_expired()) {
			motor.trigger_kinematic_motion(0);
			trigger_kinematic_motion_timer.reset();
		}

		std::cout << "Current Position: " << motor.get_position_um().value << "                \r";
    }
    ...
```

There are 3 functions introduced here. The function trigger_kinematic_motion_timer.has_expired() simply returns true if the last set timer has expired and false otherwise. The function trigger_kinematic_motion_timer.reset() sets the timer again with the last set duration.

The function that actually communicates with the motor to trigger a motion is motor.trigger_kinematic_motion(0). This function triggers the motion contained in the passed in parameter. In this case it triggers motion ID 0 to begin.

At this point the behaviour of the motor should be that it moves 40000mm in one direction and back, and it should repeat that motion every 5 seconds.