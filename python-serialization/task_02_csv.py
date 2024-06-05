import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file to a JSON file.

    Parameters:
    csv_filename (str): The name of the input CSV file.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Open the CSV file and read the data using DictReader
        with open(csv_filename, mode='r', newline='') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        # Serialize the list of dictionaries to JSON format
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        print(f"Error: The file {csv_filename} was not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Example usage:
if __name__ == "__main__":
    csv_filename = 'example.csv'
    success = convert_csv_to_json(csv_filename)
    if success:
        print("CSV file was successfully converted to JSON.")
    else:
        print("CSV file conversion to JSON failed.")

