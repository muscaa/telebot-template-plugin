cmake_minimum_required(VERSION 3.23)
project(telebot-template-plugin)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/$<CONFIGURATION>")
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/$<CONFIGURATION>")
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# VCPKG packages
find_package(SDL3 CONFIG REQUIRED)
find_package(Boost REQUIRED COMPONENTS
    system
    dll
    json
)
find_package(libzippp CONFIG REQUIRED)

# Sources
file(GLOB_RECURSE MAIN_SOURCES "src/*.cpp")

add_library(${PROJECT_NAME} SHARED
    ${MAIN_SOURCES}
)
set_target_properties(${PROJECT_NAME} PROPERTIES
    PREFIX ""
)
target_include_directories(${PROJECT_NAME} PRIVATE
    include
)

# VCPKG links
target_link_libraries(${PROJECT_NAME} PRIVATE
    SDL3::SDL3
    Boost::system
    Boost::dll
    Boost::json
    libzippp::libzippp
)

# Platform specific
if (WIN32)
    target_link_libraries(${PROJECT_NAME} PRIVATE ws2_32)
endif()
