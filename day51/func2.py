#3
#Mixing Positional and Keyword Arguments
def student_info(name,age,course):
    print(name,"is",age,"years old and studying",course)
student_info("Pavani",age="21",course="Python")

#4
#Passing data types
def print_numbers(the_list):
    for num in the_list:
        print(num)
the_list=[5,10,15]
print_numbers(the_list)

#5
def print_person(person):
    print("Name:",person["name"])
    print("Age:",person["age"])
person={"name":"Pavani","age":21}
print_person(person)

    
    