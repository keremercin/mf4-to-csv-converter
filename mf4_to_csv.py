from asammdf import MDF

def convert_mf4_to_csv(mf4_file_path, csv_file_path):
    # Load the MF4 file
    mdf = MDF(mf4_file_path)

    # Get all channels and convert to a pandas DataFrame
    df = mdf.to_dataframe()

    # Save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    print(f"MF4 data has been successfully saved to {csv_file_path}")

if __name__ == "__main__":
    mf4_file_path = "path/to/your/mf4_file.MF4"  # Change this to the path of your MF4 file
    csv_file_path = "path/to/your/output_file.csv"  # Change this to the path where you want to save the CSV file
    convert_mf4_to_csv(mf4_file_path, csv_file_path)
