import Model
from View import View
import os

class Controller:

    def __init__(self, Model, View):
        self.__model = Model
        self.__view = View

    @property
    def get_model(self):
        return self.__model
    @property
    def get_view(self):
        return self.__view

    def show_file_menu(self):
        self.get_view.show_file_menu()

    def show_note_menu(self):
        self.get_view.show_note_menu()

    def file_manager(self):
        self.show_file_menu()
        choice = self.get_view.user_choice()
        name = input("Введите название файла: ")

        match choice:
            case '1':
                editor = self.get_model.Editor_csv(name)
                return editor.create_file()
            case '2':
                my_notes = self.get_model.Editor_csv.read_file(self.get_model.Editor_csv.get_file_path)
                self.get_view.print_my_notes(my_notes)
                return my_notes


ctr = Controller(Model, View)
ctr.file_manager()

# v = os.path.join(os.getcwd(), "working_folder")
# print(type(v))
# print(v)