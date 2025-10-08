add_executable(12_AutoZeroing
	main.cpp
)

target_link_libraries(12_AutoZeroing PRIVATE orcaSDK::core)
target_link_libraries(12_AutoZeroing PRIVATE tutorialHelpers)