"""
Defining Class Patient
Attributes: pid, name, disease, gender, age
Functions: formatPatientInfo, enterPatientInfo, readPatientsFile,
searchPatientById, displayPatientInfo, editPatientInfo, displayPatientsList,
writeListOfPatientsToFile, addPatientToFile
"""
class Patient:
    def __init__ (self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    """
    Format Patient Info
    Function: Formats patient information to be added to the file
    """
    def formatPatientInfo():
        return 0

    """
    Enter Patient Info
    Function: Asks the user to enter the patient info
    """
    def enterPatientInfo():
        return 0

    """
    Read Patients File
    Function: Reads fro the file patients.txt
    """
    def readPatientsFile():
        return 0

    """
    Search Patient By Id
    Function: Searches for a patient using their patient ID
    """
    def searchPatientById():
        return 0

    """
    Display Patient Info
    Function: Displays patient info
    """
    def displayPatientInfo():
        return 0

    """
    Edit Patient Info
    Function: Asks the user to edit patient information
    """
    def editPatientInfo():
        return 0

    """
    Display Patients List
    Function: Displays the list of patients 
    """
    def displayPatientsList():
        return 0

    """
    Write List of Patients To File
    Function: Writes a list of patients into the patients.txt file
    """
    def writeListOfPatientsToFile():
        return 0

    """
    Add Patient To File
    Function: Adds a new paatient to the file
    """
    def addPatientToFile():
        return 0