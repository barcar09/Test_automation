
class Employee:

    def __init__ (self,name, surname):
        self.name = name
        self.surname = surname
        self.position = type(self).__name__


    def print_init(self):
        print(self.name, self.surname, self.position)


class Programmer(Employee):
    pass


class Manager(Employee):
    "this is description of the class"
    pass




class Base:

    __private = "PRIVATE"

    def print_method(self):
        return self.__private

class Child(Base):

    def __init__(self,argument):

        self.baby = argument

class ErrCantEmploy:
    def name_of_instance(instance):
        check_name = instance.name
        check_surname = instance.surname
        if type(check_name) != str:
            raise TypeError("{0} is not a string".format(check_name))
        elif type(check_surname) != str:
            raise TypeError("{0} is not a string".format(check_surname))



Kuba = Programmer("Kuba","gorzedow")
Bartek = Employee("Bartek", "Barcikowski")
Hania_1 = Manager("Hania",5)

if __name__ == "__main__":
    ErrCantEmploy.name_of_instance(Hania_1)