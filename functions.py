FILEPATH = 'todo.txt'

def read_todos(filepath= FILEPATH):
    """ Read a text file and return values in a list"""
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos

def write_todos(todos_arg,filepath= FILEPATH):
    """Write todos to a text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

# print(f"I am outside. {__name__}")
# if __name__ == "__main__":
#     print("I am inside")

def separate_feet_inch(height_input_local):
    parsed = height_input_local.split(" ")
    feet = float(parsed[0])
    inch = float(parsed[1])
    return feet, inch

def convert(feet, inch):
    meters = feet*0.3048 + inch*0.0254
    return meters

def count(phrase):
    return phrase.count('.')