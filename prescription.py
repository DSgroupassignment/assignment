#Prescription class implementation
class Prescription:
    #initialization
    def __init__(self, prescription_id, medication, dosage):
        self.prescription_id = prescription_id    #pres id
        self.medication = medication              #medication
        self.dosage = dosage                      #dosage
        self.patient_id = None 
        
    #function to add patient id in prescription
    def set_patient_id(self, patient_id):
        self.patient_id = patient_id