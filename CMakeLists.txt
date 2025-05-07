cmake_minimum_required(VERSION 3.23)
project(telebot-template-plugin)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/$<CONFIGURATION>")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/$<CONFIGURATION>")
set(CMAKE_CXX_STANDARD 17)

# VCPKG packages
find_package(SDL3 CONFIG REQUIRED)
find_package(Boost REQUIRED COMPONENTS
    system
)

# Sources
file(GLOB_RECURSE MAIN_SOURCES "src/*.cpp")

add_library(${PROJECT_NAME} SHARED
    ${MAIN_SOURCES}
)
target_include_directories(${PROJECT_NAME} PRIVATE
    include
)

# VCPKG links
target_link_libraries(${PROJECT_NAME} PRIVATE
    SDL3::SDL3
    Boost::system
)

# Platform specific
if (WIN32)
    target_link_libraries(${PROJECT_NAME} PRIVATE ws2_32)
endif()
