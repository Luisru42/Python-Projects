import pandas as pd

# Provide the path to your Excel file
excel_file_path = "file-path"

try:
    # Read the Excel file into a DataFrame
    data = pd.read_excel(excel_file_path)

    # Display the first few rows of the DataFrame
    print("First few rows of the DataFrame:")
    print(data.head())
except FileNotFoundError:
    print("The specified file was not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred: {e}")

