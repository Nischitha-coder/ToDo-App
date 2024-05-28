FILEPATH = "TodoList.txt"

def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todo_local = file_local.readlines()
    return todo_local


def write_todos(todo_arg, filepath=FILEPATH, ):
    with open(filepath, 'w') as file:
        file.writelines(todo_arg)


# to avoid print this line
if __name__ == "__main__":
    print("Hello")
