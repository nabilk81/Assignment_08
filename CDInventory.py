#------------------------------------------#
# Title: CDInventory.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# NKnight, 2022-Mar-20, updating code to perform program operations
#------------------------------------------#

import pickle

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []
objFile = None
file_name = None
intID = ''
cd_title = ''
cd_artist = ''

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """

    def __init__(self, ID, title, artist):
        self.__cd_id = ID
        self.__cd_title = title
        self.__cd_artist = artist
        
    @property
    def cd_id(self):
        return self.__cd_id
    
    @cd_id.setter
    def cd_id(self, value):
        if type(value) == int:
            self.cd_id = value
        else:
            raise Exception('cd_id needs to be an integer')
            
    @property
    def cd_title(self):
        return self.__cd_title
    
    @cd_title.setter
    def cd_title(self, value):
        if type(value) == str:
            self.cd_title = value
        else:
            raise Exception('cd_id needs to be a CD Title in string format')
            
    @property
    def cd_artist(self):
        return self.__cd_title
    
    @cd_artist.setter
    def cd_artist(self, value):
        if type(value) == str:
            self.cd_artist = value
        else:
            raise Exception('cd_id needs to be a CD Artist in string format')
            
                
    def __str__(self):
        lst_Inventory = '{},{},{}'.format(self.__cd_id, self.__cd_title, self.__cd_artist)
        return lstOfCDObjects.append(lst_Inventory)       
        


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from binary file using the pickle module to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table, one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from

        Returns:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        """
        with open(file_name, 'r') as objFile:
            lst_Inventory = pickle.load(objFile)
        return lst_Inventory


    @staticmethod
    def save_inventory(lst_Inventory, file_name):
        """
        Function to save cd inventory from memory to binary file using the pickle module
        
        Args:
            file_name (string): name of file used to read the data from
            lst_Inventory (list of objects): 2D data structure that holds the data during runtime

        Returns
        -------
        None.

        """
        
        with open(file_name, 'wb') as objFile:
            pickle.dump(lst_Inventory, objFile)

        


# -- PRESENTATION (Input/Output) -- #
class IO:

    """Display program Menu, Inputs data from user, presents data back to user, add cd info from memeory:

    properties:

    methods:
        menu() to display menu to let user know choice options
        menu_choice() to get input for menu choice > returns choice
        show_inventory(lst_Inventory) to display current cd inventory in memory
        cd_input() to get user input for cd info to load into memory > return user list
        cd_input_proc() to append all added inventory to memory > 
        

    """

    @staticmethod
    def menu():
        print('Menu\n\n[i] Display Current Inventory\n[a] Add CD\n[s] Save Inventory to file')
        print('[l] load Inventory from file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        choice = ' '
        while choice not in ['i', 'a', 's', 'l', 'x']:
            choice = input('Which operation would you like to perform? [i, a, s, l, or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(lst_Inventory):
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lst_Inventory:
            print(row)
        print('======================================')

    @staticmethod
    def cd_input():
        cd_id = input('Enter ID: ').strip()
        cd_title = input('What is the CD\'s title? ').strip()
        cd_artist = input('What is the Artist\'s name? ').strip()
        try:
            intID = int(cd_id)
        except:
            print('cd_id that was entered was not a number')
        user_lst = [intID, cd_title, cd_artist]
        return user_lst
    @staticmethod
    def cd_input_proc():
        user_lst = IO.cd_input()
        #lst_Inventory = [intID, cd_title, cd_artist]
        lstOfCDObjects.append(user_lst)
        return lstOfCDObjects
 

# -- Main Body of Script -- #

while True:
    IO.menu()
    strChoice = IO.menu_choice()
    #print('Please choose an option from the menu: l, a, i, d, s or x')
    if strChoice == 'i':
        IO.show_inventory(lstOfCDObjects)
        #continue
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist

        # 3.3.2 Add item to the table
        #IO.cd_input()
        IO.cd_input_proc()
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        #continue
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileIO.save_inventory(lstOfCDObjects, strFileName)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        #continue 
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled: ')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lst_Inventory = FileIO.load_inventory(strFileName)
            IO.show_inventory(lst_Inventory)
    elif strChoice == 'x':
        break


