# 01 - Hello World / Read Position

In this tutorial we will set up the most basic app that demonstrates communication with your Orca motor. The end goal of this tutorial is an application which reads and displays the sensed position of a connected Orca motor.

## The Source Code

To begin let's start with the source file that we used but didn't explain back in the orcaSDK's README.md

```./main.cpp
#include <iostream>
#include "actuator.h"

using namespace orcaSDK;

int main()
{
	Actuator motor{ "MotorName" };
	std::cout << "Hello World\n";
	return 0;
}
```

This file is largely identical to an implementation of a C++ "Hello World", but here we've included an additional header and constructed an object.

```main.cpp
#include "actuator.h"
```

This line includes the header which contains the declaration of the main object in the SDK, the Actuator object. This object is our abstraction for an Orca linear motor.

```main.cpp
using namespace orcaSDK;
```

To avoid potential name conflicts with other libraries or user-defined code, the entire SDK is encapsulated within its own namespace, orcaSDK. By including this line, we explicitly specify that we want to operate within the orcaSDK namespace. This allows us to call its methods and members directly without needing to prefix them with orcaSDK::. However, it's important to note that adding this line in header files can be potentially dangerous. Any file that includes such a header will automatically inherit the namespace, which can lead to unexpected behavior or conflicts. For this reason, it is generally recommended to avoid using using namespace in header files and instead fully qualify names when necessary.

```main.cpp
	Actuator motor{ "MotorName" };
```

This line constructs an Actuator object and assigns it to the variable "motor". Inside the curly braces is the one parameter that the motor requires. This parameter assigns the object's name, which can retrieved via the member variable Actuator::name. 

At this point we now have a virtual representation of an Orca motor, but it isn't yet connected to a physical motor. To give it the information it needs to connect to the actual motor, update your file to include the following line.

```./main.cpp
#include <iostream>
#include "actuator.h"

int main()
{
	Actuator motor{ "MotorName" };

	motor.open_serial_port(<your_com_port_number_here>);

	std::cout << "Hello World\n";
	return 0;
}
```

The motor.open_serial_port() function triggers the Actuator object to obtain the serial port indicated by the passed in parameter. For this function, pass in the COM port number of your motor's rs422 cable.

After calling this method, you now have not only a virtual representation of your Orca, but a representation that is now connected to your actual motor.

Finally, let's get some information out of the motor. The most common information needed from the motor is its position, so that's what we'll read. To display the active position of the motor, add the following lines.

```./main.cpp
#include <iostream>
#include "actuator.h"

int main()
{
	Actuator motor{ "MotorName" };

	motor.open_serial_port(<your_com_port_number_here>);

	std::cout << "Hello World\n";

	while(true) {
		std::cout << "Current Position: " << motor.get_position_um().value << "          \r";
	}

	return 0;
}
```

The new code we've added is in an infinite loop, because of this, it will continue to run until we manually interrupt the program. Very often it is the case that code interacting with our motors runs in some form of an infinite loop or another. In general, it is wise to include some method of escape from the loop, but we ignore that for now.

The only line being executed inside this loop is a line that prints info to the output console. From this line, the only command that we're particularly interested in is

```./main.cpp
	... << motor.get_position_um().value << ...
```

The function motor.get_position_um() is a blocking command that requests the current shaft position from the motor and waits for the motor to respond. This function returns an error object, the purpose of this object is to allow the user to check for errors, and handle them. To simplify this example, we simply print the value, which we access with the '.value' at the end of the function call.

Note: The spaces and '\r' following the position value allow the function to clean up and re-print the data on the same line, this is meant simply to clean up what the output looks like when running.

# Run Your Program!

With this you have completed writing the most basic orcaSDK program! Try running the program and see what your motor's position is. Try pushing your motor's shaft back and forth, and see how it changes the output.

# Adding Tutorial Helpers Generalization

Each tutorial also contains example source code for what the completed tutorial should look like. For each of them, they use a helper function for obtaining the serial port number from console input rather than having the number be hard-coded as this tutorial suggests. Each subsequent tutorial will assume we use the helper function, so we will quickly describe it here.

```./main.cpp
...
	int serial_port = obtain_serial_port_number();

	motor.open_serial_port(serial_port);
...
```

This is what the updated code looks like. The helper function obtain_serial_port_number() simply prompts the user for input and returns whatever number they pass into the console. After capturing this number, the resulting variable can be used as the hard-coded value was earlier.

In order to use the helper function we will need to include it, so we also add an #include statement to the top of the file

```./main.cpp
#include <iostream>
#include "actuator.h"
#include "TutorialHelpers.h"
...
```

# What's Next?

Now that you've completed the basic orcaSDK tutorial, feel free to browse the remaining tutorials and read them in any order that feels appropriate. If the tutorial you wish to read next contains a prerequisite that you have not read yet, please complete that prerequisite before continuing.
