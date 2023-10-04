# Write a python class which has 2 methods get_string and print_string. get_string takes a string from the user and print_string prints the string in reverse order 

class StringManipulator:
    def get_string(self):
        self.input_string = input("Enter a string: ")

    def print_string_reverse(self):
        print("Reversed string:", self.input_string[::-1])

# Usage
manipulator = StringManipulator()
manipulator.get_string()
manipulator.print_string_reverse()
