# Write a Python class to reverse a string word by word. Input string : 'hello .py' Expected Output : '.py hello'

class StringReverser:
    def reverse_words(self, s):
        words = s.split()
        words.reverse()
        return ' '.join(words)

# Usage
reverser = StringReverser()
input_str = 'hello .py'
print(reverser.reverse_words(input_str))  
