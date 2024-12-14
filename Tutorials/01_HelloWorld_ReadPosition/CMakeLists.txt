add_executable(01_ReadPosition main.cpp)

target_link_libraries(01_ReadPosition PRIVATE orcaSDK::core)
target_link_libraries(01_ReadPosition PRIVATE tutorialHelpers)
