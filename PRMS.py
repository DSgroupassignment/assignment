from singlylinklist import SinglyLinkedList
from stackclass import Stack
from queueclass import Queue
from patient import Patient
from doctor import Doctor
from appointment import Appointment
from prescription import Prescription 

#Patient Record Management class implementation
class PatientRecordManagementSystem:
    #initialization
    def __init__(self):
        self.patients = SinglyLinkedList()    #create node of singly link list
        self.doctors = SinglyLinkedList()     #create node for doctors
        self.prescriptions_stack = Stack()    #stack call
        self.prescription_count = 0           #prescription count
        self.appointment_queue = Queue()      #Queue call
        self.doctor_queues = {}               #Dictionary for doctor
        self.init_doctors()     
    
    #add patient function
    def add_patient(self, patient_id, name, age, medical_history, current_condition, weight, gender, height):
        patient = Patient(patient_id, name, age, medical_history, current_condition, weight, gender, height)
        self.patients.insert(patient)
    
    #update existing patient 
    def update_patient(self, patient_id, **kwargs):
        current = self.patients.head
        patient_found = False
        #while loop here to traverse patient
        while current:
            if current.data.patient_id == patient_id:
                patient_found = True
                for key, value in kwargs.items():
                    setattr(current.data, key, value)
                break
            current = current.next
        print()
        if patient_found:
            print("Change successfully")
        else:
            print("Id can not found in the hospital")

    #delete patient from record
    def delete_patient(self, patient_id):
        current = self.patients.head
        prev = None
        patient_found = False
        #while loop here to traverse link list
        while current:
            #condition to get same patient id
            if current.data.patient_id == patient_id:
                patient_found = True
                if prev:
                    prev.next = current.next
                else:
                    self.patients.head = current.next
                break
            prev = current
            current = current.next
        print()
        if patient_found:
            print("Deleted Confirm")
        else:
            print("Id can not found in the hospital")
            
    #display patient of the hospital        
    def display_patients(self):
        print("Patients present in the hospital:")
        print()
        current = self.patients.head
        if current is None:
            print("There is no patient in the hospital")
            return
        #while loop here to print patients details
        while current:
            print("╔══════════════════════════════════════════════════════════╗")
            print("      Patient ID: " + str(current.data.patient_id))
            print("      Name: " + current.data.name)
            print("      Age: " + str(current.data.age))
            print("      Medical History: " + current.data.medical_history)
            print("      Current Condition: " + current.data.current_condition)
            print("      Weight: " + str(current.data.weight) + " kg")
            print("      Gender: " + current.data.gender)
            print("      Height: " + str(current.data.height) + " cm")
            print("╚══════════════════════════════════════════════════════════╝")
            current = current.next

    #initialize doctors of hospital 
    def init_doctors(self):
        #doctors list 
        doctors_data = [
            {"doctor_id": 1, "name": "Strawman", "specialty": "Heart"},
            {"doctor_id": 2, "name": "Rojar", "specialty": "Spine"},
            {"doctor_id": 3, "name": "Thomas", "specialty": "Surgeon"},
            {"doctor_id": 4, "name": "Tom", "specialty": "Brain"},
            {"doctor_id": 5, "name": "Jack", "specialty": "Eye"},
            {"doctor_id": 6, "name": "Elon", "specialty": "ENT"},
            {"doctor_id": 7, "name": "musk", "specialty": "skin"},
        ]
        #for loop here to print doctors info 
        for doctor_info in doctors_data:
            doctor = Doctor(**doctor_info)
            self.doctors.insert(doctor)
            #queue class to add doctors in queue
            self.doctor_queues[doctor.doctor_id] = Queue()
            
    #display doctors of hospital
    def display_doctors(self):
        print("Doctors present in the hospital:")
        print()
        current = self.doctors.head
        if current is None:
            print("There are no doctors in the hospital")
            return
        while current:
            print("╔═══════════════════════════════╗")
            print("      Doctor ID: " + str(current.data.doctor_id))
            print("      Name: " + current.data.name)
            print("      Specialty: " + current.data.specialty)
            print("╚═══════════════════════════════╝")
            current = current.next
    
    #schedult new appointment for patient 
    def schedule_appointment(self, patient_id, doctor_id, date_time):
        #find_patient function 
        patient = self.find_patient(patient_id)
        #find_doctor function
        doctor = self.find_doctor(int(doctor_id))
        if patient:
            print("Patient found:", patient.name)
        else:
            print("Error: Patient not found.")

        if doctor:
            print("Doctor found:", doctor.name)
        else:
            print("Error: Doctor not found.")

        if patient and doctor:
            #Appointment class to add patient details
            appointment = Appointment(patient, doctor, date_time)
            #doctor queue 
            doctor_queue = self.doctor_queues.get(int(doctor_id))
            if doctor_queue:
                doctor_queue.enqueue(appointment)
                print("Appointment scheduled successfully for Patient ID:", patient_id, "with Doctor ID:", doctor_id)
            else:
                print("Error: Doctor queue not found.")
        else:
            print("Error: Patient or Doctor not found.")
    #issue prescription to patients
    def issue_prescription(self, doctor_id, patient_id, medication, dosage):
        doctor_queue = self.doctor_queues.get(int(doctor_id))
        if doctor_queue:
            if not doctor_queue.is_empty():
                appointment = doctor_queue.dequeue()
                self.prescription_count += 1
                #Prescrption class to add details
                prescription = Prescription(self.prescription_count, medication, dosage)
                prescription.set_patient_id(patient_id)
                #push prescrption in stack
                self.prescriptions_stack.push(prescription)
                print("Prescription issued successfully for Patient ID:", patient_id)
            else:
                print("Error: Doctor's queue is empty.")
        else:
            print("Error: Doctor queue not found for Doctor ID:", doctor_id)

    #find patient function
    def find_patient(self, patient_id):
        current = self.patients.head
        while current:
            if current.data.patient_id == patient_id:
                return current.data
            current = current.next
        return None
    
    #find doctor function
    def find_doctor(self, doctor_id):
        current = self.doctors.head
        while current:
            if current.data.doctor_id == doctor_id:
                return current.data
            current = current.next
        return None

    #cancel the scheduled appointment 
    def cancel_appointment(self, patient_id, doctor_id):
        doctor_queue = self.doctor_queues.get(int(doctor_id))
        if doctor_queue:
            #list of sppointments
            appointments = []
            while not doctor_queue.is_empty():
                appointment = doctor_queue.dequeue()
                if appointment.patient.patient_id != patient_id:
                    #add appointments in appointments list
                    appointments.append(appointment)
            for appointment in appointments:
                doctor_queue.enqueue(appointment)
            print("Appointment canceled successfully for Patient ID:", patient_id, "with Doctor ID:", doctor_id)
        else:
            print("Error: Doctor queue not found for Doctor ID:", doctor_id)

    #view appointments present in appointments queue
    def view_appointments(self, doctor_id):
        doctor_queue = self.doctor_queues.get(doctor_id)
        if doctor_queue:
            print("Appointments for Doctor ID " + str(doctor_id) + ":")
            while not doctor_queue.is_empty():
                appointment = doctor_queue.dequeue()
                print("Patient ID:", appointment.patient.patient_id)
                print("Patient Name:", appointment.patient.name)
                print("Date and Time:", appointment.date_time)
                print()
        else:
            print("Error: Doctor queue not found.")
            
    #view prescription function 
    def view_prescriptions(self):
        print("Prescriptions issued by doctors:")
        #add prescription in stack
        current = self.prescriptions_stack.items.head
        #while loop to display prescription details
        while current:
            print("Prescription ID:", current.data.prescription_id)
            print("Medication:", current.data.medication)
            print("Dosage:", current.data.dosage)
            print()
            current = current.next

    #display patient summary of patient
    def display_patient_summary(self, patient_id):
        #find patient
        patient = self.find_patient(patient_id)
        if patient:
            print("Patient Summary:")
            print("Patient ID:", patient.patient_id)
            print("Name:", patient.name)
            print("Age:", patient.age)
            print("Medical History:", patient.medical_history)
            print("Current Condition:", patient.current_condition)
            print("Weight:", patient.weight, "kg")
            print("Gender:", patient.gender)
            print("Height:", patient.height, "cm")

            # Display prescriptions issued to the patient
            print("\nPrescriptions:")
            current = self.prescriptions_stack.items.head
            while current:
                if current.data.patient_id == patient_id:
                    print("Prescription ID:", current.data.prescription_id)
                    print("Medication:", current.data.medication)
                    print("Dosage:", current.data.dosage)
                    print()
                current = current.next
        else:
            print("Error: Patient not found.")
