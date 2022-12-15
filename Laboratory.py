"""
Defining Class Laboratory
Attributes: Lab Name, Cost
Functions: addLabToFile, writeListOfLabsToFile, displayLabsList,
formatLabInfo, enterLaboratoryInfo, readLaboratoriesFile
"""
class Laboratory:
    def __init__(self, lab_name, cost):
        self.lab_name = lab_name
        self.cost = cost

    def __repr__(self):
        #ID then 4 spaces Name then 22 spaces Speciality then 15 spaces timing then 15 spaces then qualification then 15 spaces then room number
        return "{0:4} {1:22}".format(self.lab_name, self.cost)

    """
    Add Lab to File
    Function: Adds and writes the lab name to the file in the format
    of the data that is in the file
    """
    def addlabtofile(self):
        newlabname = input("What is the name of the lab that you would like to add?\n")
        newlabcost = input("what is the cost of this new lab?\n")
        labfile = open("laboratories.txt", "a+")
        labfile.write("\n" + newlabname + "_" + newlabcost)
        labfile.close()

    """
    Write List of Labs to File
    Function: Writes the list of labs into the files
    laboratories.txt
    """
    def writelistoflabstofile(self):
        content = self.readlaboratoriesfile()
        labs_list = ('\n'.join(content))
        print(labs_list)
        labfile = open("laboratories.txt", "r+")
        labfile.write(labs_list)
        labfile.close()
        
    """
    Displays Labs List
    Function: Displays the list of laboratories
    """
    def displaylabslist(self):
        labs_list = self.readlaboratoriesfile()
        total_rows = len(labs_list)
        current_row = 1
        print(f'{"Lab":<10}' f'{"Cost":<15}')
        while current_row < total_rows:
            print (f'{labs_list[current_row][0]:<10}' + f'{labs_list[current_row][1]:<15}')
            print ("\n")
            current_row += 1

    """
    Format Lab Info
    Function: Formats the laboratory object similar to the 
    laboratories.txt file
    """
    def formatlabinfo(self, labname, cost):
        specificlab = (labname + "_" + cost)
        return specificlab

    """
    Emter Laboratory Info
    Function: Asks the user to enter lab name and cost 
    and forms a laboratory object
    """
    def enterlaboratoryinfo(self):
        newlabname = input("What is the name of the lab that you would like to add?\n\n")
        newlabcost = input("what is the cost of this new lab?\n\n")
        newlab = self.formatlabinfo(newlabname, newlabcost)
        list = self.readlaboratoriesfile()
        list.append(newlab)

    """
    Read Laboratories File
    Function: Read the laboratories.txt file and fills its contents
    in a list of Laboratory objects
    """
    def readlaboratoriesfile(self):
        labfile = open("laboratories.txt", "r")
        labs_list = []
        for each_line in labfile:
            labs_list.append(each_line.rstrip().split('_'))
        labfile.close()
        return labs_list

"""
Laboratory Menu
Function: Allows for the user to use all the laboratory functions
"""
def labMenu():

    my_lab = Laboratory("na",0)
    isRunning = True

    while isRunning:

        #list of Labs
        lab_list = my_lab.readlaboratoriesfile()

        lab_menu = int(input("Laboratories Menu:\n1 - Display laboratories list\n2 - Add laboratory\n3 - Back to the Main Menu\n\n"))

        if lab_menu == 1:
            my_lab.displaylabslist()
            print("Back to the previous Menu")
        if lab_menu == 2:
            my_lab.addlabtofile()
            print("Back to the previous Menu")
        if lab_menu == 3:
            isRunning = False
            print("Back to the previous Menu")