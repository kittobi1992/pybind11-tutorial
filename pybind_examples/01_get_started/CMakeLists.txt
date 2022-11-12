cmake_minimum_required(VERSION 3.13)
project("Pybind11 Get Started Example")

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/../pybind11 ${CMAKE_CURRENT_BINARY_DIR}/pybind11)
pybind11_add_module(vecint module.cpp vector_int.cpp)