add_executable(02_ReadOrcaMode
	main.cpp
)

target_link_libraries(02_ReadOrcaMode PRIVATE orcaSDK::core)
target_link_libraries(02_ReadOrcaMode PRIVATE tutorialHelpers)