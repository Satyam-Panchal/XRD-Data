import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

# Step 1: Read the CSV file
file_path = 'LSCO_4_Theta_2-Theta.csv'
data = pd.read_csv(file_path)

# Step 2: Inspect the DataFrame
print("Columns in the DataFrame:", data.columns)
print(data.head())  # Display the first few rows

# Step 3: Strip whitespace from column names
data.columns = data.columns.str.strip()

# Step 4: Specify the columns to plot
column_x = '#twotheta'  # Replace with your actual column name
column_y = 'ycal'  # Replace with your actual column name

# Step 5: Check if columns exist
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import numpy as np

# Step 1: Read the CSV file
file_path = 'LSCO_4_Theta_2-Theta.csv'
data = pd.read_csv(file_path)

# Step 2: Inspect the DataFrame
print("Columns in the DataFrame:", data.columns)
print(data.head())  # Display the first few rows

# Step 3: Strip whitespace from column names
data.columns = data.columns.str.strip()

# Step 4: Specify the columns to plot
column_x = '#twotheta'  # Replace with your actual column name
column_y = 'ycal'  # Replace with your actual column name

# Step 5: Check if columns exist
if column_x in data.columns and column_y in data.columns:
    # Step 6: Calculate the logarithm of the data
    log_data = np.log(data[column_y])

    # Step 7: Find peaks in the logarithmic data
    log_peaks, _ = find_peaks(log_data)

    # Step 8: Plot the logarithm of the data
    plt.figure(figsize=(12, 8))
    plt.plot(data[column_x], log_data, color='k', label='Log of Data')

    # Step 9: Plot and label peaks for logarithmic data
    plt.plot(data[column_x].iloc[log_peaks], log_data.iloc[log_peaks], "o", color='orange', label='Peaks (Log)')

    # Step 10: Annotate peaks for logarithmic data
    for peak in log_peaks:
        plt.text(data[column_x].iloc[peak], log_data.iloc[peak],
                 f'({data[column_x].iloc[peak]:.2f}, {log_data.iloc[peak]:.2f})',
                 horizontalalignment='right', fontsize=8, color='red')

    # Step 11: Set plot details
    plt.title(f'Log of {column_y} vs {column_x} with Peaks')
    plt.xlabel(column_x)
    plt.ylabel('Log Value')
    plt.grid()
    plt.legend()
    plt.show()
else:
    print(f"Error: One or both of the specified columns '{column_x}' and '{column_y}' do not exist.")