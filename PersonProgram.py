import PersonClass as pc

def main():

    name = "John"
    address = "123 Main St"
    phone = "123-456-7890"
    customer_num = 123
    mailing = True


    person1 = pc.Person(name, address, phone)

    customer1= pc.Customer(name, address, phone, customer_num, mailing)

    person1.print_person()

    print()
    print()
    print()

    customer1.print_person()


main()

