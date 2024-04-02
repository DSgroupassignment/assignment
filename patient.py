#Patient class implmentation
class Patient:
    #initialization
    def __init__(self, patient_id, name, age, medical_history, current_condition, weight, gender, height):
        self.patient_id = patient_id     #id
        self.name = name                 #name
        self.age = age                   #age
        self.medical_history = medical_history    #history
        self.current_condition = current_condition   #condition
        self.weight = weight    #weight
        self.gender = gender    #gender
        self.height = height    #height