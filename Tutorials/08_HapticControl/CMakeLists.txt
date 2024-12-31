add_executable(08_HapticControl
	main.cpp
)

target_link_libraries(08_HapticControl PRIVATE orcaSDK::core)
target_link_libraries(08_HapticControl PRIVATE tutorialHelpers)