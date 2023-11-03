# BINARY TREES

# import collections

# Node = collections.namedtuple('Node', ['left', 'right', 'value'])

# def contains(root, value):
#     if root is None:
#         return False
#     elif root.value == value:
#         return True
#     elif root.value < value:
#         return contains(root.right, value)
#     else:
#         return contains(root.left, value)

# n1 = Node(value=1, left=None, right=None)
# n3 = Node(value=3, left=None, right=None)
# n2 = Node(value=2, left=n1, right=n3)

# print(contains(n2, 3))

#CLASS INHERITANCE AND OVERWRITING

# class TextInput:
#     def __init__(self):
#         self.char = ''

#     def add(self, character):
#         self.char += character
#         return self.char
  
#     def get_value(self):
#         return self.char
    
# class NumericInput(TextInput):
#     def add(self, character):
#         if character.isdigit():
#             self.char += character
#             return self.char
#         else:
#             return ''
    

# if __name__ == '__main__':
#     input = NumericInput()
#     input.add("1")
#     input.add("a")
#     input.add("0")
#     print(input.get_value())

# TORTOISE AND HARE ALGO FOR CHECKING CYCLES

# class Song:
#     def __init__(self, name):
#         self.name = name
#         self.next = None

#     def next_song(self, song):
#         self.next = song 
    
#     def is_in_repeating_playlist(self):
#         """
#         :returns: (bool) True if the playlist is repeating, False if not.
#         """
#         slow = self
#         fast = self.next
#         while fast is not None and fast.next is not None:
#             if slow == fast:
#                 return True
#             slow = slow.next
#             fast = fast.next.next
#         return False


# first = Song("Hello")
# second = Song("Eye of the tiger")
    
# first.next_song(second)
# second.next_song(first)
    
# print(first.is_in_repeating_playlist())

#create tuple with student name and major named students. 

# students = [('Allen Anderson', 'Engineering'),
#      ('Edgar Einstein', 'Finance'),
#      ('Farrah Finn', 'Business')]

# def add_student(students, name, major):
#     students.append((name, major))

# def update_student(students, index, name, major):
#     students[index] = name, major

# def find_student_by_name(students, name):
#     return [student for student in students if name in student[0]]

# def get_all_majors(students):
#     return [student[1] for student in students]



class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        return [[ingredient, topping] for ingredient in self.ingredients for topping in self.toppings]

if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
    print(machine.scoops())