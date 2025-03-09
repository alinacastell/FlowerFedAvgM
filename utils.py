# Variety of utility functions for the project

# Imports
import os
import json
import re


def extract_alpha(filename):
    """Extract the value of alpha= from the filename."""
    match = re.search(r"alpha=(-?\d+\.?\d*(?:e[-+]?\d+)?)", filename)
    if match:
        try:
            return float(match.group(1))  # Convert alpha value to float
        except ValueError:
            return float('-inf')  # Assign lowest priority if conversion fails
    return float('-inf')  # Assign lowest priority if alpha is not found


def extract_metrics_from_json(folder_path):
    """Read JSON files sorted by descending order of 'alpha=' value."""
    files = [f for f in os.listdir(folder_path) if f.endswith(".json")]

    # Sort files based on extracted alpha values (descending order)
    files.sort(key=extract_alpha, reverse=False)
    losses = []
    accuracies = []
    
    for file_name in files:
        if file_name.endswith(".json"):
            file_path = os.path.join(folder_path, file_name)
            print("reading", file_path)
            try:
                with open(file_path, "r") as file:
                    data = json.load(file)
                    
                    # Extract values if they exist
                    loss_data = data.get("history", {}).get("losses_centralized", [])
                    accuracy_data = data.get("history", {}).get("metrics_centralized", {}).get("accuracy", [])
                    # Extract second values and append to lists
                    if loss_data and isinstance(loss_data[0], list) and len(loss_data[0]) > 1:
                        losses.append(loss_data[0][1])

                    if accuracy_data and isinstance(accuracy_data[0], list) and len(accuracy_data[0]) > 1:
                        accuracies.append(accuracy_data[0][1])
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in file {file_name}: {e}")
            except Exception as e:
                print(f"Unexpected error reading {file_name}: {e}")
    
    return losses, accuracies

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