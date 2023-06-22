import csv
import os
from Model_Note import Note


class editor_scv:

    def __init__(self, file_name):
        self.__path = os.getcwd()
        self.__file_name = file_name + '.csv'
        self.__file_path = os.path.join(self.get_path(), self.get_file_name())

    @property
    def get_path(self):
        return self.__path

    @property
    def get_file_name(self):
        return self.__file_name

    @property
    def get_file_path(self):
        return self.__file_path

    @classmethod
    def create_file(cls):
        with open(self.get_file_path(),'a+') as file:
            pass

    @classmethod
    def read_file(cls):
        with open(self.get_file_path(), 'r') as file:
            reader = csv.DictReader(file)
            notes = list(reader)

        for note in notes:
            Note(
                id=note.get('id'),
                header=note.get('header'),
                body=note.get('body'),
                created_at=note.get('created_at'),
                modified_at=note.get('modified_at')
            )

    @classmethod
    def save_file(cls):
        with open(self.get_file_path(), 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'header', 'body', 'created_at', 'modified_at'])
            writer.writeheader()
            writer.writerows(Note.Note_list)

    @classmethod
    def delete_file(cls):
        os.remove(self.get_file_path)

    @classmethod
    def lfiles_in_directory(cls):
        files = [f for f in os.listdir(self.get_file_path()) if os.path.isfile(f)]

        if not bool(files):
            return print("Папка пустая")

        for file in files:
            print(file)