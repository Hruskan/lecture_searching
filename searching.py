from pathlib import Path
import json
import time
import matplotlib.pyplot as plt
from generators import ordered_sequence


def read_data(file_name, field):
    """
    Reads a JSON file and returns data for a given field.

    Args:
        file_name (str): Name of the JSON file.
        field (str): Key to retrieve from the JSON data.
            Must be one of: 'unordered_numbers', 'ordered_numbers' or 'dna_sequence'.

    Returns:
        list | str | None:
            - list: If data retrieved by the selected field contains numeric data.
            - str: If field is 'dna_sequence'.
            - None: If the field is not supported.
    """
    # get current working directory path
    cwd_path = Path.cwd()
    
    file_path = cwd_path / file_name

    with open(file_path, "r") as file:
        data = json.load(file)
        if not field in data:
            return None
        elif field == "dna_sequence":
            return str(data[field])
        else:
            return data[field]

def linear_search(sequence, wanted_number):
    count = 0
    positions = []
    for number in range(len(sequence)):
        if sequence[number] == wanted_number:
            count += 1
            positions.append(number)
    results = {
        "positions": positions,
        "count": count
    }
    return results

def binary_search(sequence, wanted_number):
    ordered_sequence = sorted(sequence)
    left_margin = 0
    right_margin = len(ordered_sequence) - 1
    while left_margin <= right_margin:
        middle = int((left_margin + right_margin)/2)
        if ordered_sequence[middle] == wanted_number:
            return middle
        if ordered_sequence[middle] < wanted_number:
            left_margin = middle + 1
        else:
            right_margin = middle -1
    return None

def pattern_search(sequence, wanted_pattern):


def main():
    sequential_data = read_data("sequential.json", "unordered_numbers")
    start = time.perf_counter()
    index = binary_search(ordered_sequence(1000), 9)
    end = time.perf_counter()
    duration = (end - start)
    return index, duration


if __name__ == "__main__":
    print(main())
