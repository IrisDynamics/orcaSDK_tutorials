add_executable(08_ForceControl
	main.cpp
)

target_link_libraries(08_ForceControl PRIVATE orcaSDK::core)
target_link_libraries(08_ForceControl PRIVATE tutorialHelpers)