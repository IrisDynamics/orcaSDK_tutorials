add_executable(06_ForceControl
	main.cpp
)

target_link_libraries(06_ForceControl PRIVATE orcaSDK::core)
target_link_libraries(06_ForceControl PRIVATE tutorialHelpers)