#=====importing libraries===========
import datetime

# ==== Define Functions ====
# usernames and passwords in user.txt
def users():
    f_users = open('user.txt', 'r')
    user_data = f_users.readlines()
    f_users.close()

    dict_users = {}

    for line in user_data:
        if line == '\n':
            continue
        k, v = line.split(', ')
        dict_users[k] = v.replace('\n', '')

    return dict_users


# register users
def reg_user():
    f_users = open('user.txt', 'r')
    user_data = f_users.readlines()
    f_users.close()

    # get usernames and passwords
    dict_users = users()

    while True:
        new_username = input('Enter new username: ')

        if new_username not in dict_users:
            new_password = input('Enter new password: ')
            new_pass_verif = input('Confirm new password: ')

            # write new user details to user.txt
            if new_password == new_pass_verif:
                output = f'\n{new_username}, {new_password}'

                users_write = open('user.txt', 'a')
                users_write.write(output)
                users_write.close

                break

            # print error if passwords don't match
            else:
                print('Passwords don\'t match. Try again.')
                continue

        # ask user to input new username if username already exists
        else:
            print('That username already exists. Please try another.')
            continue


# add new task
def add_task():
    # user inputs new task details
    str_task_user = input('Assign task to: ')
    str_task_title = input('Task title: ')
    str_task_description = input('Task description: ')
    str_task_due = input('Due date (e.g. 01 Jan 2023): ')

    # get today's date
    today = datetime.datetime.today().strftime('%d %b %Y')

    # output
    output = '\n'
    output += f'{str_task_user}, '
    output += f'{str_task_title}, '
    output += f'{str_task_description}, '
    output += f'{today}, '
    output += f'{str_task_due}, '
    output += 'No'

    # write to tasks.txt
    f_tasks = open('tasks.txt', 'a')
    f_tasks.write(output)
    f_tasks.close()

    # print confirmation
    print('\nTask has been added.\n')


# view all tasks
def view_all():
    f_tasks = open('tasks.txt', 'r')
    task_data = f_tasks.readlines()
    f_tasks.close()

    # display all tasks in tasks.txt
    for pos, line in enumerate(task_data, 1):
        if line == '\n':
            pos -= 1
            continue
        split_line = line.strip('\n').split(', ')

        output = '\n'
        output += f'─────────────── {pos} ───────────────\n'
        output += f'Task: {split_line[1]}\n'
        output += f'Assigned to: {split_line[0]}\n'
        output += f'Due date: {split_line[4]}\n'
        output += f'Completed?: {split_line[5]}\n'
        output += f'Description:\n'
        output += f'\t{split_line[2]}\n'
        output += '──────────────────────────────────\n'

        print(output)


# view logged-in user's tasks
def view_mine():
    f_tasks = open('tasks.txt', 'r')
    data = f_tasks.readlines()
    f_tasks.close()

    # display tasks in tasks.txt if task is assigned to logged-in user
    for pos, line in enumerate(data, 1):
        if line == '\n':
            pos -= 1
            continue
        split_line = line.split(', ')

        split_line[5] = split_line[5].strip('\n')

        if str_username == split_line[0]:
            output = '\n'
            output += f'─────────────── {pos} ───────────────\n'
            output += f'Task: {split_line[1]}\n'
            output += f'Assigned to: {split_line[0]}\n'
            output += f'Due date: {split_line[4]}\n'
            output += f'Completed?: {split_line[5]}\n'
            output += f'Description:\n'
            output += f'\t{split_line[2]}\n'
            output += '──────────────────────────────────\n'

            print(output)

        # skip to next iteration if usernames don't match
        else:
            continue

    # user selects task to edit
    while True:
        option = int(input('Enter task number to edit; \n'
                           'or enter -1 to exit to main menu:\n'))

        # exit to main menu
        if option == -1:
            return

        # error handling
        if option > pos or option == 0 or option < -1:
            print('Invalid option. Please try again.')
            continue

        edit_data = data[option-1]

        break

    while True:

        # user selects which part of task to edit
        task_option = int(input('\nSelect from the following options:\n'
                                '1 - Mark task as complete\n'
                                '2 - Edit task\n'))

        # error handling
        if task_option > 2 or task_option < 1:
            print('Invalid option. Please try again.')
            continue

        data_sects = edit_data.split(', ')

        # to mark task as complete
        if task_option == 1:
            data_sects[-1] = 'Yes\n'
            new_data = ', '.join(data_sects)
            data[option-1] = new_data

            # write new data to tasks.txt
            f_tasks = open('tasks.txt', 'w')
            for line in data:
                f_tasks.write(line)

            f_tasks.close()

            print(f'────────────────────────────────────────────\n'
                  f'Congratulations! You have completed task {option}.\n'
                  f'────────────────────────────────────────────\n')

            break

        # edit task
        if task_option == 2:
            edit_option = int(input('Please select from the following options:\n'
                                    '1 - Change user assigned to task\n'
                                    '2 - Change due date\n'))

            # error handling
            if task_option > 2 or task_option < 1:
                print('Invalid option. Please try again.')
                continue

            # change user assigned to task
            if edit_option == 1:
                data_sects[0] = input('Re-assign to: ')
                new_data = ', '.join(data_sects)
                data[option-1] = new_data

                print(f'────────────────────────────────────────────\n'
                      f'Task {option} is now assigned to {data_sects[0]}.\n'
                      f'────────────────────────────────────────────\n')

            if edit_option == 2:
                data_sects[4] = input('Enter new due date: ')
                new_data = ', '.join(data_sects)
                data[option-1] = new_data

                print(f'──────────────────────────────────────────\n'
                      f'The due date of task {option} is now {data_sects[4]}.\n'
                      f'──────────────────────────────────────────\n')

            # write new data to tasks.txt
            f_tasks = open('tasks.txt', 'w')
            for line in data:
                f_tasks.write(line)

            f_tasks.close()

            break

    return


# generate reports
def gen_reports():
    f_tasks = open('tasks.txt', 'r')
    data = f_tasks.readlines()
    f_tasks.close()

    # counters
    total_tasks = 0
    total_completed = 0
    total_uncompleted = 0
    total_overdue = 0

    # dictionary for stats for each user
    user_stats = {}

    # calculate total no. of users
    total_users = 0
    for k in dict_users.keys():
        total_users += 1
        user_stats[k] = [0, 0, 0, 0]

    for line in data:
        data_split = line.replace('\n', '').split(', ')
        total_tasks += 1

        if data_split[-1] == 'Yes':
            total_completed += 1

            # increase total and total completed tasks for user
            for k, v in user_stats.items():
                if k == data_split[0]:
                    user_stats[k] = [v[0] + 1, v[1] + 1, v[2], v[3]]

        else:
            total_uncompleted += 1

            # increase total and total uncompleted tasks for user
            for k, v in user_stats.items():
                if k == data_split[0]:
                    user_stats[k] = [v[0] + 1, v[1], v[2] + 1, v[3]]

            # get today's date
            today = datetime.datetime.today()
            due_date = datetime.datetime.strptime(data_split[4].strip(), '%d %b %Y')

            if due_date < today:
                total_overdue += 1

                # increase total overdue tasks for user
                for k, v in user_stats.items():
                    if k == data_split[0]:
                        user_stats[data_split[0]] = [v[0], v[1], v[2], v[3] + 1]

    px_uncompleted = (total_uncompleted/total_tasks) * 100
    px_overdue = (total_overdue/total_tasks) * 100

    # output
    task_output = ''
    task_output += f'{total_tasks}, '
    task_output += f'{total_completed}, '
    task_output += f'{total_uncompleted}, '
    task_output += f'{total_overdue}, '
    task_output += f'{round(px_uncompleted, 2)}, '
    task_output += f'{round(px_overdue, 2)}\n'

    # write to file
    f_task_report = open('task_overview.txt', 'w+')
    f_task_report.write(task_output)
    f_task_report.close()

    # write user reports to user_overview.txt
    user_report_w = open('user_overview.txt', 'w+')
    user_report_w.write(f'{total_users}\n')
    user_report_w.write(f'{total_tasks}\n')
    user_report_w.close()

    user_report_a = open('user_overview.txt', 'a')
    for k, v in user_stats.items():
        px_user_total = (v[0]/total_tasks) * 100
        px_user_completed = (v[1]/v[0]) * 100
        px_user_uncompleted = (v[2]/v[0]) * 100
        px_user_overdue = (v[3]/v[0]) * 100

        # output
        user_output = ''
        user_output += f'{k}, '
        user_output += f'{v[0]}, '
        user_output += f'{round(px_user_total, 2)}, '
        user_output += f'{round(px_user_completed, 2)}, '
        user_output += f'{round(px_user_uncompleted, 2)}, '
        user_output += f'{round(px_user_overdue, 2)}\n'

        user_report_a.write(user_output)

    user_report_a.close()

    return


# display statistics
def display_stats():
    # generate reports
    gen_reports()

    # read overview files
    f_task_report = open('task_overview.txt', 'r')
    task_report = f_task_report.readlines()
    f_task_report.close()

    f_user_report = open('user_overview.txt', 'r')
    user_report = f_user_report.readlines()
    f_user_report.close()

    # print task report
    while True:
        for line in task_report:
            task_data = line.replace('\n', '').split(', ')

        task_output = '───────────────────────────────────────────\n'
        task_output += f'Total tasks: {task_data[0]}\n'
        task_output += f'Total completed tasks: {task_data[1]}/{task_data[0]}\n'
        task_output += f'Total uncompleted tasks: {task_data [2]}/{task_data[0]}, {task_data[4]}%\n'
        task_output += f'Total overdue tasks: {task_data[3]}/{task_data[0]}, {task_data[5]}%\n'
        task_output += '───────────────────────────────────────────\n'

        print(task_output)

        break

    # print user report
    while True:
        i = 0
        for line in user_report:
            user_data = line.replace('\n', '').split(', ')

            i += 1
            if i == 1:
                print(f'Total number of users: {line[0]}')

            elif i == 2:
                print(f'Total number of tasks: {line[0]}\n')

            else:
                user_output = f'──────────────────── {user_data[0]} ─────────────────────\n'
                user_output += f'Tasks assigned to {user_data[0]}: {user_data[1]}/{task_data[0]}, {user_data[2]}%\n'
                user_output += f'Completed tasks: {user_data[3]}%\n'
                user_output += f'Uncompleted tasks: {user_data [4]}%\n'
                user_output += f'Overdue tasks: {user_data[5]}%\n'
                user_output += '────────────────────────────────────────────────\n'

                print(user_output)

        break
    return


#====Login Section====
# dictionary of usernames and passwords
dict_users = users()

# counter for failed log-ins
int_attempts = 0

while int_attempts < 10:
    while True:
        str_username = input('Enter username: ')

        # error if username not in file
        if str_username not in dict_users.keys():
            print('That username does not exist. Please try again.')
            int_attempts += 1
            continue

        break

    # user inputs password if registered
    while True:
        str_password = input('Enter password: ')

        # re-enter password if incorrect
        if str_password != dict_users[f'{str_username}']:
            print('Incorrect password. Try again.')
            int_attempts += 1
            continue

        if str_password == dict_users[f'{str_username}']:
            # print welcome and exit to main menu
            output = ''
            output += '\n────────────────────────\n'
            output += f'Welcome, {str_username}.\n'
            output += '────────────────────────\n'
            print(output)

        break
    break

# exit program if too many password attempts made
if int_attempts > 10:
    print('You have entered too many incorrect passwords and been locked out.')
    exit()

while True:
    # presenting the menu to the user and
    # making sure that the user input is converted to lower case.
    if str_username == 'admin':
        menu = input('''Select one of the following options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - View my tasks
gr - Generate reports
s - Display statistics
e - Exit
: ''').lower()

    else:
        menu = input('''Select one of the following options below:
a - Adding a task
va - View all tasks
vm - View my tasks
e - Exit
        : ''').lower()

    if menu == 'r':
        if str_username == 'admin':
            reg_user()

        # print error if user not admin
        else:
            print('You are not authorised to do that.')
            break

    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif menu == 'gr':
        if str_username == 'admin':
            gen_reports()

        else:
            print('You are not authorised to do that.')
            break

    elif menu == 's':
        if str_username == 'admin':
            display_stats()

        else:
            print('You are not authorised to access this.')

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")