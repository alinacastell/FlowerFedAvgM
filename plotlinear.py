# Plot the test accuracy of FedAvg and Custom-FedAvgM for CIFAR-10 dataset
# Local Epoch E = 1 | Reporting Fraction C = 0.05 | num_rounds=5

import matplotlib.pyplot as plt
import numpy as np
from utils import extract_metrics_from_json

# Read and define result values from json files of both methods
folder_path = "flower/baselines/fedavgm/multirun-jsonresults/custom-fedavgm"
losses_fedavg, accuracies_fedavg = extract_metrics_from_json(folder_path)
print("Losses:", losses_fedavg)
print("Accuracies:", accuracies_fedavg)

folder_path = "flower/baselines/fedavgm/multirun-jsonresults/fedavg"
losses_customfedavg, accuracies_customfedavg = extract_metrics_from_json(folder_path)

# Define x-axis values (Concentration) in log scale
x_values = np.array([10**-9, 10**-5, 0.001, 0.01, 0.1, 1, 10])

# Create plot
plt.figure(figsize=(8, 4))

# Plot method accuracies
plt.plot(x_values, accuracies_fedavg, marker='^', linestyle='-', color='lightcoral', label="FedAvg")
plt.plot(x_values, accuracies_customfedavg, marker='o', linestyle='-', color='mediumaquamarine', label="Custom-FedAvgM")
plt.xscale("log")
plt.xticks(x_values, x_values)
plt.gca().invert_xaxis()
plt.xlabel("Concentration")
plt.ylabel("Test Accuracy")
plt.title("CIFAR-10 Accuracies\nLocal Epoch E = 1 | Reporting Fraction C = 0.05 | num_rounds=50")
plt.legend()

plt.show()

# Plot method losses
# Remove entries with NaN values
filtered_data = [
    (x, fed, custom)
    for x, fed, custom in zip(x_values, losses_fedavg, losses_customfedavg)
    if fed is not None and custom is not None and not (isinstance(fed, float) and np.isnan(fed))
]
x_values, losses_fedavg, losses_customfedavg = zip(*filtered_data)

# Plot
plt.plot(x_values, losses_fedavg, marker='^', linestyle='-', color='plum', label="FedAvg")
plt.plot(x_values, losses_customfedavg, marker='o', linestyle='-', color='deepskyblue', label="Custom-FedAvgM")
plt.xscale("log")
plt.xticks(x_values, x_values)
plt.gca().invert_xaxis()
plt.xlabel("Concentration")
plt.ylabel("Test Loss")
plt.title("CIFAR-10 Losses\nLocal Epoch E = 1 | Reporting Fraction C = 0.05 | num_rounds=50")
plt.legend()

plt.show()