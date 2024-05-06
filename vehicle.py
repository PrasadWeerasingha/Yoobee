
import sqlite3
class Vehicle:
    def __init__(self,connection, id, brand, type, makeYear, price_per_Week,available,reg_Number):
        self.id = id
        self.brand = brand
        self.type = type
        self.makeYear = makeYear
        self.price_per_Week = price_per_Week
        self.available = available
        self.reg_Number = reg_Number
        self.connection = connection

    def get_info(self):
        return f"id: {self.id}, brand: {self.brand}, type: {self.type}, makeYear: {self.makeYear},price_per_Week: {self.price_per_Week},available: {self.available},reg_Number: {self.reg_Number}"

    #Function for get all Vehicle Records
    #@staticmethod
    def retrieve_vehicle_info_All(self):
        try:
            self.connection.cursor.execute("SELECT * FROM vehicles")
            records = self.connection.cursor.fetchall()
            return records
        except sqlite3.Error as e:
            print(f"Error retrieving records: {e}")
            return None

    # Create Function to call selected Vehicle Info
    def retrieve_vehicle_info(self,reg_id):
        try:
            self.connection.cursor.execute("SELECT * FROM vehicles WHERE reg_Number = ?", (reg_id,))
            vehicle_data = self.connection.cursor.fetchone()
            if vehicle_data:
                id, brand, type, makeYear, doors, price_Per_Week, available, reg_Number, bed_length = vehicle_data
                if type == 'Car':
                    return Car(id, brand, type, makeYear, price_Per_Week, available, reg_Number, doors).get_info()
                elif type == 'Dump_Truck':
                    return Dump_Truck('',id, brand, type, makeYear, price_Per_Week, available, reg_Number,
                                      bed_length,).get_info()

            else:
                return "Vehicle not found."
        except sqlite3.Error as e:
            print(f"Error retrieving vehicle info: {e}")
            return "Error occurred while retrieving vehicle info."

    ##@staticmethod
    def add_record(self, connection, vehicle):
        try:
            #self.connection.connect()
            cursor = self.connection.cursor
            if isinstance(vehicle, Car):
                cursor.execute("INSERT INTO vehicles (id,brand,type,makeYear,doors,price_Per_Week,avalability,reg_Number) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                               (vehicle.id, vehicle.brand, "Car", vehicle.makeYear,vehicle.doors,vehicle.price_per_Week,vehicle.available,vehicle.reg_Number))
            elif isinstance(vehicle, Dump_Truck):
                self.connection.cursor.execute("INSERT INTO vehicles (id,brand,type,makeYear,price_Per_Week,avalability,reg_Number,bed_length) VALUES (?, ?, ?, ?, ?,?, ?, ?)",
                               (vehicle.id, vehicle.brand, "Dump_Truck", vehicle.makeYear,vehicle.price_per_Week,vehicle.available,vehicle.reg_Number,vehicle.bed_length))
                conn.co
            print("Record added successfully.")
        except sqlite3.Error as e:
            print(f"Error adding record: {e}")

#Sub Class Car
class Car(Vehicle):
    def __init__(self, connection,id, brand, type, makeYear, price_per_Week,available,reg_Number,doors):
        super().__init__(connection,id, brand, type, makeYear, price_per_Week,available,reg_Number)
        self.doors = doors

    def get_info(self):
        return f"{super().get_info()}, Doors: {self.doors}"

#Sub Class Dump_Truck
class Dump_Truck(Vehicle):
    def __init__(self,connection,id, brand, type, makeYear, price_per_Week,available,reg_Number,bed_length):
        super().__init__(connection,id, brand, type, makeYear, price_per_Week,available,reg_Number)
        self.bed_length = bed_length

    def get_info(self):
        return f"{super().get_info()}, bed_length: {self.bed_length}"

