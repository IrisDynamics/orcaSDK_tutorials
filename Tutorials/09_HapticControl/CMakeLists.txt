add_executable(09_HapticControl
	main.cpp
)

target_link_libraries(09_HapticControl PRIVATE orcaSDK::core)
target_link_libraries(09_HapticControl PRIVATE tutorialHelpers)