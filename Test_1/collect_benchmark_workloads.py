import os
import shutil
import request
import tarfile

# Function to download and extract a tar.gz file
def download_and_extract(url, extract_path):
    # Download the file
    response = requests.get(url, stream=True)
    with open('temp.tar.gz', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    print("Download complete.")
    
    # Extract the file
    with tarfile.open('temp.tar.gz') as tar_ref:
        tar_ref.extractall(extract_path)
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
    download_and_extract(spec_url, spec_dir)

    # Collect workloads
    collect_workloads(spec_dir, spec_output_dir)