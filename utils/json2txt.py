#Imports
import json
import sys

# Usage:
# python devtools.py -js utils/<filename>

# Main function
def main(params):
    print("This is JSON converter")

    # If function does not get proper imputs, guide user and exit.
    if len(params) < 3:
        print("Usage: python devtools.py -js <filename>")
        sys.exit(1)

    # Choose the file on CLI.
    filename = params[2]

    # Convert JSON to Python data object.
    with open(filename, "r") as f:
        data = json.load(f)

    # Iterate over each entry and print results based on file name
        for entry in data:
            if "jsonfile.json" in filename:
                # People JSON
                print(f"id: {entry['id']}, name: {entry['name']}, age: {entry['age']}")
            elif "jsonfile2.json" in filename:
                # Pizza JSON
                print(f"id: {entry['id']}, name: {entry['name']}, size: {entry['size']}, toppings: {entry['toppings']}")
            else: # Fallback for unexpected files
                print("Wrong filename")