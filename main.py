import Model
from View import View
from Controller import Controller

def main():
    start = Controller(Model, View)
    start.hello_world()
    start.files_in_directory()
    command = True
    while command is True:
        command = start.file_manager()

    print("Вы вышли из программы")

if __name__ == "__main__":
    main()
