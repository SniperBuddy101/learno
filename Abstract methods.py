# We are creating an abstract method in this.

# Creating a file error exception.
class FileError(Exception):
    pass


# Importing the Abstract Base Class method from the abstract base class module.
from abc import ABC, abstractmethod


# Creating a "Stream" class and making it a sub class of "ABC".
class Stream(ABC):
    def __init__(self, file):  # Creating the constructor method.
        self.opened = False  # Defining the value of opened attribute.
        self.file = file  # Defining the value of file attribute. This is file/network stream's name

    # Defining the open method.
    def open(self):
        if self.opened:
            raise FileError(f"File - {self.file} is already opened.")  # Raising an error if the file is already opened
        self.opened = True  # Setting the opened attribute to true.
        print(f"File - {self.file} opened.")  # Printing the message.

    # Defining the close method.
    def close(self):
        if not self.opened:  # An if statement to determine if the file is already closed.
            raise FileError(f"File - {self.file} is already closed")  # Raising an error if the file is already closed
        self.opened = False  # Setting the opened attribute to False.
        print(f"File - {self.file} closed.")  # Printing the message.

    # Using the @abstractmethod decorator to make the read method an abstract method.
    @abstractmethod
    def read(self):
        pass  # Using pass so that this method doesn't do a thing in this class.


# Defining the FileStream class for files.
class FileStream(Stream):  # Making the FileStream class a subclass of Stream.
    def read(self):  # This read method is an abstract method. It is mandatory.
        print(f"File stream - {self.file} reading begins..")  # Printing the message of a successful read.


# Defining the NetworkStream class for network streams.
class NetworkStream(Stream):  # Making this class a subclass of the Stream class.
    def read(self):  # This read method is an abstract method. It is mandatory.
        print(f"Network stream - {self.file} reading begins..")  # Printing the message of a successful read.


# Creating an instance of the FileStream class.
file1 = FileStream("File.txt")  # Giving "File.text" as an arguement for the "file" parameter in the Stream's
# constructor method.

file1.open()  # Calling the open method.
file1.read()  # Calling the read method (an abstract class method).
file1.close()  # Calling the close method.
