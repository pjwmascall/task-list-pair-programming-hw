from modules.task_list import *
from modules.output import *
from data.task_list import *
from modules.input import *

while (True):
    print_menu()
    option = select_option()
    if (option.lower() == 'q'):
        break
    elif option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        task = get_task_with_description(tasks, option_4_input())
        if task is not None:
            mark_task_complete(task)
            print("\nTask marked complete")
        else:
            print("\nTask not found")
    elif option == '5':
        print_list(get_tasks_taking_at_least(tasks, option_5_input()))
    elif option == '6':
        task = get_task_with_description(tasks, option_6_input())
        if task is not None:
            print_task(task)
        else:
            print("\nTask not found")
    elif option == '7':
        task = create_task(option_7_input_description(), option_7_input_time_taken())
        tasks.append(task)
    else:
        print("\nInvalid Input - choose another option")