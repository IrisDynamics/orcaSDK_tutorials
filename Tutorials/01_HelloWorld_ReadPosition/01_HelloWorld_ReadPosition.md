# Hello World / Read Position

In this tutorial we will set up the most basic app that demonstrates communication with your Orca motor. The end goal of this tutorial is an application which reads and displays the sensed position of a connected Orca motor.

To begin let's start with the source file that we used but didn't explain back in the orcaSDK's README.md

```./main.cpp
#include <iostream>
#include "actuator.h"

int main()
{
    Actuator motor{ 0, "MotorName" };
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
    Actuator motor{ 0, "MotorName" };
```

This line constructs an Actuator object and assigns it the name "motor". Inside the curly braces are the two parameters that the motor requires. These parameters assign the motor's modbus address and the object's name. Neither of these parameters are of much concern for the purpose of this tutorial, so for the moment, use 0 for the first parameter and use anything you'd like for the second parameter.

At this point we now have a virtual representation of an Orca motor, but it isn't yet connected to a physical motor. To give it the information it needs to connect to the actual motor, add the following lines to the file.

```./main.cpp
#include <iostream>
#include "actuator.h"

int main()
{
    Actuator motor{ 0, "MotorName" };

	motor.set_new_serial_port(com_port);
	motor.open_serial_port();

    std::cout << "Hello World\n";
    return 0;
}
```