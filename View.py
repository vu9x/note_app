class Menu:

    file_menu = "1. Create file\n" \
                "2. Open file\n" \
                "3. Save file\n" \
                "4. Delete file\n" \
                "5. Show files in directory"

    note_menu = "1. Add new note\n" \
                "2. Show all notes\n" \
                "3. Show specific note\n" \
                "4. Edit current note\n" \
                "5. Delete note"

    success_message = "Успешно"


class View(Menu):

    @classmethod
    def show_files_in_directory(cls, file_list: list):
        # if not bool(file_list):
        #     return print("No files in directory")
        #
        # for file in file_list:
        #     print(file)
        print("show files")

    @classmethod
    def show_file_menu(cls):
        print(f"{'*' * 10}\n"
              f"{super().file_menu}\n"
              f"{'*' * 10}\n")

    @classmethod
    def show_note_menu(cls):
        print(f"{'*' * 10}\n"
              f"{super().note_menu}\n"
              f"{'*' * 10}")

    @classmethod
    def show_success_message(cls):
        print(super().show_success_message())

    @classmethod
    def user_choice(cls):
        return input("Введите номер команды: ")

    @classmethod
    def print_my_notes(cls, notes):
        print(notes)