from PRMS import PatientRecordManagementSystem
from menu import doctor_dealing_menu, doctor_prescription_menu, patient_dealing_menu , patient_summary_menu

#main function
def main():
    #Patient record system class call
    prms = PatientRecordManagementSystem()
    #initialize doctors 
    prms.init_doctors()
    while True:
        print()
        print("╔═══════════════════════════════════════════╗")
        print("    Patient Record Management System Menu ")
        print("    1. Patient Dealing")
        print("    2. Doctor Dealing")
        print("    3. Doctor Prescription")
        print("    4. Summary")
        print("    5. Exit")
        print("╚═══════════════════════════════════════════╝")
        print()
        option = input("Give your option: ")
        print()
        if option == "1":
            patient_dealing_menu(prms)
        elif option == "2":
            doctor_dealing_menu(prms)
        elif option == "3":
            doctor_prescription_menu(prms)
        elif option == "4":
            patient_summary_menu(prms)
        elif option == "5":
            print("Exiting...")
            break
        else:
            print("Please try again select upon mention options")

#call menu function
if __name__ == "__main__":
    main()