import os
import shutil
import subprocess
import zipfile
import urllib.request

# Function to download and extract a benchmark suite
def download_and_extract(url, destination):
    print(f"Downloading {url}")
    urllib.request.urlretrieve(url, destination)
    print("Extracting...")
    with zipfile.ZipFile(destination, 'r') as zip_ref:
        zip_ref.extractall('.')
    print("Extraction complete.")

# Function to collect benchmark workloads from a benchmark suite
def collect_workloads(suite_dir, output_dir):
    print(f"Collecting workloads from {suite_dir}")
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for root, dirs, files in os.walk(suite_dir):
        for file in files:
            if file.endswith('.exe') or file.endswith('.sh'):
                shutil.copy(os.path.join(root, file), output_dir)
    print("Workload collection complete.")

# Example usage
if __name__ == "__main__":
    # Define URLs and directories
    spec_url = "https://www.spec.org/cpu2006/Downloads/cpu2006v1.2.tar.gz"
    spec_dir = "./SPEC_CPU2006"
    spec_output_dir = "./SPEC_CPU2006_workloads"

    # Download and extract SPEC CPU2006
    download_and_extract(spec_url, "cpu2006.tar.gz")

    # Collect workloads from SPEC CPU2006
    collect_workloads(spec_dir, spec_output_dir)



# In this example:

# The download_and_extract function downloads a benchmark suite from a given URL and extracts it to the current directory.
# The collect_workloads function collects benchmark workloads (executable files) from a benchmark suite directory and copies them to a specified output directory.
# In the main section, you can specify the URL of the benchmark suite and the directories for downloading and extracting the suite (spec_url and spec_dir). Then, the script downloads and extracts the SPEC CPU2006 benchmark suite and collects its workloads into a directory named SPEC_CPU2006_workloads