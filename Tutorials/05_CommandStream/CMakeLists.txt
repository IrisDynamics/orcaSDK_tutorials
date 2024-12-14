add_executable(05_CommandStream
	main.cpp
)

target_link_libraries(05_CommandStream PRIVATE orcaSDK::core)
target_link_libraries(05_CommandStream PRIVATE tutorialHelpers)