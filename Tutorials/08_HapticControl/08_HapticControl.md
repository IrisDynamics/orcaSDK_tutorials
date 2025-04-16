# 08 - Haptic Control

In this tutorial we will demonstrate use of the haptics mode of Orca motors through the SDK. 

In this tutorial we will set up the motor to apply a spring effect, while also applying an additional oscillating force using a sin wave.

## Prerequisites
 - [Tutorial 07 - ForceControl](../07_ForceControl/07_ForceControl.md)
  
---

We'll start with a subset of the code from the [Force Control](../07_ForceControl/07_ForceControl.md) tutorial, once again edited to display the actively commanded force rather than the position.

```./main.cpp
#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"

using namespace orcaSDK;

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);

	motor.clear_errors();

	motor.enable_stream();

	motor.set_mode(MotorMode::ForceMode);

	while (true) {
		motor.run();

		std::cout << "Current Sensed Force: " << motor.stream_cache.force << "                    \r";
	}

	return 0;
}
```

## Set Up a Spring Effect 

First let's update the call to set_mode(), so that we enter haptic mode instead. 

```./main.cpp
	...
	motor.set_mode(MotorMode::HapticMode);
	...
```

When streaming in haptic mode, Orca motors require that the client regularly stream the current haptic effects that should be active. For now, let's update that to only include a spring effect.

```./main.cpp
	...
	motor.set_mode(MotorMode::HapticMode);

	motor.update_haptic_stream_effects(Actuator::Spring0);
	...
```

Try running the code, the motor should begin to apply a spring effect, with the parameters of the spring being whatever your saved default is for the motor.

Let's update the parameters of that spring effect to something that we desire.

```./main.cpp
	...
	motor.set_mode(MotorMode::HapticMode);

	motor.update_haptic_stream_effects(Actuator::Spring0);

	motor.set_spring_effect(
		0,		//Spring ID (0, 1, or 2)
		200,	//Spring strength
		40000	//Center position
	);
	...
```

Our program now enables a spring effect and controls its parameters.

## Add an Oscillation

Now let's update the code to add an oscillation effect. Haptics mode includes a variety of effects that can be layered on top of each other simultaneously. One of these are an oscillation effect which can apply a set of force signals which repeat themselves over time. First, let's update our streamed haptic effects.


```./main.cpp
	...
	motor.update_haptic_stream_effects(Actuator::Spring0 + Actuator::Osc0);
	...
```

Now we should have both a spring and an oscillator active. Next, similar to the spring, lets update the oscillator effect to have parameters we'd like.

```./main.cpp
	...
	motor.set_osc_effect(
		0,		//Oscillator ID (0 or 1)
		20,		//Oscillator max force (newtons)
		10,		//Frequency (decihertz),
		0,		//Duty cycle (unimportant for sin wave1)
		Actuator::OscillatorType::Sine
	);
	...
```

We now have a program that commands 2 haptic effects at once, with both configured as we'd like.