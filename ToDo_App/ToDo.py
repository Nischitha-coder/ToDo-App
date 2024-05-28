#from Functions import get_todos, write_todos
import Functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while (True):
    choice = input("Type add, show, edit, complete, exit: ")
    choice = choice.strip()

    if choice.startswith('add'):
        todo = Functions.get_todos()

        event = choice[4:] + "\n"
        todo.append(event.capitalize())

        Functions.write_todos(todo)

    elif choice.startswith('show'):
        todo = Functions.get_todos()
        for i, j in enumerate(todo):
            j = j.strip('\n')
            print(f"{i + 1}.{j.capitalize()}")

    elif choice.startswith('edit'):
        try:
            index = int(choice[5:])

            todo = Functions.get_todos()

            new_event = input("Enter the new event: ")
            todo[index - 1] = new_event.capitalize() + '\n'

            Functions.write_todos(todo)
        except ValueError:
            print("Your command is not valid.")
            continue

    elif choice.startswith('complete'):
        try:
            completed = int(choice[9:])

            todo = Functions.get_todos()

            event = todo[completed - 1].strip('\n')
            todo.pop(completed - 1)

            Functions.write_todos(todo)

            message = f"The event {event} is completed"
            print(message + '\n')
        except IndexError:
            print("There is no item with that number")
            continue

    elif choice.startswith('exit'):
        print("Byeee!!!")
        break

    else:
        print("Invalid command")
