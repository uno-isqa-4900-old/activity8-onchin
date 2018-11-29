import csv


class Customer:

    def __init__(self, ID, fName, lName, company,
                 address, city, state, zipcode):
        self.ID = ID
        self.fName = fName
        self.lName = lName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode


def display_title():
    print()
    print("Customer Viewer")
    print()


def csv_reader():
    cust_list = []
    with open('customers.csv', 'r') as file:
        reader = csv.reader(file)
        for customer in reader:
            cust_list.append(customer)
    return cust_list


def find_customer(cust_id, customers):
    for customer in customers:
        if cust_id == customer[0]:
            print(customer[1], customer[2])
            if customer[3] != "":
                print(customer[3])
            print(customer[4])
            print(customer[5] + ", " + customer[6], customer[7])
            print()
            return cust_id


def main():
    display_title()
    customer_list = csv_reader()

    cont = "y"
    while cont == "y":
        cust_id = str(input("Enter Customer ID: "))
        print()
        id_return = find_customer(cust_id, customer_list)
        if id_return != cust_id:
            print("No customer with that ID.")
            print()
        cont = input("Continue? (y/n): ")
        cont = cont.lower()
        print()

    print("Bye")


if __name__ == '__main__':
    main()




