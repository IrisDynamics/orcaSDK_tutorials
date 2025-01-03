# Log Position

In this tutorial we will set up a basic app that outputs position data from a motor to a log file.

## Prerequisites
 - [Tutorial 04 - Error Handling](../04_ErrorHandling/04_ErrorHandling.md)
  
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

## Construct a Log Object

Our SDK contains an object to help facilitate logging easily. For this tutorial we will make use of this object. First lets construct an instance of it.

```./main.cpp
	...
	Log log{ Log::TimestampType::DurationSinceOpening };
	...
```

The Log object adds a timestamp to all messages logged through it. The constructor parameter indicates what form this timestamp should take. There are only two valid parameters for this constructor. 
- Log::TimestampType::DurationSinceOpening
  - Time in microseconds since opening the file
- Log::TimestampType::CurrentDateTime
  - The current date and time of day

## Open the File

Now let's open a file using the object.

```./main.cpp
	...
	Log log{ Log::TimestampType::DurationSinceOpening };
	OrcaError error = log.open(<path-to-your-file-here>);
	if (error)
	{
		std::cout << error.what(); 
		return -1;
	}
	...
```

Inside the call to log.open() is the path to the log file you'd like created. If you pass it a relative path (doesn't contain a prefixed '/' or '~'), then the file will be placed relative to the resulting built executable. If you're struggling with locating the executable, consider using an absolute path instead.

## Write to the Log

If we were able to open the log file successfully, then we're ready to begin writing to it.

```./main.cpp
	...
	while (true) {
		int32_t current_position = motor.get_position_um().value;
		std::string curr_position_str = "Current Position: " + std::to_string(current_position);

		log.write(curr_position_str);
		std::cout << curr_position_str << "            \r";
	}
	...
```

Take a look at the file given by the path you provided to the Log object. It should now be filled with timestamped data showing the motor's position while your program was running.

## Reducing Log Verbosity

If your goal is to output data for consumption by another program, such as Microsoft Excel, then the extra text that is being printed may get in the way of your goal. In this case, it may be more useful to simply use the standard library's std::ofstream. If you would still like to use our abstraction, however, the Log does have a function which removes most of the extra text (except for newlines). This can be done by adding the following line of code.

```./main.cpp
	...
	Log log{ Log::TimestampType::DurationSinceOpening };
	log.set_verbose_mode(false);
	...
```