# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/raitis/Documents/vascusynth/Source

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs

# Include any dependencies generated for this target.
include CMakeFiles/VascuSynth.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/VascuSynth.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/VascuSynth.dir/flags.make

CMakeFiles/VascuSynth.dir/VascuSynth.cpp.o: CMakeFiles/VascuSynth.dir/flags.make
CMakeFiles/VascuSynth.dir/VascuSynth.cpp.o: /home/raitis/Documents/vascusynth/Source/VascuSynth.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/VascuSynth.dir/VascuSynth.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/VascuSynth.dir/VascuSynth.cpp.o -c /home/raitis/Documents/vascusynth/Source/VascuSynth.cpp

CMakeFiles/VascuSynth.dir/VascuSynth.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/VascuSynth.dir/VascuSynth.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raitis/Documents/vascusynth/Source/VascuSynth.cpp > CMakeFiles/VascuSynth.dir/VascuSynth.cpp.i

CMakeFiles/VascuSynth.dir/VascuSynth.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/VascuSynth.dir/VascuSynth.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raitis/Documents/vascusynth/Source/VascuSynth.cpp -o CMakeFiles/VascuSynth.dir/VascuSynth.cpp.s

CMakeFiles/VascuSynth.dir/SupplyMap.cpp.o: CMakeFiles/VascuSynth.dir/flags.make
CMakeFiles/VascuSynth.dir/SupplyMap.cpp.o: /home/raitis/Documents/vascusynth/Source/SupplyMap.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/VascuSynth.dir/SupplyMap.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/VascuSynth.dir/SupplyMap.cpp.o -c /home/raitis/Documents/vascusynth/Source/SupplyMap.cpp

CMakeFiles/VascuSynth.dir/SupplyMap.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/VascuSynth.dir/SupplyMap.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raitis/Documents/vascusynth/Source/SupplyMap.cpp > CMakeFiles/VascuSynth.dir/SupplyMap.cpp.i

CMakeFiles/VascuSynth.dir/SupplyMap.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/VascuSynth.dir/SupplyMap.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raitis/Documents/vascusynth/Source/SupplyMap.cpp -o CMakeFiles/VascuSynth.dir/SupplyMap.cpp.s

CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.o: CMakeFiles/VascuSynth.dir/flags.make
CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.o: /home/raitis/Documents/vascusynth/Source/OxygenationMap.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building CXX object CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.o -c /home/raitis/Documents/vascusynth/Source/OxygenationMap.cpp

CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raitis/Documents/vascusynth/Source/OxygenationMap.cpp > CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.i

CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raitis/Documents/vascusynth/Source/OxygenationMap.cpp -o CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.s

CMakeFiles/VascuSynth.dir/NodeTable.cpp.o: CMakeFiles/VascuSynth.dir/flags.make
CMakeFiles/VascuSynth.dir/NodeTable.cpp.o: /home/raitis/Documents/vascusynth/Source/NodeTable.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building CXX object CMakeFiles/VascuSynth.dir/NodeTable.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/VascuSynth.dir/NodeTable.cpp.o -c /home/raitis/Documents/vascusynth/Source/NodeTable.cpp

CMakeFiles/VascuSynth.dir/NodeTable.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/VascuSynth.dir/NodeTable.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raitis/Documents/vascusynth/Source/NodeTable.cpp > CMakeFiles/VascuSynth.dir/NodeTable.cpp.i

CMakeFiles/VascuSynth.dir/NodeTable.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/VascuSynth.dir/NodeTable.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raitis/Documents/vascusynth/Source/NodeTable.cpp -o CMakeFiles/VascuSynth.dir/NodeTable.cpp.s

CMakeFiles/VascuSynth.dir/VascularTree.cpp.o: CMakeFiles/VascuSynth.dir/flags.make
CMakeFiles/VascuSynth.dir/VascularTree.cpp.o: /home/raitis/Documents/vascusynth/Source/VascularTree.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Building CXX object CMakeFiles/VascuSynth.dir/VascularTree.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/VascuSynth.dir/VascularTree.cpp.o -c /home/raitis/Documents/vascusynth/Source/VascularTree.cpp

CMakeFiles/VascuSynth.dir/VascularTree.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/VascuSynth.dir/VascularTree.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raitis/Documents/vascusynth/Source/VascularTree.cpp > CMakeFiles/VascuSynth.dir/VascularTree.cpp.i

CMakeFiles/VascuSynth.dir/VascularTree.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/VascuSynth.dir/VascularTree.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raitis/Documents/vascusynth/Source/VascularTree.cpp -o CMakeFiles/VascuSynth.dir/VascularTree.cpp.s

CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.o: CMakeFiles/VascuSynth.dir/flags.make
CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.o: /home/raitis/Documents/vascusynth/Source/TreeDrawer.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs/CMakeFiles --progress-num=$(CMAKE_PROGRESS_6) "Building CXX object CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.o -c /home/raitis/Documents/vascusynth/Source/TreeDrawer.cpp

CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/raitis/Documents/vascusynth/Source/TreeDrawer.cpp > CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.i

CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/raitis/Documents/vascusynth/Source/TreeDrawer.cpp -o CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.s

# Object files for target VascuSynth
VascuSynth_OBJECTS = \
"CMakeFiles/VascuSynth.dir/VascuSynth.cpp.o" \
"CMakeFiles/VascuSynth.dir/SupplyMap.cpp.o" \
"CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.o" \
"CMakeFiles/VascuSynth.dir/NodeTable.cpp.o" \
"CMakeFiles/VascuSynth.dir/VascularTree.cpp.o" \
"CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.o"

# External object files for target VascuSynth
VascuSynth_EXTERNAL_OBJECTS =

VascuSynth: CMakeFiles/VascuSynth.dir/VascuSynth.cpp.o
VascuSynth: CMakeFiles/VascuSynth.dir/SupplyMap.cpp.o
VascuSynth: CMakeFiles/VascuSynth.dir/OxygenationMap.cpp.o
VascuSynth: CMakeFiles/VascuSynth.dir/NodeTable.cpp.o
VascuSynth: CMakeFiles/VascuSynth.dir/VascularTree.cpp.o
VascuSynth: CMakeFiles/VascuSynth.dir/TreeDrawer.cpp.o
VascuSynth: CMakeFiles/VascuSynth.dir/build.make
VascuSynth: /usr/lib/libITKCommon-5.0.so.1
VascuSynth: /usr/lib/libitksys-5.0.so.1
VascuSynth: /usr/lib/libITKVNLInstantiation-5.0.so.1
VascuSynth: /usr/lib/libitkvnl_algo-5.0.so.1
VascuSynth: /usr/lib/libitkvnl-5.0.so.1
VascuSynth: /usr/lib/libitkv3p_netlib-5.0.so.1
VascuSynth: /usr/lib/libitknetlib-5.0.so.1
VascuSynth: /usr/lib/libitkvcl-5.0.so.1
VascuSynth: CMakeFiles/VascuSynth.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs/CMakeFiles --progress-num=$(CMAKE_PROGRESS_7) "Linking CXX executable VascuSynth"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/VascuSynth.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/VascuSynth.dir/build: VascuSynth

.PHONY : CMakeFiles/VascuSynth.dir/build

CMakeFiles/VascuSynth.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/VascuSynth.dir/cmake_clean.cmake
.PHONY : CMakeFiles/VascuSynth.dir/clean

CMakeFiles/VascuSynth.dir/depend:
	cd /home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/raitis/Documents/vascusynth/Source /home/raitis/Documents/vascusynth/Source /home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs /home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs /home/raitis/Documents/Computer_Science/Year_3/COMP3931-Individual-Project/vascusynth/vs/CMakeFiles/VascuSynth.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/VascuSynth.dir/depend
