FILEPATH = "todos.txt"

#function definition with filepath as a parameter(argument) and return todos
def get_todos(filepath=FILEPATH):
    """
    read a text file and return the list of to-do items.
    """
    with open(f'{filepath}', 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


#no need to return because it modifies the file. procedure function
def write_todos(todos_arg, filepath=FILEPATH):
    """write the to-do items list in the text file"""
    with open(f'{filepath}', 'w') as file:
        file.writelines(todos_arg)

print(__name__)
#only runs when running functions or the file directly
if __name__ ==  "__main__":
    print("hello")
    print(get_todos())