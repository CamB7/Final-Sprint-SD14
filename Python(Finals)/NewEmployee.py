# Description: HAB Taxi Services New Employee
# Author: Cameron Boyer
# Date: April 7th, 2025

# Import required libraries.
import FormatValues as FV
import datetime
import sys
import os

# Define function.

def NewEmployee():
    # Function will accept a new employee's information and write it to the Employee.dat file.
    # Function will also return the new employee's ID number.
    while True:
        # Clear the screen.
        os.system('cls' if os.name == 'nt' else 'clear')
        # Gather user inputs.
        print()
        print(" Enter New Employee Information")
        print(" -------------------------------")
        print()
        DriverName = input(" Enter the driver's name: ").title()
        DriverStAddress = input(" Enter the driver's street address: ").title()
        DriverCity = input(" Enter the driver's city: ").title()
        DriverProv = input(" Enter the driver's province: ").upper()
        DriverPostCode = input(" Enter the driver's postal code: ").upper()
        DriverPhone = input(" Enter the driver's phone number (10 digits): ")
        if  len(DriverPhone) != 10:
            print()
            print("  Invalid phone number - Please enter a 10 digit number.")
            print()
            DriverPhone = input(" Enter the driver's phone number (10 digits): ")
        else:
            DriverPhone = DriverPhone.strip()
            DriverPhone = "(" + DriverPhone[:3] + ")" + DriverPhone[3:6] + "-" + DriverPhone[6:]
        DriverLicense = input(" Enter the driver's license number: ").upper()
        LicenseExp = input(" Enter the driver's license expiration date (yyyy-mm-dd): ")
        try:
            LicenseExp = datetime.datetime.strptime(LicenseExp, "%Y-%m-%d").date()
        except ValueError:
            print()
            print("  Invalid date - Please enter a valid date in the format yyyy-mm-dd.")
            print()
            LicenseExp = input(" Enter the driver's license expiration date (yyyy-mm-dd): ")
        InsurPolCompany = input(" Enter the driver's insurance policy company: ").title()
        InsurPolNum = input(" Enter the driver's insurance policy number: ").upper()
        OwnCar = input(" Does the driver own their own car? (Y/N): ").upper()
        if OwnCar == "":
            print()
            print("  Invalid input - Please enter Y or N.")
            print()
            OwnCar = input(" Does the driver own their own car? (Y/N): ").upper()
        elif OwnCar == "Y":
            OwnCar = True
        else:
            OwnCar = False
        BalDue = 0.00

        # Open the Employee.dat file for writing.
        f = open("Employee.dat", "a")
        # Write the new employee's information to the file.
        f.write(f"{DriverName},{DriverStAddress},{DriverCity},{DriverProv},{DriverPostCode},")
        f.write(f"{DriverPhone},{DriverLicense},{LicenseExp},{InsurPolCompany},{InsurPolNum},")
        f.write(f"{OwnCar},{BalDue}\n")
        # Close the file.
        f.close()

        # Tell the user that the new employee has been added.
        print()
        print(" New employee added successfully.")
        print()
        
        # Get new employee's ID number from the second line in Defaults.dat file.
        
        # Open Defaults.dat to read the current employee ID.
        with open("Defaults.dat", "r") as Defaults:
            Lines = Defaults.readlines()
            NxtEmpID = int(Lines[1].strip())  # Read the second line and convert to integer

        # Print the new employee's ID.
        print(f"   New Employee ID: {NxtEmpID}")

        # Increment the employee ID in Defaults.dat.
        with open("Defaults.dat", "w") as defaults_file:
            Lines[1] = str(NxtEmpID + 1) + "\n"  # Increment and convert back to string
            defaults_file.writelines(Lines)  # Write the updated ID back to the file

        # Ask the user if they want to add another employee.
        print()
        AddAnother = input(" Do you want to add another employee? (Y/N): ").upper()
        if AddAnother == "":
            print()
            print("  Invalid input - Please enter Y or N.")
            print()
            AddAnother = input(" Do you want to add another employee? (Y/N): ").upper()
        elif AddAnother == "Y":
            continue
        else:
            print()
            print("  Exiting the New Employee function")
            print("   and returning to the main menu.")
            break
            
        


        