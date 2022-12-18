## Project Name

Task Manager

## Description

This is a task management tool that enables you to:

1: Set up users

2: Create and assign tasks to the users of the system

3: Keep track of the status of the tasks using some great reports!


## Table of Contents

Project Name

Description

Table of Contents

Installation guide

Usage

Credits

## Installation guide

To install task manager follow these steps:

1. Clone the repo

   ```sh
   git clone https://github.com/your_username_/Project-Name.git
   ```
   
2. Run the task_manager.py file in your ide


## Usage

### Logging in

1. Enter your username and password, if the details are correct you'll be able to log in, if not you'll get an error.

### Register user (this can only be done by an admin)
1. from the main menu enter 'r' - register user, see screenshot below:

![image](https://user-images.githubusercontent.com/120670963/208303377-01a50660-6ea9-41ea-9d41-800d3cbf9cde.png)

2. Enter your new username and password and then confirm the password. 

**NB:** If the username already exist you'll get an error and if the passwords do not match you will also get an error

Once complete you'll get a success message, see screenshot below:

![image](https://user-images.githubusercontent.com/120670963/208303504-8698dd70-d9e7-4751-b0ce-ef3163e57d85.png)

### Adding tasks
1. from the main menu enter 'a' - add task, see screenshot below:

![image](https://user-images.githubusercontent.com/120670963/208303784-08b57ffe-23c2-4344-9931-d89da9f3fb27.png)

2. Enter the username of the person you want to assign the task to.

**NB:** If the user does not exist you will get an error message

Enter the title of the task

Enter a description of the task

Enter the due date of the task use (dd mmm yyyy) format, the date must be today or in the future.

Once complete you'll get a success message, see screenshot below:

![image](https://user-images.githubusercontent.com/120670963/208303925-60941da2-3002-4f9b-8291-c3fbd73cf311.png)

### Viewing tasks
#### View all tasks
1. from the main menu enter 'va' - view all tasks, this will display all the tasks in the system, see screenshot below:

![image](https://user-images.githubusercontent.com/120670963/208304202-b550ae1c-5610-403d-98f7-4abcbe478796.png)

#### View my tasks
1. from the main menu enter 'vm' - view my tasks, this will only display the tasks assigned to the logged in user

3. You can then edit your tasks, edit the id of the task you want to edit

**NB:**You can only edit tasks that are still open, you will get an error if you try to edit a completed task

3. you'll get the following menu options:

![image](https://user-images.githubusercontent.com/120670963/208304806-55ba23cb-2307-46aa-841f-65160f8f6113.png)

Pick the option you want, if you pick edit task you'll be bale to either change the task assignee or edit the due date.


### Generating reports
1. from the main menu enter 'gr' - generate reports.

3. This will generate 2 reports as follows:

- task_overview.txt
- user_overview.txt

## Credits
Ash Starr - Who worte the code

Hyperion Dev - Who provided the training and support to help me write the code

## Contact
Ash Starr

Project Link: https://github.com/ashstarr/finalCapstone
