class Person:
    def __init__(self, name, address, phone):
        self.__name = name
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address
    
    def get_phone(self):
        return self.__phone

    def print_person(self):
        print("Name: ", self.__name)
        print('Addr: ', self.__address)
        print('Phone: ', self.__phone)

class Customer(Person):

    def __init__(self,name, address, phone, customer_num, mailing):

        Person.__init__(self, name, address, phone)
        self.__customer_num = customer_num
        self.__mailing = mailing

   

    def print_person(self):
        print("Method 1")
        print('Name:', Person.get_name(self))
        print("Addr:", Person.get_address(self))
        print("Phone: ", Person.get_phone(self))

        print()
        print()

        print('Method 2')
        Person.print_person(self)
        print('Customer Numnber:', self.__customer_num)
        if self.__mailing:
            print("On Mailing List: Yes")
        else:
            print("On Mailing List: No")




    


