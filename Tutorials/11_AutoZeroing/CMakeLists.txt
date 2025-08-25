add_executable(11_AutoZeroing
	main.cpp
)

target_link_libraries(11_AutoZeroing PRIVATE orcaSDK::core)
target_link_libraries(11_AutoZeroing PRIVATE tutorialHelpers)