#Importing the classes from the other files
#This will act like a main file where everything will happen
from Doctor import *
from Facility import *
from Laboratory import *
from Patient import *

main_menu = True
while main_menu == True:

    main_menu_selection = int(input("""
Welcome to Alberta Hospital (AH) Management system\n
Select from the following options, or select 0 to stop:
1 -\tDoctors
2 -\tFacilities
3 -\tLaboratories
4 -\tPatients
\n
"""))
    #if doctors is selected
    if main_menu_selection == 1:
        doctorMenu()

    #if facilities is selected
    if main_menu_selection == 2:
        facilitiesMenu()

    #if Laboratories is selected
    if main_menu_selection == 3:
        laboratoriesMenu()

    #if patient is selected
    if main_menu_selection == 4:
        patientMenu()

    if main_menu_selection == 0: 
        main_menu = False

    else:
        continue


"""
Notes:
Management will just call upon the respective menus
from the other class functions. 

Expected Output:
Welcome to Alberta Hospital (AH) Managment system 
Select from the following options, or select 0 to stop: 
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients 

1

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

Welcome to Alberta Hospital (AH) Managment system 
Select from the following options, or select 0 to stop: 
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients
2
Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu

1
The Hospital  Facilities are:

Ambulance

Admissions

Canteen

Emergency

Back to the prevoius Menu
Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu

2
Enter Facility name:

Covid Care

Back to the prevoius Menu
Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu

1
The Hospital  Facilities are:

Ambulance

Admissions

Canteen

Emergency

Covid Care

Back to the prevoius Menu
Facilities Menu:
1 - Display Facilities list
2 - Add Facility
3 - Back to the Main Menu

3

Welcome to Alberta Hospital (AH) Managment system 
Select from the following options, or select 0 to stop: 
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients 

3
Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu

1
Lab             Cost
          
Lab1            800
           
Lab2            1200
          
Lab3            500
           
Lab4            50             

Back to the prevoius Menu
Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu

2
Enter Laboratory facility:

Lab5
Enter Laboratory cost:

250

Back to the prevoius Menu
Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu

1
Lab             Cost
          
Lab1            800
           
Lab2            1200
          
Lab3            500
           
Lab4            50
            
Lab5            250            

Back to the prevoius Menu
Laboratories Menu:
1 - Display laboratories list
2 - Add laboratory
3 - Back to the Main Menu

3
Welcome to Alberta Hospital (AH) Managment system 
Select from the following options, or select 0 to stop: 
1 - 	Doctors
2 - 	Facilities
3 - 	Laboratories
4 - 	Patients 

4
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

1
ID   Name                   Disease         Gender          Age
           
12   Pankaj                 Cancer          Male            30
            
13   Janina                 Cold            Female          23
            
14   Alonna                 Malaria         Female          45
            
15   Ravi                   Diabetes        Male            65             

Back to the prevoius Menu
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

2

 Enter the Patient Id: 

16
Can't find the Patient with the same id on the system

Back to the prevoius Menu
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

2

 Enter the Patient Id: 

15
15   Ravi                   Diabetes        Male            65             

Back to the prevoius Menu
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

3
Enter Patient id:

16
Enter Patient name:

Mary
Enter Patient disease:

Cancer
Enter Patient gender:

Female
Enter Patient age:

55

Back to the prevoius Menu
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

4
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

4
Please enter the id of the Patient that you want to edit their information: 

13

Enter new Name: 

Janina

Enter new disease:

Cold&Flue

Enter new gender: 

Female

Enter new age: 

23

Back to the prevoius Menu
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

1
ID   Name                   Disease         Gender          Age
           
12   Pankaj                 Cancer          Male            30
            
13   Janina                 Cold&Flue       Female          23             
14   Alonna                 Malaria         Female          45
            
15   Ravi                   Diabetes        Male            65
            

Back to the prevoius Menu
Patients Menu:
1 - Display patients list
2 - Search for patient by ID
3 - Add patient
4 - Edit patient info
5 - Back to the Main Menu

5
"""