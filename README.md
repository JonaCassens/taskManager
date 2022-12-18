# Task Manager

Task Manager is a command line tool for managing tasks and users. It allows users to add, edit, and mark tasks as complete, as well as register new users and view all tasks.

## Getting Started
To use this program, clone or download the repository to your local machine and make sure you have Python installed.

## Functionality

**reg_user(admin_check)**: Allows an admin user to register a new user by inputting a new username and password. The new user will be added to the *'user.txt'* file.

**add_task()**: Allows a user to add a new task by inputting the task's title, description, and due date. The task will be added to the *'tasks.txt'* file.

**view_all()**: Displays all tasks read in the *'tasks.txt'* file.

**view_mine(user_check)**: Shows all tasks assigned to user, and provides the option to mark them as complete or use *edit_task(user_check, task_select)*.

**mark_as_complete(user_check, task_select)**: Allows a user to mark a specific task as complete by selecting the task from a list of the user's tasks. The task's status will be updated in the tasks.txt file.

**edit_task(user_check, task_select)**: Allows a user to edit a specific task by selecting the task from a list of the user's tasks. The user can choose to edit the task's title, description, due date, or assign the task to a different user. The task's details will be updated in the *'tasks.txt'* file.

## File Information
The program reads data from the *'user.txt'* and *'tasks.txt'* file, which should be in the same directory as the task_manager.py file. 

The *'tasks.txt'* file should be in the following format, with each attribute separated by a comma and a space:

User, Title, Description, Set Date, Due Date, Completion(Yes/No)

The *'user.txt'* file should be in the follwing format, which each attribute seperate by a comma and a space:

User, Password

## Requirements
Python 3
