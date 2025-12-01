# 12 - Multiple Motors

If you are working with multiple motors and Modbus RTU, each motor must be connected to an associated RS422 cable and spliter. An Actuator object must be initialized for each motor, and its corresponding port opened. 

## Prerequisites
 - [Tutorial 01 - Hello World Read Position](../01_HelloWorld_ReadPosisition/01_HelloWorld_ReadPosition.md)
 - [Tutorial 07 - Command Stream](../07_CommandStream/07_CommandStream_ReadPosition.md)
---

We will begin with creating our Actuator object, using a portion of the code from tutorial one. 

```
#include <iostream>
#include "actuator.h"

using namespace orcaSDK;

int main() {
	Actuator motor{ "ORCA1" };

	return 0;
}
```

To initialize multiple motors, we can either create each Actuator individually if it is helpful for each motor to have a distinct name, or we can use a data structure like an array. 

We will modify our above code to create multiple Actuators rather than a single Actuator object. This example demonstrates the array-based approach. 

```./main.cpp
    ...
    Actuator motors[2] {
        { "ORCA1" },
        { "ORCA2" }
    }
    ...
```

To declare the motors with distinct names, the following approach can be used: 

```./main.cpp
    ...
    Actuator motor_one { "ORCA1" };
    Actuator motor_two { "ORCA2" };
    ...
```

Next, the serial port for each motor should be opened. The serial port numbers are entered through user entry. This can be done through a loop to minimize our repeated code.  

```./main.cpp
    ...
    int serial_port;
    const int NUM_MOTORS = sizeof(motors) / sizeof(motors[0]);

    for (int i = 0; i < NUM_MOTORS; i++) {

        // for print formatting 
        if (i > 0) {
            std::cout << "\n\n";
        }
        std::cout << "Enter the serial port for " << motors[i].name << ": ";

        std::cin >> serial_port;
    }
    ...
```

We will add some error handling to determine if the ports have opened successfully, and enable command streaming while we are at it:

```./main.cpp
    ...
        std::cin >> serial_port;

        auto error = motors[i].open_serial_port(serial_port);

        motors[i].enable_stream();

        if (error) {
            std::cout << "Error: " << error.what() << "\n";
        } else {
            std::cout << motors[i].name << " connected succesfully.";
        }
    } // closing off our for loop
    ...
```

Now we will call motor.run() and print the position for each motor. Motor Zero is used as an example here.

```./main.cpp
    ...
    while (true) {
        motors[0].run();

        std::cout << "\nCurrent Position: " << motors[0].stream_cache.position << "   \r";
    }
    return 0;
```



