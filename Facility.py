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
        newfacilityname = self.facilityName
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
        print(facility_list)

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