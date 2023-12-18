#!/usr/bin/python3
"""
Script that fetch and display TODO list progress
for a given employee ID using a REST API.
"""

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

        # Calculate total tasks.
        total_tasks = len(todos_data)

        # Filter completed tasks using a for loop
        completed_tasks = []
        for task in todos_data:
            if task.get("completed"):
                completed_tasks.append(task)
        # Calculate the number of completed tasks
        num_completed_tasks = len(completed_tasks)

        # Print the progress of the employee's TODO list
        print("Employee {} is done with tasks ({}/{}):"
              .format(employee_name, num_completed_tasks, total_tasks))

        # Print the titles of completed tasks
        for task in completed_tasks:
            print("\t{}".format(task.get('title')))

    # Handle exceptions and print an error message
    except requests.exceptions.RequestException as e:
        print("Error fetching data: {}".format(e))
        sys.exit(1)


# Execute the script if it is the main entry point.
if __name__ == "__main__":

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    # Convert the command-line argument to an integer
    employee_id = int(sys.argv[1])
    # Call the fetch_todo_list function
    fetch_todo_list(employee_id)
