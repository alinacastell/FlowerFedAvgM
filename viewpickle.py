import pickle
import json
import sys
import os
import pprint
from utils import make_serializable

# Correctly read the input pickle file
if len(sys.argv) != 2:
    print("Usage: python view_pickle.py <input_pickle_file>")
    sys.exit(1)
input_file = sys.argv[1]

if not os.path.isfile(input_file):
    print(f"Error: The file '{input_file}' does not exist.")
    sys.exit(1)

with open(input_file, "rb") as f:
    data = pickle.load(f)
serializable_data = make_serializable(data)

# Save the output JSON file with the same name
output_file = os.path.splitext(input_file)[0] + ".json"
with open(output_file, "w") as json_file:
    json.dump(serializable_data, json_file, indent=4)

print(f"Data saved to {output_file}. Open it in VS Code for better visualization.")
pprint.pprint(data)