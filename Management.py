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


