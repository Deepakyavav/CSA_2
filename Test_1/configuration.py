def read_config_file(filename):
    config = {}
    with open(filename, 'r') as file:
        for line in file:
            if not line.strip() or line.strip().startswith("#"):
                continue  # Skip empty lines and comments
            key, value = line.strip().split("=")
            config[key.strip()] = value.strip()
    return config

# Example usage
if __name__ == "__main__":
    config = read_config_file("processor_config.txt")
    fetch_width = int(config.get("FetchWidth", 1))  # Default fetch width is 1
    num_stages = int(config.get("NumStages", 5))   # Default number of stages is 5
    stage_names = config.get("StageNames", "").split()  # Default stage names are empty

    print("Fetch Width:", fetch_width)
    print("Number of Stages:", num_stages)
    print("Stage Names:", stage_names)
