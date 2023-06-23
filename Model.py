import os
import csv
import datetime

class Editor_csv:

    def __init__(self, file_name):
        self.__path = os.path.join(os.getcwd(), "working_folder")
        self.__file_name = file_name + '.csv'
        self.__file_path = os.path.join(self.get_path, self.get_file_name)

    @property
    def get_path(self):
        return self.__path

    @property
    def get_file_name(self):
        return self.__file_name

    @property
    def get_file_path(self):
        return self.__file_path

    # @get_file_name.setter
    # def set_file_name(self, file_name: str):
    #     self.__file_name = file_name + '.csv'
    #
    # @get_file_path.setter
    # def set_file_path(self):
    #     self.__file_path = os.path.join(self.get_path, self.get_file_name)
    #
    # def abs_path(self, file_name):
    #     self.set_file_name = file_name
    #     self.set_file_path

    def create_file(self):
        print(self.get_path)
        print(self.get_file_name)
        print(self.get_file_path)
        if not os.path.exists(fr'{self.get_path}'):
            os.mkdir(fr'{self.get_path}')

        with open(fr'{self.get_file_path}', 'a+') as file:
            print(self.get_file_name, " создан")


    def read_file(cls, file_path):
        # with open(cls.get_file_path, 'r') as file:
        with open(fr'{file_path}', 'r') as file:
            reader = csv.DictReader(file)
            notes = list(reader)

        filled_note_file = Note
        for note in notes:
            Note(
                id=note.get('id'),
                header=note.get('header'),
                body=note.get('body'),
                created_at=note.get('created_at'),
                modified_at=note.get('modified_at')
            )
        return filled_note_file

    @classmethod
    def save_file(cls):
        with open(cls.get_file_path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'header', 'body', 'created_at', 'modified_at'])
            writer.writeheader()
            writer.writerows(Note.Note_list)

    @classmethod
    def delete_file(cls):
        os.remove(cls.get_file_path)

    @classmethod
    def listf_in_directory(cls):
        files = [f for f in os.listdir(cls.get_path) if os.path.isfile(f)]
        return files

class Note:
    note_list = []

    #Note constructor
    def __init__(self, header: str, body: str, id=None, created_at=None, modified_at=None):

        #Attributes should be set without user prompt
        if id is None:
            self.__id = self.set_id()
        else:
            self.__id = id

        if created_at is None:
            self.set_created()
        else:
            self.__created_at = created_at

        if modified_at is None:
            self.set_modified()
        else:
            self.__modified_at = modified_at

        #Attributes set by user prompt
        self.__header = header
        self.__body = body

        # Add the note to the class list
        Note.note_list.append({
            "id": self.get_id(),
            "created_at": self.get_created(),
            "modified_at": self.get_modified(),
            "header": self.get_header(),
            "body": self.get_body()
        })

    @property
    def get_id(self):
        return self.__id

    @get_id.setter
    def set_id(self):
        self.__id = len(Note.note_list)

    @property
    def get_created(self):
        return self.__created_at

    @get_created.setter
    def set_created(self):
        self.__created_at = datetime.now()

    @property
    def get_modified(self):
        return self.__modified_at

    @get_modified.setter
    def set_modified(self):
        self.__modified_at = datetime.now()

    @property
    def get_header(self):
        return self.__header

    @get_header.setter
    def set_header(self, header: str):
        self.__header = header

    @property
    def get_body(self):
        return self.__body

    @get_body.setter
    def set_body(self, body: str):
        self.__body = body

    def __str__(self):
        message = f"create: {self.get_created()}\n" \
                  f"las modify: {self.get_modified()}\n" \
                  f"id: {self.get_id()}\n" \
                  f"header: {self.get_header()}\n" \
                  f"body: {self.get_body()}"

        print(message, "_" * 10)

    def __repr__(self):
        return f"id: {self.get_id()}, {self.get_header()}"

    # @classmethod
    # def edit_note(cls, index: int, header: str, body:str):
    #     Note.note_list[index - 1]['header'] = header
    #     Note.note_list[index - 1]['body'] = body
    #     Note.note_list[index - 1]['modified_at'] = modified()

    def remove_note(self, index=int):
        return Note.note_list.pop(index-1)

# c = Editor_csv("test")
# print(type(c.get_file_name))
# print(type(c.get_path))
# print(c.get_file_path)