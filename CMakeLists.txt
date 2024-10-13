cmake_minimum_required(VERSION 3.12)
project(PyHockeyStats NONE)

# Use find_package to locate Python components
find_package(Python3 REQUIRED COMPONENTS Interpreter)

# Add a custom target for building the Python package
add_custom_target(build ALL
    COMMAND ${Python3_EXECUTABLE} setup.py build --build-base ${CMAKE_BINARY_DIR}
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
    COMMENT "Building PyHockeyStats using Python setup.py"
)

# Install process, supporting DESTDIR
install(CODE
    "
    set(_root_arg)
    if (NOT \"\$ENV{DESTDIR}\" STREQUAL \"\")
        set(_root_arg --root \$ENV{DESTDIR})
    endif()
    execute_process(
        COMMAND ${Python3_EXECUTABLE} setup.py install --prefix ${CMAKE_INSTALL_PREFIX} \${_root_arg}
        WORKING_DIRECTORY \"${CMAKE_SOURCE_DIR}\"
    )
    "
    COMMENT "Installing PyHockeyStats using Python setup.py"
)
