#patient menu function
def patient_dealing_menu(prms):
    while True:
        print()
        print("╔═════════════════════════════╗")
        print("      Patient Dealing Menu")
        print("      a. Add Patient")
        print("      b. Edit Patient")
        print("      c. Delete Patient")
        print("      d. View Patients")
        print("      e. Back")
        print("╚═════════════════════════════╝")
        print()
        option = input("Give your option: ")
        print()
        if option == "a":
            #prompt user to add details 
            patient_id = input("Give patient ID: ")
            name = input("Give name: ")
            age = input("Give age: ")
            medical_history = input("Give medical history: ")
            current_condition = input("Give current condition: ")
            weight = input("Give weight (in kg): ")
            gender = input("Give gender: ")
            height = input("Give height (in cm): ")
            #add details in patient class
            prms.add_patient(patient_id, name, age, medical_history, current_condition, weight, gender, height)
            print("Added successfully")
        elif option == "b":
            patient_id = input("Give patient ID to update: ")
            attribute = input("Give attribute to update (name/age/medical_history/current_condition/weight/gender/height): ")
            new_value = input("Give new value: ")
            #update patient
            prms.update_patient(patient_id, **{attribute: new_value})
        elif option == "c":
            patient_id = input("Give patient ID to remove: ")
            #delete patient 
            prms.delete_patient(patient_id)
        elif option == "d":
            #display patient
            prms.display_patients()
        elif option == "e":
            break
        else:
            print("Please try again select upon mention options")

#doctor menu function
def doctor_dealing_menu(prms):
    while True:
        print()
        print("╔══════════════════════════════╗")
        print("      Doctor Dealing Menu")
        print("      a. View Doctors")
        print("      b. Schedule Appointment")
        print("      c. Cancel Appointment")
        print("      d. View Appointments")
        print("      e. Back")
        print("╚══════════════════════════════╝")
        print()
        option = input("Give your option: ")
        print()
        if option == "a":
            #display doctors
            prms.display_doctors()
        elif option == "b":
            patient_id = input("Give patient ID: ")
            doctor_id = input("Give doctor ID: ")
            date_time = input("Give date and time (YYYY-MM-DD HH:MM): ")
            #schedule appointment
            prms.schedule_appointment(patient_id, doctor_id, date_time)
        elif option == "c":
            patient_id = input("Give patient ID: ")
            doctor_id = input("Give doctor ID: ")
            #cancel appointment
            prms.cancel_appointment(patient_id, doctor_id)
        elif option == "d":
            doctor_id = input("Give doctor ID: ")
            #view appointment
            prms.view_appointments(int(doctor_id))
        elif option == "e":
            break
        else:
            print("Please try again select upon mention options")

#prescription menu function
def doctor_prescription_menu(prms):
    while True:
        print()
        print("╔══════════════════════════════╗")
        print("    Doctor Prescription Menu")
        print("    a. Issue Prescription")
        print("    b. View Prescriptions")
        print("    c. Back")
        print("╚══════════════════════════════╝")
        print()
        option = input("Give your option: ")
        print()
        if option == "a":
            doctor_id = input("Give doctor ID: ")
            patient_id = input("Give patient ID: ")
            medication = input("Give medication: ")
            dosage = input("Give dosage: ")
            #issue prescription
            prms.issue_prescription(doctor_id, patient_id, medication, dosage)
        elif option == "b":
            #view prescription function
            prms.view_prescriptions()
        elif option == "c":
            break
        else:
            print("Please try again select upon mention options")
              
#patient summary function
def patient_summary_menu(prms):
    while True:
        print()
        print("╔══════════════════════════════╗")
        print("         Summary Menu")
        print("         a. Summary Of Patient")
        print("         b. Back")
        print("╚══════════════════════════════╝")
        print()
        option = input("Give your option: ")
        print()
        if option == "a":
            patient_id = input("Give patient ID: ")
            #display summary
            prms.display_patient_summary(patient_id)
        elif option == "b":
            break
        else:
            print("Please try again select upon mention options")
