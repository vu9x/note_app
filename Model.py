import os
import csv
from datetime import datetime

class Editor_csv:
    def __init__(self, file_name):
        self.__file_name = file_name + '.csv'
        self.__path = os.path.join(os.getcwd(), "working_folder")
        self.__file_path = os.path.join(self.get_path, self.get_file_name)

        #Create Working Directory if not exist
        if not os.path.exists(fr'{self.get_path}'):
            os.mkdir(fr'{self.get_path}')

    @property
    def get_path(self):
        return self.__path

    @property
    def get_file_name(self):
        return self.__file_name

    @property
    def get_file_path(self):
        return self.__file_path

    def create_file(self):
        with open(fr'{self.get_file_path}', 'a+') as file:
            print(self.get_file_name, " создан")

    def read_file(self):
        # with open(cls.get_file_path, 'r') as file:
        with open(fr'{self.get_file_path}', 'r') as file:
            reader = csv.DictReader(file)
            notes = list(reader)

        for note in notes:
            tmp = Note(header=note.get('header'),
                       body=note.get('body'),
                       id=note.get('id'),
                       created_at=note.get('created_at'),
                       modified_at=note.get('modified_at'))

        return Note.note_list

    def save_file(self, Note_List):
        with open(self.get_file_path, 'w') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'header', 'body', 'created_at', 'modified_at'])
            writer.writeheader()
            writer.writerows(Note_List)

    def delete_file(cls):
        os.remove(cls.get_file_path)


class Note:
    note_list = []

    #Note constructor
    def __init__(self, header: str, body: str, id=None, created_at=None, modified_at=None):

        #Attributes should be set without user prompt
        self.__id = str(len(Note.note_list) + 1) if id is None else id
        self.__created_at = datetime.now() if created_at is None else created_at
        self.__modified_at = datetime.now() if modified_at is None else modified_at

        #Attributes set by user prompt
        self.__header = header
        self.__body = body
        # Add the note to the class list
        Note.note_list.append({'id':self.__id,
                               'header':self.__header,
                               'body':self.__body,
                               'created_at': self.__created_at,
                               'modified_at': self.__modified_at})

    # Note Getters
    @property
    def id(self):
        return self.__id

    @property
    def created(self):
        return self.__created_at

    @property
    def modified(self):
        return self.__modified_at

    @property
    def header(self):
        return self.__header

    @property
    def body(self):
        return self.__body

    # Note setters
    @id.setter
    def set_id(self, value):
        self.__id = value

    @created.setter
    def set_created(self, value):
        self.__created_at = value

    @modified.setter
    def set_modified(self, value):
        self.__modified_at = value

    @header.setter
    def header(self, header: str):
        self.__header = header

    @body.setter
    def body(self, body: str):
        self.__body = body

    def __str__(self):
        message = f"id: {self.id}, " \
                  f"create: {self.created}, " \
                  f"last modify: {self.modified}, " \
                  f"header: {self.header}, " \
                  f"body: {self.body}"
        return message

    def __repr__(self):
        return str({'id':self.id,
                'header':self.header,
                'body':self.body,
                'created_at':self.created,
                'modified_at':self.modified})

    @classmethod
    def remove_note(cls, index):
        return Note.note_list.pop(index-1)
