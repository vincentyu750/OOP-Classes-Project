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

    """
    Add Lab to File
    Function: Adds and writes the lab name to the file in the format
    of the data that is in the file
    """
    def addlabtofile(self):
        newlabname = input("What is the name of the lab that you would like to add?")
        newlabcost = input("what is the cost of this new lab?")
        labfile = open("laboratories.txt", "a+")
        labfile.write("\n" + newlabname + "_" + newlabcost)
        labfile.close()

    """
    Write List of Labs to File
    Function: Writes the list of labs into the files
    laboratories.txt
    """
    def writelistoflabstofile(self):
        content = labhere.readlaboratoriesfile()
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
        labs_list = labhere.readlaboratoriesfile()
        print(labs_list)

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
        newlabname = input("What is the name of the lab that you would like to add?")
        newlabcost = input("what is the cost of this new lab?")
        newlab = labhere.formatlabinfo(newlabname, newlabcost)
        list = labhere.readlaboratoriesfile()
        list.append(newlab)

    """
    Read Laboratories File
    Function: Read the laboratories.txt file and fills its contents
    in a list of Laboratory objects
    """
    def readlaboratoriesfile(self):
        labfile = open("laboratories.txt", "r")
        content = labfile.read()
        labs_list = content.split("\n")
        labfile.close()
        return labs_lis
