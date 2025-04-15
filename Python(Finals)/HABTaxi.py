# Description: HAB Taxi Services Menu
# Author(s): Cameron Boyer, Landon Lewis, and Brandon Maloney
# Date(s): April 7th, 2025 -


# Define required libraries.
import FormatValues as FV
import datetime
import sys
import os


# Define program constants.
 # See Defaults.dat for default values.


# Define program funtions.
import NewEmployee as NE

def MainMenu():
    print()
    print("          HAB Taxi Services")
    print("       Company Services System")
    print()
    print("  1. Enter a New Employee (driver).")
    print("  2. Enter Company Revenues.")
    print("  3. Enter Company Expenses.")
    print("  4. Track Car Rentals.")
    print("  5. Record Employee Payment.")
    print("  6. Print Company Profit Listing.")
    print("  7. Print Driver Financial Listing.")
    print("  8. Quit Program.")
    print()
    

# Main program starts here.
while True:
    # Clear the screen.
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display the main menu.
    MainMenu()

    # Gather user inputs.
    UserChoice = int(input("         Enter choice (1-8): "))
    if UserChoice < 1 or UserChoice > 8:
        print()
        print("Invalid choice - Please enter a number between 1 and 8.")
        print()
           
    elif UserChoice == 1:
        # Call the NewEmployee function to add a new employee.
        NE.NewEmployee()
        '''
        elif UserChoice == 2:
        elif UserChoice == 3:
        elif UserChoice == 4:
        elif UserChoice == 5:
        elif UserChoice == 6:
        elif UserChoice == 7:
        '''
    else:
        # Exit the program.
        print("Exiting the program.")
        break
           
    



    # Perform required calculations.



    # Display results



    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.