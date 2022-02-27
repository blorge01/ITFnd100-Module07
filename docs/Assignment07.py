# -------------------------- #
# Filename Assignment07.py
# Description: Create a file that incorporates structured error handling and pickling
# Created by Brandon Lorge
# Created 2/26
# -------------------------- #

import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'    # File Name
lstCustomer = []
list_of_data = []

# Processing -------------------------------------- #
class PickleFile:
    def save_data_to_file(file_name, list_of_data):
        file = open(file_name, "ab")
        pickle.dump(list_of_data, file)
        file.close()

    def read_data_from_file(file_name):
        file = open(file_name, "rb")
        while True:
            try:
                list_of_data = pickle.load(file) # load() only loads one row of data.
                print(list_of_data)
            except Exception as e:
                break
        file.close()
        print("=" * 60)

# Presentation ------------------------------------ #
while True:
    print("""
    Menu of Options
    1. Enter Data
    2. View Data
    3. Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 - 3] - "))
    print()  # Adding extra line for breaks

    if strChoice == '1':         # Add to list and save to pickle file
        print("Enter Data")
        try:
            Id = input("Enter an Id: ")
            if Id.isnumeric() is False:
                raise Exception("Only integers are allowed.")
        except Exception as e:
            print("Only integers are allowed.")

        try:
            strName = str(input("Enter a Name: "))
            if strName.isnumeric() is True:
                raise Exception ("Only letters are allowed.")
        except Exception as e:
            print("Only letters are allowed.")
            print("There was a non-specific error!")
            print("Built-In Python error info: ")
            print(e, e.__str__, type(e), sep='\n')
        lstCustomer = [Id, strName]

        PickleFile.save_data_to_file(strFileName, lstCustomer)  # Save to file every time
        continue

    elif strChoice == '2':      # Read from pickle File
        print(PickleFile.read_data_from_file(strFileName))
        continue

    elif strChoice == '3':      # Exit
        print("Goodbye")
        break
