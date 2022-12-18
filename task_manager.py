# =====References===================
# I wasn't sure how to default a date to today, I ready this article
# https://www.w3schools.com/python/python_datetime.asp

# I used this article to get some best practice advice on building functions
# https://towardsdatascience.com/python-clean-code-6-best-practices-to-make-your-python-functions-more-readable-7ea4c6171d60

# I used this article to help me convert a date string into a datetime
# https://stackoverflow.com/questions/466345/convert-string-jun-1-2005-133pm-into-datetime
# I need to do this to make sure the new due date is set in the future

# I used this article to find out how to get yesterday's date
# https://www.geeksforgeeks.org/get-yesterdays-date-using-python/
# I need to do this to enable the new due date to be today's date

# I used this article to find out how to check if a file exists or not
# https://stackoverflow.com/questions/82831/how-do-i-check-whether-a-file-exists-without-exceptions
# I need to do this to check if task_overview.txt and user_overview.txt exist before importing the data from them
# In the display statistics section

# I read the chapter on functions in this book to learn how to set default values for function arguments
# https://www.amazon.co.uk/Python-Crash-Course-2nd-Edition/dp/1593279280
# I used this on the reporting functions where they needed to work for all users or a specific user

# =====Importing Libraries===========

# Import Datetime
import datetime

from datetime import datetime
from datetime import timedelta

# Import OS.Path
import os.path

# ====== Create Functions ======

# === Process Functions ===

# --- Username & password function ---
# Builds a username (key) and password (value) dictionary from data in the users.txt file.
# Returns the dictionary
def username_password ():

    username_password = {}

    with open ('user.txt','r') as file:
        for line in file:
            key, value = line.split(',')[0].strip(), line.split(',')[1].strip()
            username_password[key] = value

    return username_password


# --- Check user function ---
# Checks if the user exists in the username and password dictionary.
# Returns True if they do
def check_user (username):

    user_exists = False

    if username in username_password().keys():
        user_exists = True

    return user_exists


# --- Check password function ---
# Checks if the password entered by the user matches their password 
# in the username and password dictionary.
# Returns True if it does
def check_password (username,password):

    password_correct = False

    if password == username_password()[username]:
        password_correct = True

    return password_correct


# --- Register user function ---
# Writes the new username and password to the users.txt file.

def reg_user (username,password):

    with open ('user.txt', 'a+') as file:
        register_user = file.write ('\n'+username +', ' + password)
    
    return register_user


# --- Create task dictionary function ---
# Builds a task id (key) and task data list (value) dictionary from data in the tasks.txt file
# Returns the dictionary. 
def task_dict ():

    task_dictionary = {}

    with open ('Tasks.txt','r') as file:
        for line in file:
            key, value = line.split(',')[0], line.split(',')
            task_dictionary[key] = value
        
    return task_dictionary


# --- Task ID function ---
# Assigns a unique ID that is an increment of 1 more than the last ID in the system.
# It gets the next id by adding 1 to the length of the task dictionary.
def task_ref ():

    new_task_ref = 'T'+str(len(task_dict())+1)

    return new_task_ref


# --- Add task function ---
# Takes task title, description and due date and creates a new task in the task.txt file
def add_task (title,description,duedate):

    with open ('tasks.txt', 'a') as file:
        create_task = file.write ('\n'+ str(task_ref()) +', ' + task_username +', ' + title +', ' 
+ description +', ' + duedate +', ' 
+ datetime.now().strftime('%d %b %Y') +', ' + 'No')

    return create_task


# --- View all tasks function ---
# Shows all the tasks listed in tasks.txt
def view_all ():
    with open ('tasks.txt', 'r') as file:
        for line in file:
            taskdata = line.split(',')
            
            print (f'_______________________________________________________________________\n')
            print (f'Task:\t\t\t{taskdata[2].strip()}')
            print (f'Assigned to:\t\t{taskdata[1].strip()}')
            print (f'Date Assigned:\t\t{taskdata[5].strip()}')
            print (f'Due Date:\t\t{taskdata[4].strip()}')
            print (f'Task Complete?:\t\t{taskdata[6].strip()}')
            print (f'Task Description:\n {taskdata[3].strip()}\n')


# --- View my tasks function ---
# Shows only the tasks assigned to the logged in user in tasks.txt
def view_mine (username):
    with open ('tasks.txt', 'r') as file:
        for line in file:
            taskdata = line.split(',')
            if username == taskdata[1].strip():
                
                print (f'_______________________________________________________________________\n')
                print (f'Task ID:\t\t{taskdata[0].strip()}')
                print (f'Task:\t\t\t{taskdata[2].strip()}')
                print (f'Assigned to:\t\t{taskdata[1].strip()}')
                print (f'Date Assigned:\t\t{taskdata[5].strip()}')
                print (f'Due Date:\t\t{taskdata[4].strip()}')
                print (f'Task Complete?:\t\t{taskdata[6].strip()}')
                print (f'Task Description:\n {taskdata[3].strip()}\n')


# --- Check if task is complete function ---
# Reads the task data from the create task dictionary function
# Checks if the status of the provided task id is complete 
# It it is it returns True
def task_complete (task_dictionary,task_ref):

    task_complete = False

    if task_dictionary[task_ref][6].strip() == 'Yes':
        task_complete = True

    return task_complete

# --- Complete task function ---
# Gets a dictionary of tasks refs and tasks from the create task dictionary function
# Updates the status of the given task id to yes
# Outputs the data back into the tasks.txt file
def complete_task (task_dictionary,task_ref):

    task_dictionary [task_ref] = [
        task_dictionary [task_ref][0] + ',' + 
        task_dictionary [task_ref][1] + ',' +
        task_dictionary [task_ref][2] + ',' + 
        task_dictionary [task_ref][3] + ',' +
        task_dictionary [task_ref][4] + ',' + 
        task_dictionary [task_ref][5] + ',' +
        task_dictionary [task_ref][6].replace('No','Yes')
        ]

    with open ('Tasks.txt', 'w') as file:
        for task_ref, value in task_dictionary.items():
            file.writelines (','.join(value))

# --- Update task assignee function ---
# Gets a dictionary of tasks refs and tasks from the create task dictionary function
# Updates the assignee of the given task id to the new value provided
# Outputs the data back into the tasks.txt file
def update_task_assignee (task_dictionary,task_ref,current_assignee,new_assignee):

    task_dictionary[task_ref] = [
        task_dictionary[task_ref][0] + ',' + 
        task_dictionary[task_ref][1].replace(current_assignee,new_assignee) + ',' +
        task_dictionary[task_ref][2] + ',' + 
        task_dictionary[task_ref][3] + ',' +
        task_dictionary[task_ref][4] + ',' + 
        task_dictionary[task_ref][5] + ',' +
        task_dictionary[task_ref][6]
        ]

    with open ('Tasks.txt', 'w') as file:
        for task_ref, value in task_dictionary.items():
            file.writelines (','.join(value))


# --- Update task due date function ---
# Gets a dictionary of tasks refs and tasks from the create task dictionary function
# Updates the due date of the given task id to the new value provided
# Outputs the data back into the tasks.txt file
def update_task_duedate (task_dictionary,task_ref,new_duedate):

    task_dictionary[task_ref] = [
        task_dictionary[task_ref][0] + ',' + 
        task_dictionary[task_ref][1] + ',' +
        task_dictionary[task_ref][2] + ',' + 
        task_dictionary[task_ref][3] + ',' +
        task_dictionary[task_ref][4].replace(task_dictionary[task_ref][4].strip(),new_duedate) + ',' + 
        task_dictionary[task_ref][5] + ',' +
        task_dictionary[task_ref][6]
        ]

    with open ('Tasks.txt', 'w') as file:
        for task_ref, value in task_dictionary.items():
            file.writelines (','.join(value))


# --- Check due date is in the future function ---
# Checks that the date provided is either today or in the future.
# If it is it returns true
def check_duedate (duedate):

    duedate_infuture = False

    today = datetime.today()
    yesterday = today - timedelta(days = 1)
    duedate_asdate = datetime.strptime(duedate, '%d %b %Y')

    if duedate_asdate > yesterday:
        duedate_infuture = True

    return duedate_infuture 


# === Report Functions ===

# --- Count all tasks function ---
# Gets a dictionary of tasks refs and tasks from the create task dictionary function
# By default it counts all tasks
# If a username is provided it only counts tasks assigned to that user.
# Returns the count
def count_all_tasks (task_dictionary,user = 'all'):

    count = 0
    
    for task_ref, value in task_dictionary.items():
        
        if user == 'all':
            count += 1
        
        else:
            if task_dictionary.get(task_ref)[1].strip() == user:
                count += 1

    return count


# --- Count completed tasks function ---
# Gets a dictionary of tasks ids and tasks from the create task dictionary function
# By default it counts all tasks where the status is set to complete (Yes).
# If a username is provided it only counts tasks assigned to that user.
# Returns the count
def count_completed_task (task_dictionary,user = 'all'):

    count = 0

    for task_ref, value in task_dictionary.items():

        if (user == 'all' and 
        task_dictionary.get(task_ref)[6].strip() == 'Yes'):

            count += 1
        
        else:
            if (task_dictionary.get(task_ref)[1].strip() == user 
            and task_dictionary.get(task_ref)[6].strip() == 'Yes'):

                count += 1

    return count

# --- Count incomplete tasks function ---
# Gets a dictionary of tasks refs and tasks from the create task dictionary function
# By default it counts all tasks where the status is set to incomplete (No)
# If a username is provided it only counts tasks assigned to that user
# Returns the count
def count_incomplete_task (task_dictionary,user = 'all'):

    count = 0

    for task_ref, value in task_dictionary.items():

        if (user == 'all' and 
            task_dictionary.get(task_ref)[6].strip() == 'No'):

            count += 1

        else:
            if (task_dictionary.get(task_ref)[1].strip() == user and 
            task_dictionary.get(task_ref)[6].strip() == 'No'):

                count += 1

    return count


# --- Count overdue tasks function ---
# Gets a dictionary of tasks refs and tasks from the create task dictionary function
# By default it counts all tasks where the status is set to incomplete (No) 
# and the due date is in the past i.e the task is overdue.
# If a username is provided it only counts tasks assigned to that user
# Returns the count
def count_overdue_task (task_dictionary,user = 'all'):

    count = 0

    for task_ref, value in task_dictionary.items():

        if (user == 'all' and 
        task_dictionary.get(task_ref)[6].strip() == 'No' and 
        check_duedate (task_dictionary.get(task_ref)[4].strip()) == False):

            count += 1

        else:
            if (task_dictionary.get(task_ref)[1].strip() == user and 
            task_dictionary.get(task_ref)[6].strip() == 'No' and 
            check_duedate (task_dictionary.get(task_ref)[4].strip()) == False):

                count += 1

    return count


# --- Calculate the incomplete task percentage function ---
# Calculates the percentage of incomplete tasks by
# Getting the count of incomplete tasks from the count incomplete tasks function
# and dividing this by the count of all tasks which it gets from the count all tasks function.
# If a username is provided it only gets counts for tasks assigned to that user
# If there are no incomplete tasks it returns 0
# Otherwise it returns the percentage rounded to 2 decimal places
def incomplete_percentage (user = 'all'):

    if user == 'all':
        count_of_incomplete_tasks = count_incomplete_task(task_dict())

        if count_of_incomplete_tasks == 0:
            percentage = 0

        else:
            count_of_all_tasks = count_all_tasks(task_dict())
            percentage = round(((count_of_incomplete_tasks/count_of_all_tasks) *100),2)

    else:
        count_of_incomplete_tasks = count_incomplete_task(task_dict(),user)

        if count_incomplete_task(task_dict(),user) == 0:
            percentage = 0

        else:
            count_of_all_tasks = count_all_tasks(task_dict(),user)
            percentage = round(((count_of_incomplete_tasks/count_of_all_tasks) *100),2)

    return percentage


# --- Percentage of overdue tasks function ---
# Calculates the percentage of overdue tasks by
# getting the count of overdue tasks from the count overdue tasks function
# and dividing this by the count of all tasks which it gets from the count all tasks function.
# If a username is provided it only gets counts for tasks assigned to that user
# If there are no incomplete tasks it returns 0
# Otherwise it returns the percentage rounded to 2 decimal places
def overdue_percentage (user = 'all'):

    if user == 'all':
        count_of_overdue_tasks = count_overdue_task(task_dict())

        if count_of_overdue_tasks == 0:
            percentage = 0

        else:
            count_of_all_tasks = count_all_tasks(task_dict())
            percentage = round(((count_of_overdue_tasks/count_of_all_tasks) *100),2)

    else:
        count_of_overdue_tasks = count_overdue_task(task_dict(),user)

        if count_of_overdue_tasks == 0:
            percentage = 0

        else:
            count_of_all_tasks = count_all_tasks(task_dict(),user)
            percentage = round(((count_of_overdue_tasks/count_of_all_tasks) *100),2)

    return percentage



# --- Percentage of all tasks assigned to a user function ---
# Calculates the percentage of tasks assigned to the provided username by
# getting the count of tasks assigned to the user from the count all tasks function
# and dividing this by the count of all tasks which it gets from the count all tasks function.
# If there are no incomplete tasks it returns 0
# Otherwise it returns the percentage rounded to 2 decimal places
def usertask_percentage (user):

    count_of_users_tasks = count_all_tasks(task_dict(),user)

    if count_of_users_tasks == 0:
        percentage = 0

    else:
        count_of_all_tasks = count_all_tasks(task_dict())
        percentage = round(((count_of_users_tasks/count_of_all_tasks)*100),2)

    return percentage


# --- Percentage of complete tasks function ---
# Calculates the percentage of tasks where the status is set to complete (Yes) by
# getting the count of completed tasks from the count completed tasks function
# and dividing this by the count of all tasks which it gets from the count all tasks function.
# If a username is provided it only gets counts for tasks assigned to that user
# If there are no incomplete tasks it returns 0
# Otherwise it returns the percentage rounded to 2 decimal places
def complete_percentage (user = 'all'):

    count_of_complete_tasks = count_completed_task(task_dict())

    if user == 'all':
        if count_of_complete_tasks == 0:
            percentage = 0

        else:
            count_of_all_tasks = count_all_tasks(task_dict())
            percentage = round(((count_of_complete_tasks/count_of_all_tasks) *100),2)

    else:
        count_of_complete_tasks = count_completed_task(task_dict(),user)

        if count_of_complete_tasks == 0:
            percentage = 0

        else:
            count_of_all_tasks = count_all_tasks(task_dict(),user)
            percentage = round(((count_of_complete_tasks/count_of_all_tasks) *100),2)

    return percentage


# --- Create task overview report function ---
# Creates the task overview report by running the relevant functions that
# calculate the information provided in the report.
# It then outputs this to the task_overview.txt file
def task_overview ():

    with open ('task_overview.txt','w') as file:

        file.write (f'Task overview report\n')
        file.write ('_____________________________________________________\n\n')
        file.write (f'Total number of tasks:\t\t\t\t{count_all_tasks(task_dict())}\n')
        file.write (f'Total number of completed tasks:\t\t{count_completed_task(task_dict())}\n')
        file.write (f'Total number of incomplete tasks:\t\t{count_incomplete_task(task_dict())}\n')
        file.write (f'Total number of overdue tasks:\t\t\t{count_overdue_task(task_dict())}\n')
        file.write (f'Percentage of tasks that are incomplete:\t{incomplete_percentage ()}\n')
        file.write (f'Percentage of tasks that are overdue:\t\t{overdue_percentage()}\n')
        file.write ('_____________________________________________________\n\n')


# --- Create user overview report function ---
# Creates the user overview report by running the relevant functions that
# calculate the information provided in the report.
# It loops through the users passwords dictionary to create a report for each user
# and provide the relevant functions with the username required to filter the 
# function output to just that username.
# It then outputs this to the user_overview.txt file
def user_overview ():

    with open ('user_overview.txt','w') as file:

        file.write (f'User overview report\n')
        file.write ('_____________________________________________________\n\n')
        file.write ('System summary\n')
        file.write ('_____________________________________________________\n\n')
        file.write (f'Total number of users registered:\t\t{len(username_password())}\n')
        file.write (f'Total number of tasks:\t\t\t\t{count_all_tasks(task_dict())}\n')
        file.write ('_____________________________________________________\n\n\n')
        for user in username_password():
            file.write (f'Summary report for {user}\n')
            file.write ('_____________________________________________________\n\n')
            file.write (f'Total number of tasks:\t\t\t\t{count_all_tasks(task_dict(),user)}\n')
            file.write (f'Percentage of all tasks assigned to {user}:\t{usertask_percentage (user)}\n')
            file.write (f'Percentage of tasks that are complete:\t\t{complete_percentage (user)}\n')
            file.write (f'Percentage of tasks that are incomplete:\t{incomplete_percentage (user)}\n')
            file.write (f'Percentage of tasks that are overdue:\t\t{overdue_percentage (user)}\n\n')


# --- Display task overview report function ---
# Imports the report data held in the task_overview.txt file and displays this to the user
# If the task_overview.txt file doesn't exist it runs the create task overview report function
# so the file is generated before it imports it.
def display_task_overview ():

    if os.path.isfile ('task_overview.txt') == False:
        task_overview ()

    with open ('task_overview.txt','r') as file:
        for line in file:
            print (line.strip())


# --- Display user overview report function ---
# Imports the report data held in the user_overview.txt file and displays this to the user
# If the user_overview.txt file doesn't exist it runs the create user overview report function
# so the file is generated before it imports it.
def display_user_overview ():

    if os.path.isfile ('user_overview.txt') == False:
        user_overview ()

    with open ('user_overview.txt','r') as file:
        for line in file:
            print (line.strip())
    

# =====Variables=====================

correct_details = False


#====Login Section====

# ===user name sub section===
# Start a while loop to get the username
# Check if the username exists in the user.txt file
# If it doesn't exist display an error and ask again
# If the user name is correct move to the password sub section
while True:
    if correct_details == True:
        break

    else:
        
        username = input('Enter your username: ')
        if check_user (username) == True:
            print('Correct username entered\n')


                # ===password sub section===
                # Ask the user to enter their password
                # Check the user.txt file to see if the password matches the password for the user
                # If it doesn't tell them and ask them to enter their password again
                # If the password is correct move to the menu section
            while True:
                password = input(f'Enter the password for {username}: ')
                if check_password (username,password) == True:
                    print('Correct password entered\n')
                    correct_details = True
                    break

                else:
                    print('Incorrect Password\n')


            # If the username does not exist in the user.txt file 
            # Tell them and run the username sub section again

        else:
            print('Username not found\n')


#====Main Menu Section====

# Check to see if the logged in user is admin if they are
# Presenting the menu to the user with the additional options of:
# register user
# generate reports
# display statistics
correct_details = False

while True:
    if username == 'admin':

        # Convert the user input to lower case.
        menu = input('''Please select one of the following options:
        r - register user
        a - add task
        va - view all tasks
        vm - view my tasks
        gr - generate reports
        ds - display statistics
        e - exit           
        : ''').lower()


        # If the logged in user is not admin
        # Present the menu to the user without the additional options of:
        # register user
        # generate reports
        # display statistics
    else:

        # Convert the user input to lower case.
        menu = input('''Please select one of the following options:
        a - add task
        va - view all tasks
        vm - view my tasks
        e - exit
        : ''').lower()


#====Register User Section====

    if menu == 'r':
        pass

        # ===user name sub section===
        # Ask the user to enter a new username
        # Check if the username already exists in the user.txt file
        # If it does tell the user and ask them to enter a username again
        # If it doesn't move to the password sub section

        correct_details = False

        while True:
            if correct_details == True:
                break

            else:
                newusername = input('Enter the username for the new user: ')

                if check_user(newusername) == True:
                    print('Username already exists\n')
                
                else:
                    print('Username does not exist\n')
                    # ===password sub section===
                    # Ask the user to enter a password for the user
                    # Get them to confirm the password
                    # If they are the same write the username and password to the users.txt file
                    # Go back to the main menu section
                    # If they are different ask them to enter a password for the user again
            
                    while True:
                        if correct_details == True:
                            break

                        else:
                            newpassword = input(f'Enter a password for {newusername}: ')

                            if newpassword == (input('Please confirm your password: ')):
                                reg_user (newusername,newpassword)
                                correct_details = True
                                print('New user created!\n')

                            else:
                                print('Password doesn\'t match\n')


#====Adding a task section====

    elif menu == 'a':
        pass
            
        # Ask the user to enter the username of the person the task is assigned to
        # Make sure the user exists in the users.txt file
        # If they don't exist, tell them and prompt for the username again
        # If they do exist ask for the rest of the details required to create a task
        # Default the Data Assigned to today's date and the Task Completed to No
        # Save the new task to the tasks.txt file 

        correct_details = False

        while True:
            if correct_details == True:
                break

            else:
                task_username = input('Enter the username of the person the task is assigned to: ')
                if check_user(task_username) == False:
                    print('Username does not exist\n')

                else:
                    correct_details = True
                    task_title = input('Enter the title of the task: ')
                    task_description = input('Enter a description of the task: ')
                    correct_details = False

                    while True:
                        task_due_date = input('Enter the due date of the task use (dd mmm yyyy) format,\
the date must be today or in the future: ')
                        if correct_details == True:
                            break

                        elif check_duedate (task_due_date):
                            add_task(task_title,task_description,task_due_date)
                            correct_details = True
                            print('Task created!\n')
                            break

                        else:
                            print(f'\n{task_due_date} is in the past. Please enter today\'s date or a date in the future\n')


#====View all tasks section====

    elif menu == 'va':
        pass
        
        # Call the view all tasks function
        # Which shows all the tasks listed in tasks.txt
        view_all ()

#====View my tasks section====

    elif menu == 'vm':
        pass
        
        # Call the view my tasks function which
        # shows only the tasks assigned to the logged in user
        view_mine (username)


        # Ask the user enter a task id and check it exists
        while True:
            task_id = input('''MY TASKS - MENU
\nEnter the ID of the task you want to edit or -1 to exit: ''').upper()

            if task_id == '-1':
                break

            elif task_id in task_dict():

                # Make sure the task status is not complete
                if task_complete(task_dict(),task_id):
                    print(f'\nTask {task_id} is marked as complete and cannot be edited\n')

                else:
                    print(f'\nTask {task_id} exists and is open\n')

                    # Ask the user what they want to do to the task
                    while True:
                        task_action_menu = input('''MY TASKS - MENU --> TASK ACTION MENU
\nPlease select one of the following options:
c - mark task as complete
e - edit task
-1 - exit
: ''').lower()

                        if task_action_menu == '-1':
                            break

                        # If they want to mark it as complete call the complete task function
                        # which will update the task status to complete
                        elif task_action_menu == 'c':
                            complete_task(task_dict(),task_id)
                            print(f'\nTask {task_id} marked as complete!\n')
                            break

                        # If they want to edit the task ask them which field they want to edit
                        elif task_action_menu == 'e':
                            while True:
                                task_edit_menu = input('''\nMY TASKS - MENU --> TASK ACTION MENU --> TASK EDIT MENU
\nPlease select one of the following options:
a - edit task assignee
d - edit task due date
-1 - exit
: ''').lower()

                                if task_edit_menu == '-1':
                                    break
                                # If they select task assignee ask them to enter the new assignee
                                # Check the user exists. If they do update the assignee field
                                elif task_edit_menu == 'a':
                                    while True:
                                        new_assignee = (input('\nEnter the username of the new Assignee: '))

                                        if check_user (new_assignee):
                                            update_task_assignee(task_dict(),task_id,username,new_assignee)
                                            print(f'\nTask {task_id} assignee updated to {new_assignee}!\n')
                                            break

                                        else:
                                            print(f'\n{new_assignee} does not exist on the system. Please enter a valid username')

                                # If they select task due date ask them to enter the new due date
                                # Check the due date is either today or in the future.
                                # If it is update the due date field    
                                elif task_edit_menu == 'd':
                                    while True:
                                        new_duedate = (input('\nEnter the new Due Date for the task, use (dd mmm yyyy) format, \
the date must be today or in the future: '))

                                        if check_duedate (new_duedate):
                                            update_task_duedate(task_dict(),task_id,new_duedate)
                                            print(f'\nTask {task_id} due date updated to {new_duedate}!\n')
                                            break

                                        else:
                                            print(f'\n{new_duedate} is in the past. Please enter today\'s date or a date in the future')

                                else:
                                    print(f'\n{task_edit_menu} is not a valid option\n')
                                    continue
                        else:
                            print(f'\n{task_action_menu} is not a valid option\n')
                            continue
            else:
                print(f'\nThe task ID {task_id} does not exist\n')
                continue

#====Generate reports section====
        
    elif menu == 'gr':
        pass
        
        # Generate the task overview and user overview reports and output them to
        # the task_overview.txt and user_overview.txt files
        task_overview ()
        user_overview ()
        print('\nThe reports have been generated!\n')


#====Display statistics section====
        
    elif menu == 'ds':
        pass
        
        # Import the report data from the task_overview.txt and user_overview.txt files
        # If they don't exist generate them.
        # Display the report data to the user
        display_task_overview ()
        display_user_overview ()


#====Exit section====

    # If the user enters e exit the programme

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    # If the user enters something that isn't one of the menu options display an error

    else:
        print('You have made a wrong choice, Please Try again\n')
