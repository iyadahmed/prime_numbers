cmake_minimum_required(VERSION 3.16)
project(prime_numbers)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED YES)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_EXPORT_COMPILE_COMMANDS YES)

add_executable(gen_primes gen_primes.cpp)
