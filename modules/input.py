
def select_option():
    return input("\nSelect an option 1, 2, 3, 4, 5, 6, 7, display (m)enu or (q)uit: ")

def option_4_input():
    return input("\nEnter task description to search for: ")

def option_5_input():
    try:
        return int(input("\nEnter task duration: "))
    except ValueError:
        print("\nPlease enter an integer")
        return option_5_input()

def option_6_input():
    return input("\nEnter task description to search for: ")

def option_7_input_description():
    return input("\nEnter description: ")
    
def option_7_input_time_taken():
    try:
        return int(input("\nEnter time taken: "))
    except ValueError:
        print("\nPlease enter an integer")
        return option_7_input_time_taken()