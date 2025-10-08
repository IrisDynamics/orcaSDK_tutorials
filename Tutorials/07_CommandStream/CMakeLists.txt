add_executable(07_CommandStream
	main.cpp
)

target_link_libraries(07_CommandStream PRIVATE orcaSDK::core)
target_link_libraries(07_CommandStream PRIVATE tutorialHelpers)