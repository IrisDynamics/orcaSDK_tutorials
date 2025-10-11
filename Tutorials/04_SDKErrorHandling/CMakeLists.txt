add_executable(04_SDKErrorHandling
	main.cpp
)

target_link_libraries(04_SDKErrorHandling PRIVATE orcaSDK::core)
target_link_libraries(04_SDKErrorHandling PRIVATE tutorialHelpers)