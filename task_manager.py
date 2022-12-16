#====Function Section====
#Registering a new user
def reg_user(admin_check):
    if admin_check:
        user_list = []
        with open("user.txt", "r") as f:
            for line in f:
                user_list.append(line.split(', ')[0])
        test = False
        while not test:
            username = input("Enter a new username: ")
            if username not in user_list:
                test = True
            else:
                print('Username already exists. Please try again.')
        password = input("Enter a new password: ")
        while test:
            confirm = input("Confirm password: ")
            if password == confirm:
                print("Success! User has been registered.")
                with open("user.txt","a") as f:
                    f.write(f"{username}, {password}\n")
                test = False
            else:
                print("Passwords do not match. Try again.")
    else:
        print("ERROR: You do not have the admin role")

#Adding a task
def add_task():
    username = input("Who is the task assigned to? ")
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("What is the due date (e.g. 10/10/2019): ")
    with open("tasks.txt", "a") as f:
        f.write(f"{username}, {title}, {description}, {current_date}, {due_date}, No\n")

#Displaying all tasks by iterating through the tasks.txt file
def view_all():
    with open("tasks.txt", "r") as f:
        for line in f:
            task_list = line.split(", ")
            print(f'''
            ________________________________________________________________________
            Task:                   {task_list[1]}
            Assigned to:            {task_list[0]}
            Date assigned:          {task_list[3]}
            Due date:               {task_list[4]}
            Task Complete?          {task_list[5]}
            Task description:       
                {task_list[2]}
            ________________________________________________________________________
            ''')

#Making a new string that contains the changes to a file then overwriting the original file
def mark_as_complete(user_check, task_select):
    task_count_check = 0
    new_text = ''
    with open('tasks.txt', 'r') as f:
        for line in f:
            task_list = line.split(", ")
            if task_list[0] == user_check:
                task_count_check += 1
                if task_count_check == task_select:
                    task_list[5] = 'Yes'
                    new_text += ', '.join(task_list)
                else:
                    new_text += ', '.join(task_list)
            else:
                new_text += ', '.join(task_list)
    print(new_text)
    with open('tasks.txt','w') as f:
        f.write(new_text)

#Check whether the task matches the selected task, then provide the options on that task and change the file accordingly
def edit_task(user_check, task_select):
    task_count_check = 0
    new_text = ''
    with open('tasks.txt', 'r') as f:
        for line in f:
            task_list = line.split(", ")
            if task_list[0] == user_check:
                task_count_check += 1
                if task_count_check == task_select:
                    if task_list[5] == 'No\n':
                        user_or_due = input('''
                        Choose an option:
                        u = Change the user doing the task
                        d = Change the due date
                        : ''').lower()
                        if user_or_due == 'u':
                            task_list[0] = input('\nInput the new user: ')
                            new_text += ', '.join(task_list)
                        else:
                            task_list[4] = input('\nInput the new due date e.g. 10/10/2019: ')
                            new_text += ', '.join(task_list)
                        print('Successful change.\n')
                    else:
                        print('Error: Task has already been completed and cannot be edited.')
                        new_text += ', '.join(task_list)
                else:
                    new_text += ', '.join(task_list)
            else:
                new_text += ', '.join(task_list)
    with open('tasks.txt', 'w') as f:
        f.write(new_text)
            
#Iterate through all tasks in tasks.txt then refer to a new function to provide editing options
def view_mine(user_check):
    with open("tasks.txt", "r") as f:
        return_check = False
        task_count = 0
        for line in f:
            task_list = line.split(", ")
            if task_list[0] == user_check:
                task_count += 1
                print(f'''
                ________________________________________________________________________
                Task ID:                {task_count}    
                Task:                   {task_list[1]}
                Assigned to:            {task_list[0]}
                Date assigned:          {task_list[3]}
                Due date:               {task_list[4]}
                Task Complete?          {task_list[5]}
                Task description:       
                    {task_list[2]}
                ________________________________________________________________________
                ''')
                return_check = True
        if return_check == False:
            print("User has no tasks.")
        elif return_check == True:
            user_ID_input = int(input('Select a Task ID or enter \'-1\' to return to main menu: '))
            while user_ID_input < -1 or user_ID_input > task_count:
                user_ID_input = int(input('\nError: Task ID does not exist.\n\nPlease select a Task ID or enter \'-1\' to return to main menu: '))
            if user_ID_input != -1:               
                mark_or_edit = input('''\nSelect one of the options below:
                m = Mark task as complete
                e = Edit the task
                : ''').lower()
                if mark_or_edit == 'm':
                    mark_as_complete(user_check,user_ID_input)
                    print('\nTask marked as complete.\n')
                elif mark_or_edit == 'e':
                    edit_task(user,user_ID_input)

#Display statistics after reading them from the generated report
def statistics(admin_check):
    user_content = ''
    task_content = ''
    if admin_check:
        generate_report(current_date)
        with open('user_overview.txt', 'r') as f:
            user_content = f.read()
        with open('task_overview.txt', 'r') as f:
            task_content = f.read() 
        print(user_content)
        print(task_content)
    else:
        print("You have made a wrong choice, Please try again")

#Assisting function, makes code in other functions easier to read - returns a boolean on whether something is overdue or not
def overdue(due_date, current_day):
    day_number_list = current_day.split('/')
    day_number_list = [int(item) for item in day_number_list]
    current_day_number = day_number_list[0] + day_number_list[1]*12 + day_number_list [2]*12*365
    day_number_list = due_date.split('/')
    day_number_list = [int(item) for item in day_number_list]
    day_number = day_number_list[0] + day_number_list[1]*12 + day_number_list [2]*12*365
    if current_day_number - day_number > 0:
        return True
    else:
        return False

#Returns a file that contains the statistics of all the tasks for specific users, by iterating and reading through all the lines in tasks.txt
def task_overview(current_date):
    total_tasks = 0
    completed_tasks = 0
    incomplete_tasks = 0
    incomplete_overdue = 0
    with open('tasks.txt', 'r') as f:
        for line in f:
            total_tasks += 1
            task_list = line.split(", ")
            if task_list[5] == 'Yes\n':
                completed_tasks += 1
            else:
                incomplete_tasks += 1
                if overdue(task_list[4], current_date):
                    incomplete_overdue += 1
    incomplete_percent = (incomplete_tasks / total_tasks) * 100
    overdue_percent = (incomplete_overdue / total_tasks) * 100
    with open('task_overview.txt', 'w') as f:    
        f.write(f'''
        Task Overview
        ________________________________________________________________________

        Total Tasks:                {total_tasks}    
        Completed Tasks:            {completed_tasks}
        Incomplete Tasks:           {incomplete_tasks}
        Overdue:                    {incomplete_overdue}
        Percentage Incomplete:      {incomplete_percent}
        Percentage Overdue:         {overdue_percent}
        ________________________________________________________________________
        ''')

#Returns a report on each individual user that shows their statistics - done by iterating through the tasks.txt file for each user in user.txt
def user_overview(current_date):
    user_count = 0
    task_count = 0
    with open('tasks.txt', 'r') as f:
        for line in f:
            task_count += 1
    with open('user.txt', 'r') as f:
        for line in f:
            user_count += 1
    with open('user_overview.txt', 'w') as f:
        f.write(f'''
        User Overview
        _______________________________________________________________________
        Total Users:                    {user_count}
        Total Tasks:                    {task_count}
        _______________________________________________________________________
        ''')
    with open('user.txt', 'r') as f:
        for user_line in f:
            specific_task_count = 0
            percent_complete = 0
            percent_incomplete = 0
            percent_overdue = 0
            user_list = user_line.split(", ")
            with open('tasks.txt', 'r') as f2:
                for task_line in f2:
                    task_list = task_line.split(", ")
                    if task_list[0] == user_list[0]:
                        specific_task_count += 1
                        if task_list[5] == 'Yes\n':
                            percent_complete += 1
                        else:
                            percent_incomplete += 1
                            if overdue(task_list[4],current_date):
                                percent_overdue += 1
            percent_task = (specific_task_count/task_count)*100
            if specific_task_count != 0:
                percent_complete = (percent_complete/specific_task_count)*100
                percent_incomplete = (percent_incomplete/specific_task_count)*100
                percent_overdue = (percent_overdue/specific_task_count)*100
            else:
                percent_complete = 'n/a'
                percent_incomplete = 'n/a'
                percent_overdue = 'n/a'
            with open('user_overview.txt', 'a') as f3:
                f3.write(f'''
            User:                           {user_list[0]}

            Total Tasks for User:           {specific_task_count}
            Percentage of Total Tasks:      {percent_task}
            Percentage Complete:            {percent_complete}
            Percentage Incomplete:          {percent_incomplete}
            Percentage Overdue:             {percent_overdue}
            _______________________________________________________________________
            ''')

#Generates both reports
def generate_report(current_date):
    task_overview(current_date)
    user_overview(current_date)

#====Login Section====
login = {}
with open("user.txt", "r") as f:
    for line in f:
        user, password = line[0:-1].split(', ')
        login[user] = password
user = input("Enter your username: ")
password = input("Enter your password: ")
while (user, password) not in login.items():
    print("Error: Invalid Username or Password.")
    user = input("Enter your username: ")
    password = input("Enter your password: ")

#Setting admin privileges
admin_privilege = False
if user == 'admin':
    admin_privilege = True

print("\nLogin successful.\n")

current_date = input('\nInput the current date (e.g. 19/10/2019): ')

#Core of program, menu loop
while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    
    if admin_privilege:
        menu = input('''
                ____________________________________________________________________________
                Select one of the following options below:
                r - Registering a user
                a - Adding a task
                va - View all tasks
                vm - View my task
                ds - Display statistics (admin only)
                gr - Generate reports
                e - Exit
                ____________________________________________________________________________

                : ''').lower()

    else:
        menu = input('''
                ____________________________________________________________________________
                Select one of the following options below:
                r - Registering a user
                a - Adding a task
                va - View all tasks
                vm - View my task
                gr - Generate reports
                e - Exit
                ____________________________________________________________________________

                : ''').lower()

    if menu == 'r':
        reg_user(admin_privilege)

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine(user)

    elif menu == 'ds':
        statistics(admin_privilege)

    elif menu == 'gr':
        generate_report(current_date)
        print('\nReport generated.\n')

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please try again")