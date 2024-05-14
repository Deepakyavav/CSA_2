import re
import os

# Function to clean up assembly code
def cleanup_assembly(input_file, output_file):
    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' not found.")
        return

    with open(input_file, 'r') as infile:
        assembly_code = infile.read()

    # Remove comments
    assembly_code = re.sub(r';.*', '', assembly_code)

    # Remove labels
    assembly_code = re.sub(r'^\.[a-zA-Z_][a-zA-Z0-9_]*:', '', assembly_code, flags=re.MULTILINE)

    # Remove directives
    assembly_code = re.sub(r'\.[a-zA-Z_]+', '', assembly_code)

    # Remove empty lines and leading/trailing whitespace
    assembly_code = os.linesep.join([line.strip() for line in assembly_code.splitlines() if line.strip()])

    # Write cleaned-up assembly code to output file
    with open(output_file, 'w') as outfile:
        outfile.write(assembly_code)

    print(f"Cleaned up assembly code written to '{output_file}'.")

# Example usage
if __name__ == "__main__":
    # Specify the input and output files
    input_file = "input.s"  # Path to the input assembly code file
    output_file = "cleaned_output.s"  # Path to the cleaned-up output assembly code file

    # Clean up the assembly code
    cleanup_assembly(input_file, output_file)



# # 
# Cleaning up generated assembly code for input to a scheduler involves removing unnecessary parts like comments, labels, and directives. Here's a Python script that performs basic cleanup of assembly code:


# In this script:

# The cleanup_assembly function reads the input assembly code from a file.
# It uses regular expressions to remove comments, labels, and directives from the assembly code.
# It also removes empty lines and leading/trailing whitespace.
# The cleaned-up assembly code is then written to an output file.
# You can adjust the regular expressions or add additional cleanup steps as needed based on the specific requirements of your scheduler or the format of the input assembly code