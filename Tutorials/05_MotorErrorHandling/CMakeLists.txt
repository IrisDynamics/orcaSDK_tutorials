add_executable(05_MotorErrorHandling
	main.cpp
)

target_link_libraries(05_MotorErrorHandling PRIVATE orcaSDK::core)
target_link_libraries(05_MotorErrorHandling PRIVATE tutorialHelpers)