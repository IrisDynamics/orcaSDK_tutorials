# Command Stream
In this tutorial we introduce an important concept when using Orca motors through the SDK, the Command Stream. Command streaming is the SDK's main form of asynchronous communication with the motor. It allows for sending commands to the motor while simultaneously reading commonly used data. It is also required in order to use some features of the motor. For more details see the Orca Series Modbus RTU User Guide pdf available through our [Downloads](https://irisdynamics.com/downloads) page.
  
## 

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

To begin a command stream with your motor, add a call to the Actuator::enable_stream() method of your Actuator object.


```./main.cpp
	...
	motor.enable_stream();
	...
```

When this method is called. The motor will begin sending asynchronous command stream messages to your connected motor. Whenever you are streaming to your motor, you must call the Actuator::run() method at a regular interval. We'll add it within the while loop.

```./main.cpp
	...
	while (true)
	{
		motor.run();

		std::cout << "Current Position: " << motor.get_position_um().value << "          \r";
	}
	...
```

The run() checks to see if there is any existing messages that haven't been resolved yet. If there is no active message it sends a new command stream message. If there is a previously queued message, it checks to see if a valid response has occurred, or if the message should be considered to have failed. If either of those conditions have occurred, it handles the end of the existing message. 

If the object determines that there is an active message, but there is no work to do, then the run() method instead does nothing, allowing the caller to continue without being blocked.

Finally we need to make use of the data that the command stream returns. Currently we're reading the motor's position using the Actuator::get_position_um() method. Let's update that to instead read from the command stream's cache. 

```./main.cpp
	...
	while (true)
	{
		motor.run();

		std::cout << "Current Position: " << motor.stream_cache.position << "          \r";
	}
	...
```

Now instead of injecting additional read messages in order to get the motor's position, we're using the position data automatically returned while streaming.