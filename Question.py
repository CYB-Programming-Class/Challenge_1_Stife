# Question class. Keeping track of what I want to ask and the answers to those questions.
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
# Self represents the object itself. Everytime you create an object you need to know which object your creating. Ex:
# class Human:
#   def __init__(self, name, gender):
#       self.name = name
#       self.gender = gender
#
# will = Human("William", "Male")
#
# will = self in this case because the object is will. Self = the object it self.
# Self is the specific object created by a class. Self is a temporary place-holder for the object.
#
# "self.prompt = prompt" and "self.name = name" are instant variables. They are unique to each object.
# Using Human Ex: self.name = name is equal to will.name = name. Will's name is equal to whatever we pass in as his name
# When we use self we are saying that this variable belongs to the entire class, not just that specific function.
#
# __init__ is an initialization method. When you create any object from a class, the first thing it does is look for an
# __init__ function and it calls whatever is in the function.
