import subprocess
import os

# Function to cross-compile C/C++ source code to assembly code for a specific architecture
def cross_compile_to_assembly(source_file, architecture, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Define compiler toolchain based on the architecture
    if architecture == 'x86':
        compiler = 'gcc'
    elif architecture == 'arm':
        compiler = 'arm-linux-gnueabi-gcc'
    elif architecture == 'mips':
        compiler = 'mips-linux-gnu-gcc'
    else:
        print("Unsupported architecture.")
        return

    # Define compiler flags for assembly output
    if source_file.endswith('.c'):
        output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(source_file))[0] + '.s')
        command = [compiler, '-S', '-O2', '-Wall', '-o', output_file, source_file]
    elif source_file.endswith('.cpp'):
        output_file = os.path.join(output_dir, os.path.splitext(os.path.basename(source_file))[0] + '.s')
        command = [compiler, '-S', '-O2', '-Wall', '-std=c++11', '-o', output_file, source_file]
    else:
        print("Unsupported source file format.")
        return

    # Execute the compilation command
    print(f"Cross-compiling {source_file} to assembly code for {architecture} architecture...")
    subprocess.run(command)
    print("Compilation complete.")

# Example usage
if __name__ == "__main__":
    # Specify the source file, target architecture, and output directory
    source_file = "example.c"  # Path to your C/C++ source file
    architecture = "x86"  # Target architecture: x86, arm, mips, etc.
    output_dir = "output_assembly"  # Directory to store the generated assembly code

    # Cross-compile the source code to assembly
    cross_compile_to_assembly(source_file, architecture, output_dir)



# Cross-compiling C/C++ source code to assembly code for different architectures involves using compiler toolchains specifically designed for those architectures. Here's a Python script that demonstrates how you can cross-compile C/C++ source code to assembly code for different architectures using GCC (GNU Compiler Collection)

# In this script:

# The cross_compile_to_assembly function takes the path to the C/C++ source file, the target architecture, and the output directory as input parameters.
# It determines the appropriate compiler toolchain based on the target architecture and constructs the compilation command accordingly.
# The function then executes the compilation command using subprocess.run to cross-compile the source code to assembly code.
# The example usage section at the bottom demonstrates how to use the function by specifying the source file, target architecture, and output directory.