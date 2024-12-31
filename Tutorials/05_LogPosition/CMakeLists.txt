add_executable(05_LogPosition
	main.cpp
)

target_link_libraries(05_LogPosition PRIVATE orcaSDK::core)
target_link_libraries(05_LogPosition PRIVATE tutorialHelpers)