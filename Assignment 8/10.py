# Write a Python program to get the class name of an instance in Python.

class ClassNameGetter:
    def get_class_name(self, instance):
        return instance.__class__.__name__

# Usage
getter = ClassNameGetter()
Circle = 0
obj = Circle(10)
print(getter.get_class_name(obj))
