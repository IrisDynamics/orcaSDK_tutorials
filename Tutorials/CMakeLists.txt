cmake_minimum_required(VERSION 3.20)

project(orcaSDK_tutorials)

find_package(orcaSDK REQUIRED PATHS C:/Users/AidenBull/Documents/orcaSDK/out/build/x64-Debug)
add_subdirectory(helpers)

#Begin adding tutorials here
add_subdirectory(01_HelloWorld_ReadPosition)
add_subdirectory(02_ReadOrcaMode)
add_subdirectory(03_TriggerKinematicMotions)
add_subdirectory(04_ErrorHandling)
add_subdirectory(05_LogPosition)
add_subdirectory(06_CommandStream)
add_subdirectory(07_ForceControl)
add_subdirectory(08_HapticControl)