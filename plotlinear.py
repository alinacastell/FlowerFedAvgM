# Plot the test accuracy of FedAvg and Custom-FedAvgM for CIFAR-10 dataset
# Local Epoch E = 1 | Reporting Fraction C = 0.05 | num_rounds=10.000

import matplotlib.pyplot as plt
import numpy as np

# Define x-axis values (Concentration) in log scale
x_values = np.array([10, 1, 0.1, 0.01, 10**-5, 10**-9])

# Define corresponding test accuracy for each method
fedavg_acc = np.array([0.70, 0.63, 0.62, 0.55, 0.52, 0.48])  # Approximate values
custom_fedavgm_acc = np.array([ 0.4238, 0.3448, 0.1, 0.1258,0.1 , 0.1])

# Create plot
plt.figure(figsize=(8, 4))

# Plot FedAvg
plt.plot(x_values, fedavg_acc, marker='^', linestyle='-', color='tab:blue', label="FedAvg")

# Plot Custom-FedAvgM
plt.plot(x_values, custom_fedavgm_acc, marker='o', linestyle='-', color='tab:pink', label="Custom-FedAvgM")

# Set log scale for x-axis
plt.xscale("log")

# Labels and title
plt.xlabel("Concentration")
plt.ylabel("Test Accuracy")
plt.title("CIFAR-10\nLocal Epoch E = 1 | Reporting Fraction C = 0.05 | num_rounds=10.000")

# Legend
plt.legend()

# Show the plot
plt.show()