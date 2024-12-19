# Hello World / Read Position

In this tutorial we will set up the most basic app that demonstrates communication with your Orca motor. The end goal of this tutorial is an application which reads and displays the sensed position of a connected Orca motor.

To begin let's start with a basic main function which simply prints "Hello World" and then returns.

```./main.cpp
int main()
{
    return 0;
}
```

Now let's set up a basic project to build this  CMakeLists.txt file, which creates an executable target and links it to the SDK.

```./CMakeLists.txt
cmake_minimum_required(VERSION 3.23)

project(firstOrcaSDKProj)

add_executable(HelloWorld-ReadPosition
    main.cpp
)
```

Let's try building and running the file. To do so we'll create a build folder, and 

The next let's include the actuator.h header file and try to create an Actuator object.

```./main.cpp
#include "actuator.h"

int main()
{
    Actuator motor{ 0, "MotorName" };
    return 0;
}
```

The two parameters passed into the constructor represent the motor's modbus address and the object's name. Neither of these parameters are of much concern for the purpose of this tutorial, so for the moment, use 0 for the first parameter and use anything you'd like for the second parameter.

At this point the project