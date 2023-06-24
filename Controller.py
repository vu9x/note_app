import Model
import os
from View import View
from datetime import datetime

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

    def hello_world(self):
        self.get_view.hello_world()

    # Show files in working directory
    def files_in_directory(self):
        files = os.listdir(os.path.join(os.getcwd(), "working_folder"))
        file_names = []
        for file in files:
            file_names.append(file.split('.')[0])
        return file_names
    def show_files_in_directory(self, file_names):
        self.get_view.show_files_in_directory(file_names)

    def file_manager(self):
        #User input
        file_names = self.files_in_directory()
        self.get_view.show_file_menu()
        editor_commands = ['1', '2', '3']

        command = self.get_view.show_command_input()

        if command in editor_commands:
            file_name = self.get_view.show_file_name()
            editor = self.get_model.Editor_csv(file_name)

        if command == '1':
            editor.create_file()
        elif command == '2':
            if file_name in file_names:
                editor.read_file()
                self.note_manager(editor)
            else: print("Файл не существует")
        elif command == '3':
            editor.delete_file() if file_name in file_names else print("Файл не существует")
        elif command == '4':
            file_names = self.files_in_directory()
            self.show_files_in_directory(file_names)
        elif command == '5':
            return False
        return True

    def note_manager(self, editor):
        while True:
            note_list = self.get_model.Note.note_list
            commands = ['1', '2', '3', '4', '5']
            self.get_view.show_note_menu()
            command = self.get_view.show_command_input()

            if command == '1':
                header = self.get_view.show_header_input()
                body = self.get_view.show_body_input()
                my_note = self.get_model.Note(header=header, body=body)
            elif command == '2':
                self.get_view.show_my_notes(note_list)
            elif command == '3':
                index = self.get_view.show_note_index()
                header = self.get_view.show_header_input()
                body = self.get_view.show_body_input()

                for note in note_list:
                    if note.get('id') == index:
                        note['header'] = header
                        note['body'] = body
                        note['modified_at'] = datetime.now()

            elif command == '4':
                editor.save_file(note_list)
            elif command == '5':
                index = self.get_view.show_note_index()
                for note in note_list:
                    if note.get('id') == index:
                        self.get_model.Note.note_list.remove(note)
            elif command == '6':
                return False
