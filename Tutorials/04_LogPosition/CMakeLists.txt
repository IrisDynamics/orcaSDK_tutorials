add_executable(04_LogPosition
	main.cpp
)

target_link_libraries(04_LogPosition PRIVATE orcaSDK::core)
target_link_libraries(04_LogPosition PRIVATE tutorialHelpers)