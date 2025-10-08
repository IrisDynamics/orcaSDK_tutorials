add_executable(06_LogPosition
	main.cpp
)

target_link_libraries(06_LogPosition PRIVATE orcaSDK::core)
target_link_libraries(06_LogPosition PRIVATE tutorialHelpers)