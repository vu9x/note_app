import csv
from datetime import datetime

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
