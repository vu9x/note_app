class View():
    #Menu
    @classmethod
    def show_file_menu(cls):
        file_menu = "1. Create file\n" \
                    "2. Open file\n" \
                    "3. Delete file\n" \
                    "4. Show files in directory\n" \
                    "5. Close file manager"
        print(f"{'*' * 10}\n"
              f"{file_menu}\n"
              f"{'*' * 10}\n")

    @classmethod
    def show_note_menu(cls):
        note_menu = "1. Add new note\n" \
                    "2. Show all notes\n" \
                    "3. Edit current note\n" \
                    "4. Save file\n" \
                    "5. Delete note\n" \
                    "6. Back to file menu"
        print(f"{'*' * 10}\n"
              f"{note_menu}\n"
              f"{'*' * 10}")

    #Print Messages
    @classmethod
    def hello_world(cls):
        print("Добро пожаловать в редактор заметок v1.0")

    @classmethod
    def show_success_message(cls):
        print("Успешно")

    @classmethod
    def show_command_not_exist(cls):
        print("Вы ввели не существующую команду")

    #User Inputs
    @classmethod
    def show_file_name(cls):
        return input("Введите название файла: ")

    @classmethod
    def show_command_input(cls):
        return input("Введите номер команды: ")

    @classmethod
    def show_header_input(cls):
        return input("Введите заголовок заметки: ")

    @classmethod
    def show_body_input(cls):
        return input("Введите вашу заметку: ")

    @classmethod
    def show_note_index(cls):
        return input("Введите идентификатор заметки: ")

    @classmethod
    def show_files_in_directory(cls, file_list: list):
        if not bool(file_list):
            return print("No files in directory")

        for file in file_list:
            print(file)

    @classmethod
    def show_my_notes(cls, notes):
        for note in notes:
            print(note)
