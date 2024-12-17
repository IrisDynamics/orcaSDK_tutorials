add_executable(07_HapticControl
	main.cpp
)

target_link_libraries(07_HapticControl PRIVATE orcaSDK::core)
target_link_libraries(07_HapticControl PRIVATE tutorialHelpers)