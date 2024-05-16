# Assembly Code Analysis Pipeline

This repository contains a collection of scripts that form a pipeline for analyzing assembly code.

## Overview

Analyzing assembly code can be a complex task, especially when dealing with large codebases. This pipeline aims to simplify the process by providing a series of scripts that handle different stages of analysis, from reading and parsing assembly code to extracting and analyzing branch conditions.

## Files

### 1. File_1.cpp

- **Description**: This C++ program calculates the sum of elements in an array recursively.
- **Usage**: Compile and run the program to see the sum of elements in a predefined array.

### 2. new.py

- **Description**: This Python script reads assembly code from a file (`input.s`) and writes it to a text file (`output.txt`).
- **Usage**: Run the script to transfer assembly code from `input.s` to `output.txt`.

### 3. branch.py

- **Description**: This Python script reads a parse tree file (`output.txt`), extracts branch conditions (e.g., 'call' instructions), and writes these branch conditions to another file (`branch_conditions.txt`).
- **Usage**: Execute the script to analyze branch conditions in the parse tree.

### 4. oparse.py

- **Description**: This Python script defines a lexer and parser to tokenize assembly code, parse tokens into a parse tree, and output this tree to a text file (`parse_tree.txt`).
- **Usage**: Run the script to tokenize assembly code, create a parse tree, and output it to `parse_tree.txt`.

## Usage

1. **Setup**: Ensure you have the necessary dependencies installed for running C++ (for File_1.cpp) and Python (for new.py, branch.py, and oparse.py) scripts.
2. **Calculate Sum**: Compile and run File_1.cpp to see the sum of elements in the array.
3. **Transfer Assembly Code**: Execute new.py to transfer assembly code from `input.s` to `output.txt`.
4. **Analyze Branch Conditions**: Run branch.py to analyze branch conditions in the parse tree and generate `branch_conditions.txt`.
5. **Generate Parse Tree**: Execute oparse.py to tokenize assembly code, create a parse tree, and output it to `parse_tree.txt`.

## Contributors

- [DEEPAK YADAV](https://github.com/Deepakyavav/CSA_2)

Feel free to contribute to this project by opening issues or pull requests. Contributions are welcomed and appreciated!

