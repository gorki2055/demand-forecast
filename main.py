import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the actual path to your CSV file
file_path = '2073-asadh.csv'

# Read CSV file into a DataFrame, skipping the first row (header)
df = pd.read_csv(file_path, skiprows=1)

# Check for missing data in any cell
missing_data = df.isnull()

# Find indices (rows and columns) with missing data
missing_indices = [(row, col) for row in missing_data.index for col in missing_data.columns if missing_data.at[row, col]]

# Print the result
if missing_indices:
    print("Missing data exists in the following cell(s):")
    for row, col in missing_indices:
        print(f"Row: {row}, Column: {col}")
else:
    print("No missing data in the CSV file.")

# Transpose the DataFrame to have days as rows and time as columns
df_transposed = df.transpose()

# Plot the original data
plt.figure(figsize=(12, 6))
plt.plot(df_transposed.index, df_transposed.values, marker='o', linestyle='-', label='Original Data')

# Calculate and plot the moving average
window_size = 3  # Adjust the window size as needed
moving_average = df_transposed.rolling(window=window_size, min_periods=1).mean()
plt.plot(moving_average.index, moving_average.values, linestyle='--', label=f'Moving Average (Window Size={window_size})')

# Customize the plot
plt.title('Load Demand Over Time with Moving Average')
plt.xlabel('Day of Month')
plt.ylabel('Load Demand')
plt.grid(True)
plt.legend()

# Save the plot as an image (optional)
plt.savefig('load_demand_plot.png')

# Create a new DataFrame for the moving average with the same first row and column
moving_average_with_headers = pd.DataFrame(index=moving_average.index, columns=moving_average.columns)
moving_average_with_headers.iloc[:, 1:] = moving_average.iloc[:, 1:]

# Save the moving average to the specified CSV file with headers
output_file_path = r'D:\moving_average_output_with_headers.csv'
moving_average_with_headers.to_csv(output_file_path)
print(f"Moving average data (with headers) exported to '{output_file_path}'")

# Show the plot
plt.show()
