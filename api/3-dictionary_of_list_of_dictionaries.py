#!/usr/bin/python3
"""
Script that export data in the JSON format
"""

import json
import requests
import sys


def export_todo_data():
    """ Fetch and display TODO list progress for all employees """

    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    try:
        # Make requests to the API to fetch user and todo data
        response_users = requests.get(users_url)
        response_todos = requests.get(todos_url)

        users = response_users.json()
        todos = response_todos.json()

        user_dict = {}

        # Populate user dictionary with tasks
        for user in users:
            user_id = str(user.get("id"))
            username = user.get("username")
            tasks = []

            for todo in todos:
                if todo.get("userId") == user.get("id"):
                    task_data = {
                        "username": username,
                        "task": todo.get("title"),
                        "completed": todo.get("completed")
                    }
                    tasks.append(task_data)

            user_dict[user_id] = tasks

        # Create a JSON file
        json_file_name = "todo_all_employees.json"
        with open(json_file_name, "w") as json_file:
            json.dump(user_dict, json_file)

    # Handle exceptions and print an error message
    except requests.exceptions.RequestException as e:
        print("Error fetching data: {}".format(e))
        sys.exit(1)


# Execute the script if it is the main entry point.
if __name__ == "__main__":
    # Call the export_todo_data function
    export_todo_data()
