class FileError(Exception):
    pass


from abc import ABC, abstractmethod


class Stream(ABC):
    def __init__(self, file):
        self.opened = False
        self.file = file

    def open(self):
        if self.opened:
            raise FileError(f"File - {self.file} is already opened.")
        self.opened = True
        print(f"File - {self.file} opened.")

    def close(self):
        if not self.opened:
            raise FileError(f"File - {self.file} is already closed")
        self.opened = False
        print(f"File - {self.file} closed.")

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print(f"File stream - {self.file} reading begins..")


class NetworkStream(Stream):
    def read(self):
        print(f"Network stream - {self.file} reading begins..")


file1 = FileStream("File.txt")

file1.open()
file1.read()
file1.close()
