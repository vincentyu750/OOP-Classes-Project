"""
Defining Class Facility
Attributes: Facility name
Functions: addFacility, displayFacilities, writeListOfFacilitiesToFile
"""
class Facility: 
    def __init__(self, facility_name):
        self.facility_name = facility_name

    """
    Add Facility
    Function: Adds and writes the facility name to the file
    """
    def addFacility(self):
        newfacilityname = input("Enter Facility name:\n\n")
        facilityfile = open("facilities.txt", "a+")
        facilityfile.write("\n" + newfacilityname)
        facilityfile.close()

    """
    Make List of Facilities
    Function: Opens Text file to make a list of Facilities Objects
    """
    def makeListOfFacilities(self):
        facilityfile = open("facilities.txt", "r")
        content = facilityfile.read()
        facility_list = content.split("\n")
        facilityfile.close()
        return facility_list

    """
    Display Facilities
    Function: Displays the list of facilities
    """
    def displayFacilities(self):
        facility_list = self.makeListOfFacilities()
        for i in range(len(facility_list)):
            print(facility_list[i]+"\n")

    """
    Write List of Facilities to File
    Function: Writes the facilities list to facilities.txt
    """
    def writeListofFacilitiesToFile(self):
        content = self.makeListOfFacilities()
        facilities_list = ('\n'.join(content))
        print(facilities_list)
        faciltyfile = open("facilities.txt", "r+")
        faciltyfile.write(facilities_list)
        faciltyfile.close()

"""
Facility Menu
Function: Allows for the user to use all the facility functions
"""
def facilitiesMenu():

    my_facility = Facility("na")
    isRunning = True

    while isRunning:

        #list of facilities
        facility_list = my_facility.makeListOfFacilities

        facility_menu = int(input("Facilities Menu:\n1 - Display Facilities list\n2 - Add Facility\n3 - Back to the Main Menu\n\n"))

        if facility_menu == 1:
            my_facility.displayFacilities()
            print("Back to the previous Menu")
        if facility_menu == 2:
            my_facility.addFacility()
            print("Back to the previous Menu")
        if facility_menu == 3:
            isRunning = False
            print("Back to the previous Menu")