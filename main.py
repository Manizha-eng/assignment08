#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
file = open('cdInventory.txt', 'w')

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODO Add Code to the CD class
    cd_id = 1
    cd_title = "Songs"
    cd_artist = "Najlla"

obj_cd = CD()

# -- PROCESSING -- #
class FileIO:

    """Processes data to and from file:

        properties:

        methods:
            save_inventory(file_name, lst_Inventory): -> None
            load_inventory(file_name): -> (a list of CD objects)

    """
    # TODO Add code to process data from a file
    # TODO Add code to process data to a file

    def add_cd(self):
        again = "y"
        while again == "y":
            item = input("Input the CD name: ")
            lstOfCDObjects.append(item)
            again = input("Do you want to add another item [y/n]?")
        return lstOfCDObjects

    def save_inventory(file_name, lst_Inventory):
        for item in lstOfCDObjects:
            file.writelines(item + '\n')
        file.close()

    def load_inventory(file_name):
        for item in lstOfCDObjects:
            print(item)

obj_fileio = FileIO()

# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODO add docstring
    """
    Processes input and output
    """
    # TODO add code to show menu to user
    is_on = True
    while is_on:
        choice = input("Please choose an operation: (Add CD/Display Current Inventory/Save Inventory to file/exit) ")
        if choice == 'Add CD':
            obj_fileio.add_cd()
        elif choice == 'Display Current Inventory':
            obj_fileio.load_inventory()
        elif choice == 'Save Inventory to file':
            obj_fileio.save_inventory(lstOfCDObjects)
        else:
            is_on = False

    # TODO add code to display the current data on screen
    # TODO add code to get CD data from user


# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program

