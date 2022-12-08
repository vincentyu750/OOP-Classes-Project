"""
Defining Class Doctor
Properties: ID, Name, Specialization, Working Time, Qualification, Room Number
Functions: formatDrInfo, enterDrInfo, readDoctorsFile, searchDoctorById,
searchDoctorByName, displayDoctorInfo, editDoctorInfo, displayDoctorsList
"""
class Doctor:
    def __init__(self, id, name, specialization, working_time, qualification, room_number):
        self.id = id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    """
    Format Doctor Info
    Function: Formats each doctor's information (properties)
    #id_name_specialist_timing_qualification_roomNumber
    """
    def formatDrInfo():

        return 0


    """
    Enter Doctor Info
    Function: Asks the user to enter doctor properties 
    """
    def enterDrInfo():

        return 0


    """
    Read Doctors Info
    Function: Reads from "doctors.txt" file and fills the 
    doctor objects in a list
    """
    def readDoctorsFile():
        return 0


    """
    Search Doctor by ID
    Function: Searches whether the doctor is in the list of
    doctors/file using the doctor ID that the user enters
    """
    def searchDoctorById():
        return 0


    """
    Search Doctor By Name
    Function: Searches whether the doctor is in the list of
    doctors/file using the doctor name that the user enters
    """
    def searchDoctorByName(name):
        return 0

    """
    Display Doctor Info
    Function: Displays doctor information on different lines,
    as a list
    """
    def displayDoctorInfo():
        return 0

    """
    Edit Doctor Info
    Function: Asks the user to enter the ID of the doctor to
    change their information, and then the user can enter the 
    new doctor information
    """
    def editDoctorInfo():
        return 0

    """
    Display Doctors List
    Function: Displays all the doctors' information,
    read from the file as a report / table
    """
    def displayDoctorsList():
        return 0