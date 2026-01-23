# Motor Error Handling

In this tutorial we will learn about errors that the motor itself detects and reports, and how to handle them from the SDKs perspective.

## Prerequisites
 - We highly recommend reading the ORCA Series Reference Manual's section "Errors" before moving on. The reference manual can be found [on our downloads page](https://irisdynamics.com/downloads)
 - [SDK Error Handling](../04_ErrorHandling/README.md)

---

## Motor Errors Intro

Motor errors here refers to errors that an ORCA motor detects internally. They can arise when the motor detects a variety of situations which it deems incorrect for normal operation. As a safety precaution, when a motor error is active the motor will typically not output force or position until the error is cleared. 

These errors can be seen in the IrisControls GUI in the "Active Errors" field found in the status bar at the top of the window. When an error is active the value of this field will be a bright red. 

![voltage error](active_voltage_error.png "IrisControls displaying a 1024 error (Supply Voltage Invalid)")

This image shows a motor thats displaying a 1024 error. Upon reading the reference manual (or clicking the question mark button) we can determine that this error is reporting an invalid supply voltage. Indeed if we look at our "Voltage" field in the same status bar, we can see that our motor is detecting 1.48 volts, which is below the necessary supply voltage for operating an ORCA motor.

The image also displays a 1024 error in the "Latched Errors" field. This field is merely there to report all errors which have occured since the last time this register was cleared. A non-zero value listed here does not mean that your motor is actively encountering the errors listed.

## Detecting Errors with the SDK

We'll start with a stripped down version of tutorial 1:

```./main.cpp
#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"

using namespace orcaSDK ;

int main() {
	Actuator motor{ "MyMotorName" };

	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);

	return 0;
}
```

In order to access the active errors of a motor, we can call the `Actuator::get_errors()` member function.


```./main.cpp
	...
	OrcaResult<uint16_t> motor_errors_result = motor.get_errors();

	if (motor_errors_result.error)
	{
		std::cout << "Failed to read active errors: " << motor_errors_result.error.what() << "\n";
		return 1;
	}

	std::cout << "Active motor errors: " << motor_errors_result.value << "\n";
	...
```

> Note that motor errors are distinct from OrcaError objects handled in the SDK. If `motor_errors_result.error` evaluates to true in this code block, it means that there was an issue communicating with your motor, not that your motor itself has encountered an error. In this case, `motor_errors_result.value` is what contains the actual motor errors.

Give this code a try! Try running this program with the motor connected to an active power supply and with the motor unpowered. See how the results change!

## Extracting Individual Errors

There are multiple errors that your motor might encounter, and some of these errors may be encountered simultaneously. However, calling `Actuator::get_errors()` only returns one value. Each individual error is reported by a single bit/flag within the active errors register. As an example, this is what the error value would be if you were encountering both a 1024 (invalid voltage) and 512 (poor shaft quality) error at the same time:

![both voltage and shaft quality error](invalid_voltage_and_poor_shaft_quality.png "IrisControls displaying both a 1024 error (Supply Voltage Invalid) and a 512 error (Low Shaft Quality)")

If our code needs to detect when our motor has encountered an invalid supply voltage error but another error was present, then simply comparing the `Actuator::get_errors()` return value to the error we're interested in (1024) could fail. Because each error is reported using a single bit, extracting a specific error can be achieved by performing a bitwise AND on the error value with the error bit that you're interested in.

```./main.cpp
	...
	if (motor_errors_result.value & 1024) ... // GOOD: There is definitely a 1024 error
	if (motor_errors_result.value == 1024) ... // BAD: Will fail if multiple active errors
	...
```

## Clearing Active Errors

Because the motor will not produce force while active errors are present, any active errors will need to be cleared before the motor can be used again. 

Some errors are transient, and disappear when the condition that caused them to appear is removed. For example an invalid supply voltage error will disappear when the motor receives power from a valid power supply. 

Some errors, however, will remain active after the event that triggered them has passed. For example, if a motor has stopped operating due to exceeding its max temperature (error 64), then the error will need to be manually cleared after the motor has cooled down. 

These persistent errors can be cleared either by setting the motor to Sleep Mode, or by calling the `Actuator::clear_errors()` function. If either option is available to you, prefer setting the motor to sleep mode over calling `Actuator::clear_errors()` directly.

```./main.cpp
	...
	motor.set_mode(MotorMode::SleepMode); // Prefer this
	motor.clear_errors();                 // But this works too
	...
```