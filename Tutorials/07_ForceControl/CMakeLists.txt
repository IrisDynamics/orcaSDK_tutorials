add_executable(07_ForceControl
	main.cpp
)

target_link_libraries(07_ForceControl PRIVATE orcaSDK::core)
target_link_libraries(07_ForceControl PRIVATE tutorialHelpers)