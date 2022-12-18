# Task Manager

Task Manager is a command line tool for managing tasks and users. It allows users to add, edit, and mark tasks as complete, as well as register new users and view all tasks.

## Functionality

**reg_user(admin_check)**: Allows an admin user to register a new user by inputting a new username and password. The new user will be added to the *'user.txt'* file.

**add_task()**: Allows a user to add a new task by inputting the task's title, description, and due date. The task will be added to the *'tasks.txt'* file.

**view_all()**: Displays all tasks read in the *'tasks.txt'* file.

**mark_as_complete(user_check, task_select)**: Allows a user to mark a specific task as complete by selecting the task from a list of the user's tasks. The task's status will be updated in the tasks.txt file.

**edit_task(user_check, task_select)**: Allows a user to edit a specific task by selecting the task from a list of the user's tasks. The user can choose to edit the task's title, description, due date, or assign the task to a different user. The task's details will be updated in the *'tasks.txt'* file.

## Requirements
Python 3
