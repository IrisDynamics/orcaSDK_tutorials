# orcaSDK_tutorials

## Introduction

This repo contains a set of small code examples and tutorials for illustrating how to interact with your Orca series motor through our [C++ SDK](https://github.com/IrisDynamics/orcaSDK/). This repo contains tutorials for common use cases for using our motors from C++. 

## Building the SDK

If you have not downloaded and built the SDK yet, navigate to [our Github repo for the SDK](https://github.com/IrisDynamics/orcaSDK) and follow the setup instructions in the README.

## How to Use the Tutorials

In order to build and use the code examples, use the same steps found in the orcaSDK's README in the section [Building Your Application](https://github.com/IrisDynamics/orcaSDK/#compile-and-run-your-application). In this case, each of the tutorials are an executable target contained in a larger project. Thus to use any of them, build your project with the [./Tutorials/CMakeLists.txt](./Tutorials/CMakeLists.txt) file as the root file. Don't forget, if you chose to build but not install the SDK, you will need to update the find_package(orcaSDK) command in the CMakeLists.txt file with a PATHS argument that points to the SDK's build directory.

These tutorials may rely on each other for prior knowledge. If a tutorial is dependent on having completed another tutorial first, it will provide a link to it under a "Prerequisites" header. Because of this, you can navigate the tutorials in any order you wish. A single exception to this is every tutorial will have expected you to complete [Tutorial 01: HelloWorld and ReadPosition](./Tutorials/01_HelloWorld_ReadPosition/01_ReadPosition.md). Because of this, Tutorial 01 will never be included in the Prerequisites section of another tutorial, because it is an implicit prerequisite.

## If using pyorcasdk

If you're using the python bindings version of this library, pyorcasdk, then this tutorial suite is still applicable to you. The structure of a program which interacts with either orcaSDK or pyorcasdk is equivalent. Because of this, we recommend still reading the writeups for each tutorial. As you read a tutorial, in that tutorial's folder there is a python source file, main.py, which contains the Python equivalents of the final result. Please refer to that file if the C++ code blocks are too confusing.

---

If you've followed the instructions up until now, you're ready to begin coding! Walk through [the first tutorial](./Tutorials/01_HelloWorld_ReadPosition/01_HelloWorld_ReadPosition.md) to learn about the most basic application that uses our SDK.