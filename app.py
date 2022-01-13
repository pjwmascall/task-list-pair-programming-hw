from modules.task_list import *
from modules.output import *
from data.task_list import *
from modules.input import *

while (True):
    print_menu()
    if (option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        task = get_task_with_description(tasks, option_4_input)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        print_list(get_tasks_taking_at_least(tasks, option_5_input))
    elif option == '6':
        print(get_task_with_description(tasks, option_6_input))
    elif option == '7':
        task = create_task(option_7_input_description, option_7_input_time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")