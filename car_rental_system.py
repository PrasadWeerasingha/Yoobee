import sqlite3

import vehicle
from connection import Connection
from client import Client
from vehicle import Vehicle
from vehicle import Car, Dump_Truck
from userlogin import UserLogin
from createtable import CreateTable

# Function to display menu options
def display_menu():
    print("\n1. Login")
    print("2. Exit")

# Function to display menu options 2 for Admin once pass the login
def display_menu2():
    print("\n1. Display Vehicles")
    print("2. Add/delete Vehicle")
    print("3. Rent Vehicle")
    print("4. Reporting Rented Information")
    print("5. Exit")
# Function to display menu options 3 for Transaction user once pass the login
def display_menu3():
    print("\n1. Display Vehicles")
    print("2. Rent Vehicle")
    print("3. Reporting Rented Information")
    print("4. Exit")

def display_menu4():
    print("\n1. Add New Vehicle")
    print("2. Update or Delete Exesting Vehicle")
    print("3. Exit")

#Create Fuction to retuen all Values from Vehical table
def display_records(records):
    if not records:
        print("No records found.")
        return
    # Print header
    print(f"{'ID':<8}{'BRAND':<15}{'TYPE':<15}{'MAKE_YEAR':<10}{'DOORS':<10}{'PRICE PER WEEK':<15}{'AVAILABILITY':<15}{'REG_NO':<15}{'BED LENGHT':<15}")

    # Print records
    for record in records:
        print(f"{record[0]:<8}{record[1]:<15}{record[2]:<15}{record[3]:<10}{record[4]:<10}{record[5]:<15}{record[6]:<15}{record[7]:<15}{record[8]:<15}")


# Main function
def main():
    db_file = "car_rental_system.db"
    connection = Connection(db_file)
    connection.connect()

    # Creating tables and performing other setup tasks

    #while True:
    create_table = CreateTable(connection)
    create_table.create_user_table()
    create_table.create_vehicle_table()
    display_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        choice_Other = 0
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        user_login = UserLogin(connection)
        if user_login.login(username, password):
    # Proceed with car rental system functionalities
            user = username
            if user == "admin":
                display_menu2()
                choice_Other = input("Enter your choice: ")
                if choice_Other == "1":
                    #Get Selected Data for the Input Reg ID
                    vehicle = Vehicle(connection, '', '', '', '', '','','')
                    records = vehicle.retrieve_vehicle_info_All()
                    display_records(records)
                    display_menu4()
                    choice_Other = input("Enter your choice: ")
                    if choice_Other == "1":
                        car = Car('',1002,	'Ford',	'Car',	2018,	250,	1, reg_Number='NXT100',doors=5)
                        vehicle.add_record(connection,car)
                    elif choice_Other == "2":
                        reg_ID = input("Enter Vehicle Registration ID: ")
                        print(vehicle.retrieve_vehicle_info(reg_ID))
                        display_menu4()
                    else:
                        connection.close()
            else:
                display_menu3()
                choice_Other = input("Enter your choice: ")
                #pass
       # elif choice == "2":
        #    break
        else:
            print("Invalid choice. Please try again.")
        connection.close()

if __name__ == "__main__":
    main()