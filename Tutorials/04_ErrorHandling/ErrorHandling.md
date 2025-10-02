# Error Handling

In this tutorial we will learn about the system that the SDK uses to report errors that occur.

---

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

## The OrcaError Object

Some functions in the SDK can fail. These functions will return one of two objects. If a function wouldn't normally return anything, but it has a chance of failure, it will instead return an OrcaError object. This OrcaError object will evaluate to true when converted to a boolean if an error has occurred. In this case, the object will contain an error message which can be accessed through the OrcaError::what() function. Actuator::open_serial_port() is a function that might fail, either in the case that the port doesn't exist, or if it is already in use by another program. Let's add error handling to our starting code.

```./main.cpp
	...
	OrcaError serial_port_error = motor.open_serial_port(serial_port);

	if (serial_port_error)
	{
		std::cout << "Error Detected! Message: " << serial_port_error.what() << "\n";
	}
	else
	{
		std::cout << "Serial port opened successfully!\n";
	}
	...
```

Try this code out! Try running your program, and instead of passing in your actual Orca's rs422 port number, pass in a random number instead.

## The OrcaResult Object

If a function can fail, but also must return a value, the function will instead return an OrcaResult object. These objects are simple structs containing an OrcaError and an object of whatever type the function would return for its 'happy path'. OrcaResult is a templated struct, so a full definition of any instance will look something along the lines of:

```
OrcaResult<uint16_t>
```

In this case, the OrcaResult contains an unsigned 16 bit integer.

To access the OrcaError object within the OrcaResult, check the OrcaResult::error member variable, and when you want to access the value object, instead check the OrcaResult::value member. Let's add an example showing use of an OrcaResult object.

```./main.cpp
	...
	OrcaResult<int32_t> position_result = motor.get_position_um();

	if (position_result.error)
	{
		std::cout << "Error Getting Position! Message: " << position_result.error.what() << "\n";
	}
	else
	{
		std::cout << "Motor Position: " << position_result.value << "\n";
	}
	...
```

In general, when handling errors for OrcaResults, it is wise to first check the error, and only access the value after confirming that an error hasn't occurred. We make no promise as to what will be contained in the OrcaResult::value member in case of an error, so using it blindly in a situation where error is possible may lead to unpredictable behaviour. 

In these tutorials, we often simply access the value from returned OrcaResult objects. This is for brevity in most cases, focusing on the content of the specific tutorial. For the purpose of tutorials, we will generally only handle errors in the case where not handling it may lead to more confusion. 

When writing your own code, we highly recommend handling all errors. Errors can arise due to a variety of situations, including misconfiguration, undiscovered bugs, faulty hardware, or instability of the underlying platform. For example, a Windows update may change your registry keys, updating the comport latency of your connected rs422 cable. This will be invisible to you, but will lead to communication instability. We have experienced errors like this. In general, assume that errors may occur, and handle them wherever using an incorrect or unpredictable value would lead to problems.