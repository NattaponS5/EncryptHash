import os
import random
from datetime import datetime, timedelta
import json

# Define the base folder to store logs
base_folder = "plant_house_logs_400"
meta_file = "last_run_meta.json"

# Set the initial timestamp (first run starts exactly at this time)
initial_timestamp = datetime(2024, 11, 1, 12, 0, 0)

# Ensure the base folder exists
os.makedirs(base_folder, exist_ok=True)

# Load or initialize the last run time
if os.path.exists(meta_file):
    with open(meta_file, "r") as f:
        meta_data = json.load(f)
        last_run_time = datetime.fromisoformat(meta_data["last_run_time"])
else:
    last_run_time = None

# Determine the current run time
if last_run_time is None:
    current_run_time = initial_timestamp  # First run starts exactly at 12:00 PM
else:
    current_run_time = last_run_time + timedelta(minutes=5)  # Subsequent runs increment by 5 minutes

# Update the meta file
with open(meta_file, "w") as f:
    json.dump({"last_run_time": current_run_time.isoformat()}, f)

# Create a folder for this run with the timestamp as its name
current_run_folder = os.path.join(base_folder, current_run_time.strftime("%Y-%m-%d_%H-%M-%S"))
os.makedirs(current_run_folder, exist_ok=True)

# Generate files
for plant_house in range(1, 11):  # Plant houses 1 to 10
    for sensor in range(1, 41):  # Sensors 1 to 40
        # Create the file name
        file_name = f"plant_house_{plant_house}_sensor_{sensor}_{current_run_time.strftime('%Y-%m-%d_%H-%M-%S')}.log"
        file_path = os.path.join(current_run_folder, file_name)

        # Generate file content
        data_value = random.uniform(0.0, 1.0)
        file_content = (
            f"Plant House: {plant_house},  Sensor: {sensor}\n"
            f"Data: {data_value}\n"
            f"TimeStamp: {current_run_time.strftime('%Y-%m-%d_%H-%M-%S')}\n"
            f"--------------------"
        )

        # Write to the file
        with open(file_path, "w") as f:
            f.write(file_content)

print(f"Log files have been successfully generated in: {current_run_folder}")