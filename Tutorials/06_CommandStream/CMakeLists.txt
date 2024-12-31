add_executable(06_CommandStream
	main.cpp
)

target_link_libraries(06_CommandStream PRIVATE orcaSDK::core)
target_link_libraries(06_CommandStream PRIVATE tutorialHelpers)