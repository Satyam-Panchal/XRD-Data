import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

# Step 1: Read the CSV files
data_file_path = 'LSCO_4_Theta_2-Theta.csv'
data = pd.read_csv(data_file_path)

# Read the reference CSV file without headers
reference_file_path = 'reference_powderpattern_xy_collCode#82818.csv'
reference_data = pd.read_csv(reference_file_path, header=None)  # No header

# Step 2: Inspect the data (optional)
print("Original Data Columns:", data.columns)
print("Reference Data Shape:", reference_data.shape)  # Print shape to confirm data read

# Step 3: Specify columns to plot
column_x = '#twotheta'  # X-axis column from original data
column_y = ' ycal'       # Y-axis column from original data (replace with actual name)

# Reference columns (assuming first column is x and second column is y)
reference_x = reference_data[0]  # First column
reference_y = reference_data[1]  # Second column

# Step 4: Plot the original data
plt.figure(figsize=(12, 8))

# # Plot original data
# plt.plot(data[column_x], data[column_y], marker='o', linestyle='-', color='b', label='Original Data')
#
# # Plot reference data
# plt.plot(reference_x, reference_y, color='r', label='Reference Data')

# Step 5: Calculate absolute difference
# Align the data: ensure both datasets are on the same x values
reference_y_interp = np.interp(data[column_x], reference_x, reference_y)

# Calculate the absolute difference
absolute_difference = np.abs(data[column_y] - reference_y_interp)

# Step 6: Find peaks in the absolute difference
peaks, _ = find_peaks(absolute_difference)

# Step 7: Plot absolute difference
plt.plot(data[column_x], absolute_difference, color='g', label='Absolute Difference')

# Step 8: Annotate peaks on the absolute difference plot with x-values
for peak in peaks:
    plt.annotate(f'{data[column_x].iloc[peak]:.2f}',
                 xy=(data[column_x].iloc[peak], absolute_difference[peak]),
                 xytext=(5, 5),
                 textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', color='orange'),
                 fontsize=8, color='orange')

# Step 9: Set plot details
plt.title(f'{column_y} vs {column_x} with Reference Data and Absolute Difference')
plt.xlabel(column_x)
plt.ylabel('Value')
plt.xticks(rotation=45)  # Rotate x labels for better visibility
plt.grid()
plt.legend()
plt.show()
