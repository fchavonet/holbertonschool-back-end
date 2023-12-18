#!/usr/bin/python3
"""
Script that fetch and display TODO list progress
for a given employee ID using a REST API
and exports data to CSV.
"""

import csv
import requests
import sys


def fetch_todo_list(employee_id):
    """ Fetch and display TODO list progress for a given employee. """

    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Make requests to the API to fetch user and todo data
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        # Convert responses to JSON format
        user_data = user_response.json()
        todos_data = todos_response.json()

        # Extract user information
        employee_name = user_data.get("name")

        # Create a CSV file
        csv_file_name = "{}.csv".format(employee_id)
        with open(csv_file_name, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            csv_writer.writerow(["USER_ID",
                                 "USERNAME",
                                 "TASK_COMPLETED_STATUS",
                                 "TASK_TITLE"])

            # Write task data to CSV
            for task in todos_data:
                csv_writer.writerow([employee_id,
                                     employee_name,
                                     str(task.get("completed")),
                                     task.get("title")])

        # Print success message
        print(f"Data exported to {csv_file_name}")

    # Handle exceptions and print an error message
    except requests.exceptions.RequestException as e:
        print("Error fetching data: {}".format(e))
        sys.exit(1)


# Execute the script if it is the main entry point.
if __name__ == "__main__":

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    # Convert the command-line argument to an integer
    employee_id = int(sys.argv[1])
    # Call the fetch_todo_list function
    fetch_todo_list(employee_id)
