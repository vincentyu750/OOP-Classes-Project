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
    Function for ___repr___ for turning doctor object to string
    This function deals with formatting for display of doctors 
    """
    def __repr__(self):
        #ID then 4 spaces Name then 22 spaces Speciality then 15 spaces timing then 15 spaces then qualification then 15 spaces then room number
        return "{0:4} {1:22} {2:15} {3:15} {4:15} {5}".format(self.id, self.name, self.specialization, self.working_time, self.qualification, self.room_number)


    """
    Format Doctor Info
    Function: Formats each doctor's information (properties)
    #id_name_specialist_timing_qualification_roomNumber
    """
    def formatDrInfo(self):
        
        #formatting the doctor object into a string that is spaced by underscores
        formattedDoctor = "{0}_{1}_{2}_{3}_{4}_{5}".format(self.id, self.name, self.specialization, self.working_time, self.qualification, self.room_number)
        return formattedDoctor


"""
Write List of Doctors to File
Function: Writes the list of doctors to the doctors.txt file after formatting it correctly
"""
def writeListOfDoctorsToFile(input_list):
    #opens file and wipes its contents
    open('doctors.txt', 'w').close()

    #opens file for adding text
    f = open("doctors.txt", "a")

    #for all elements in the list 
    for i in range(1, len(input_list)):
        #formats the doctor object in the list
        string = input_list[i].formatDrInfo()
        #writing the formatted string into the file
        f.write(string)
        f.write("\n")
        
    #closes the file afterwards     
    f.close()


"""
Add Doctor To File
Function: Writes doctors to the doctors.txt file after formatting it correctly
"""
def addDrToFile(doctor):
    #opening the doctors.txt file for appending
    f = open("doctors.txt", "a")

    #formatting the doctor object into string
    string = doctor.formatDrInfo()

    #adding the doctor into the file
    f.write("\n" + string)

    #closing the file
    f.close()

"""
Enter Doctor Info
Function: Asks the user to enter doctor properties 
"""
def enterDrInfo():
    #Asking the user for the doctors information then creating a doctor object to add to the list
    id = input("Enter the doctor's ID:\n\n")
    name = input("Enter the doctor's name:\n\n")
    spec = input("Enter the doctor's speciality:\n\n")
    time = input("Enter the doctor's timing (e.g., 7am-10pm):\n\n")
    qual = input("Enter the doctor's qualification:\n\n")
    room = input("Enter the doctor's room number:\n\n")
    
    #creating a doctors object with the values asked
    d = Doctor(id,name,spec,time,qual,room)

    #returns the newely created doctor object
    return d

"""
Display Doctor Info
Function: Displays doctor information on different lines,
as a list
"""
def displayDoctorInfo(doctor):
    #printing the header Id Name Speciality Timing Qualification Room Number
    print("Id   Name                   Speciality      Timing          Qualification   Room Number\n")
    #printing doctor object
    print(doctor)

"""
Search Doctor by ID
Function: Searches whether the doctor is in the list of
doctors/file using the doctor ID that the user enters
"""
def searchDoctorById(list):
    #Asks the user for the ID
    selected_id = input("Please enter the doctor id:\n\n")
    
    #if the id is not there
    is_there = 0

    #Traverses through the list checking if the id is matched
    for i in range(0, len(list)):
        if str(list[i].id) == selected_id:

            #displays the selected doctor
            displayDoctorInfo(list[i])

            #changes is there to 1 signify that it is there
            is_there = 1

    if is_there == 0:
        print("Can't find the doctor with the same ID on the system")
            
"""
Search Doctor By Name
Function: Searches whether the doctor is in the list of
doctors/file using the doctor name that the user enters
"""
def searchDoctorByName(list):
    #Asks the user for the Name
    selected_name = input("Please enter the name of the doctor:\n\n")

    #if the id is not there
    is_there = 0

    #Traverses through the list checking if the name is matched
    for i in range(0, len(list)):
        if str(list[i].name) == selected_name:

            #displays the selected doctor
            displayDoctorInfo(list[i])

            #sets the is there to 1 signifiying there was something
            is_there = 1

    if is_there == 0:
        print("Can't find the doctor with the same name on the system")

"""
Edit Doctor Info
Function: Asks the user to enter the ID of the doctor to
change their information, and then the user can enter the 
new doctor information
"""
def editDoctorInfo(list):
    
    #Asks the user for the ID
    selected_id = input("Please enter the id of the doctor that you want to edit their information:\n\n")
    
    #if the id is not there
    is_there = 0

    #Traverses through the list checking if the id is matched
    for i in range(0, len(list)):
        if str(list[i].id) == selected_id:

            #changes is there to 1 signify that it is there
            is_there = 1

            #Asking the user for the doctors information then creating a doctor object to add to the list
            id = selected_id
            name = input("Enter the doctor's name:\n\n")
            spec = input("Enter the doctor's speciality:\n\n")
            time = input("Enter the doctor's timing (e.g., 7am-10pm):\n\n")
            qual = input("Enter the doctor's qualification:\n\n")
            room = input("Enter the doctor's room number:\n\n")
            
            #creating a doctors object with the values asked
            inputDoctor = Doctor(id,name,spec,time,qual,room)

            #replaces the current selected with the new updated doctor
            list[i] = inputDoctor

    if is_there == 0:
        print("Can't find the doctor with the same name on the system")
    
"""
Display Doctors List
Function: Displays all the doctors' information,
read from the file as a report / table
"""
def displayDoctorsList():
    #creating a list of doctors from reading the doctors.txt file
    doctorList = readDoctorsFile()

    #printing the header Id Name Speciality Timing Qualification Room Number
    print("Id   Name                   Speciality      Timing          Qualification   Room Number\n")
    #reading each doctor in the list of doctors from the text file
    for i in range(1, len(doctorList)):
        #pringint out the doctors object the formatting is done in the __repr__ function
        print(doctorList[i])
        print("")

"""
Read Doctors Info
Function: Reads from "doctors.txt" file and fills the 
doctor objects in a list
"""
def readDoctorsFile():
    #creating a list of doctor objects
    doctorList = []

    #Reading the doctor.txt file and appending the data into a list of doctor objects
    with open('doctors.txt') as f:

        #read the lines of the file
        lines = f.readlines()

        #runs through all the lines
        for line in lines:
            #spliting t he line of text by underscore 
            row = line.split('_')
            
            #assigning each variable by the split string
            id, name, specilist, timing, qualification, roomNumber = [i.strip() for i in row]
            
            #creating doctor object based on split text file
            doctor = Doctor(id, name, specilist, timing, qualification, roomNumber)
            
            #adding the newly created doctor objects into a list
            doctorList.append(doctor)

    #closing the file
    f.close()

    return doctorList     

#Testing the doctors case
def doctorMenu():

    #creating a list from the file
    listOfDoctors = readDoctorsFile()

    #start of the menu selection
    doctorMenuSelection = True
    while doctorMenuSelection:

        #Doctor menu prompt
        choice = int(input("Doctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor into\n6 - Back to the Main Menu\n\n"))

        #menu selection
        if choice == 1: 
            displayDoctorsList()

        if choice == 2:
            searchDoctorById(listOfDoctors)

        if choice == 3:
            searchDoctorByName(listOfDoctors)

        if choice == 4:
            inputDoctor = enterDrInfo()
            addDrToFile(inputDoctor)

        if choice == 5:
            editDoctorInfo(listOfDoctors)
            writeListOfDoctorsToFile(listOfDoctors)

        if choice == 6:
            doctorMenuSelection = False

"""
Expected output (tested)
Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

1
Id   Name                   Speciality      Timing          Qualification   Room Number

21   Dr.Gody                ENT             5am-11aM        MBBS,MD         17
       
32   Dr.Vikram              Physician       10pm-3am        MBBS,MD         45
       
17   Dr.Amy                 Surgeon         8pm-2am         BDM             8
        
33   Dr.David               Artho           10am-4pm        MBBS,MS         40
       
123  Dr. Ross               Headackes       8pm-10am        MST             102
      
66   Dr. Mike               Heart           9am-5pm         MS              2         

Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

2

 Enter the doctor Id: 

66
Id   Name                   Speciality      Timing          Qualification   Room Number

66   Dr. Mike               Heart           9am-5pm         MS              2         

Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

3

 Enter the doctor name: 

Dr.David
Id   Name                   Speciality      Timing          Qualification   Room Number

33   Dr.David               Artho           10am-4pm        MBBS,MS         40
       

Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

2

 Enter the doctor Id: 

20
Can't find the doctor with the same ID on the system

Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

3

 Enter the doctor name: 

Dr. Tom
Can't find the doctor with the same name on the system

Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

4
Enter the doctor’s ID:

62
Enter the doctor’s name:

Dr. Smith
Enter the doctor’s specility:

Heart
Enter the doctor’s timing (e.g., 7am-10pm):

6am-11am
Enter the doctor’s qualification:

PHD
Enter the doctor’s room number:

12

Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

5
Please enter the id of the doctor that you want to edit their information: 

66

Enter new Name: 

Dr. Mike kale

Enter new Specilist in:

Heart

Enter new Timing: 

9am-3pm

Enter new Qualification: 

MS

Enter new Room number: 

2

Back to the prevoius Menu

Doctors Menu:
1 - Display Doctors list
2 - Search for doctor by ID
3 - Search for doctor by name
4 - Add doctor
5 - Edit doctor info
6 - Back to the Main Menu

6
"""