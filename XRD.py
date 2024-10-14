import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

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
    # Step 6: Find peaks
    peaks, _ = find_peaks(data[column_y])

    # Step 7: Plot the data
    plt.figure(figsize=(10, 6))
    plt.plot(data[column_x], data[column_y], color='b', label='Data')

    # Step 8: Plot and label peaks
    plt.plot(data[column_x].iloc[peaks], data[column_y].iloc[peaks], "o", color='k', label='Peaks')

    # Step 9: Annotate peaks with both x and y values
    for peak in peaks:
        plt.text(data[column_x].iloc[peak], data[column_y].iloc[peak],
                 f'({data[column_x].iloc[peak]:.2f}, {data[column_y].iloc[peak]:.2f})',
                 horizontalalignment='right', fontsize=8, color='red')

    plt.title(f'{column_y} vs {column_x} with Peaks')
    plt.xlabel(column_x)
    plt.ylabel(column_y)
    plt.grid()
    plt.legend()
    plt.show()
else:
    print(f"Error: One or both of the specified columns '{column_x}' and '{column_y}' do not exist.")
