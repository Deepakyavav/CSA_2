# Makefile for Assembly Code Analysis Pipeline

# Compiler
CXX := g++
CC := gcc

# Compiler flags
CXXFLAGS := -std=c++11 -Wall
CCFLAGS := -S

# Source files
CPP_FILES := File_1.cpp

# Executables
EXECUTABLE := File_1
ASSEMBLY_FILE := input.s

# Python interpreter
PYTHON := python3

# Python scripts
PYTHON_SCRIPTS := new.py branch.py oparse.py

# Targets
.PHONY: all clean

all: $(EXECUTABLE) run_python_scripts

$(EXECUTABLE): $(CPP_FILES)
	$(CXX) $(CXXFLAGS) -o $@ $^

$(ASSEMBLY_FILE): $(CPP_FILES)
	$(CC) $(CCFLAGS) -o $@ $^

run_python_scripts: $(ASSEMBLY_FILE)
	$(PYTHON) new.py
	$(PYTHON) branch.py
	$(PYTHON) oparse.py

clean:
	rm -f $(EXECUTABLE) $(ASSEMBLY_FILE) output.txt branch_conditions.txt parse_tree.txt

