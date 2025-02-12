import pickle
import json
import sys
import os
import pprint

def make_serializable(obj):
    """Recursively convert non-serializable objects to dictionaries or strings."""
    if isinstance(obj, dict):
        return {k: make_serializable(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [make_serializable(i) for i in obj]
    elif hasattr(obj, "__dict__"):  # Convert custom objects to dictionaries
        return obj.__dict__
    else:
        return str(obj)  # Convert unknown objects to strings

# Check if the correct number of arguments is provided
if len(sys.argv) != 2:
    print("Usage: python view_pickle.py <input_pickle_file>")
    sys.exit(1)

# Get the input pickle file from command-line arguments
input_file = sys.argv[1]

# Validate the file existence
if not os.path.isfile(input_file):
    print(f"Error: The file '{input_file}' does not exist.")
    sys.exit(1)

# Load the pickle file
with open(input_file, "rb") as f:
    data = pickle.load(f)

# Convert to a serializable format
serializable_data = make_serializable(data)

# Save the output JSON file with the same name
output_file = os.path.splitext(input_file)[0] + ".json"
with open(output_file, "w") as json_file:
    json.dump(serializable_data, json_file, indent=4)

print(f"Data saved to {output_file}. Open it in VS Code for better visualization.")
pprint.pprint(data)