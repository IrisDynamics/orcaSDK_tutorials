add_executable(04_ErrorHandling
	main.cpp
)

target_link_libraries(04_ErrorHandling PRIVATE orcaSDK::core)
target_link_libraries(04_ErrorHandling PRIVATE tutorialHelpers)