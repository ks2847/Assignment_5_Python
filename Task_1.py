# Create a Dictionary of Student's marks
try:
    dict = {'john':86,'Maria':92,'Sophia':89,'Michael':95}
    name = input("Enter Student's name: ")
    marks = dict[name]
    print("{}'s marks: {}".format(name,marks))
except KeyError:
    print("Student not found")



# dict = {'john':86,'Maria':92,'Sophia':89,'Michael':95}
# name = input("Enter Student's name: ")
# marks = dict[name]
# print("{}'s marks: {}".format(name,marks))    