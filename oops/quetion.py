class person :
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def display_person_details(self):
        print("Name : ", self.name)
        print("Age : ", self.age)

class doctor(person) :
    def __init__(self, name, age, specialization, doctor_id,userType):
        person.__init__(self,name, age)
        self.specialization = specialization
        self.doctor_id = doctor_id
        self.userType = userType
    def display_doctor_details(self):
        super().display_person_details()
        print("User : " ,self.userType)
        print("Specialization : " , self.specialization)
        print("Doctor ID : " , self.doctor_id)

class patient(person):
    def __init__(self, name, age, disease, patient_id,userType):
        super().__init__(name, age)
        self.disease = disease
        self.patient_id = patient_id
        self.userType = userType

    def display_patient_details(self):
        super().display_person_details()
        print("User : " ,self.userType)
        print("Disease : ", self.disease)
        print("Patient ID : ", self.patient_id)

class medicalReport:
    def __init__(self,report_number,test_result):
        self.report_number = report_number
        self.test_result = test_result

    def display_report(self):
        print("Report Number : " , self.report_number)
        print("Test Result : ", self.test_result)

class HospitalRecord(doctor,patient,medicalReport):
    def __init__(self, name, age, specialization, doctor_id, disease, patient_id, report_number, test_result,user):
        doctor.__init__(self,name, age, specialization, doctor_id,user)
        patient.__init__(self,name, age, disease, patient_id,user)
        medicalReport.__init__(self,report_number, test_result)

    def display_complete_record(self):
        self.display_doctor_details()
        self.display_patient_details()
        self.display_report()

class EmergencyPatient(patient):
    def __init__(self, name, age, disease, patient_id,emergency_level,ambulance_number,user):
        super().__init__(name, age, disease, patient_id,user)
        self.emergency_level = emergency_level
        self.ambulance_number = ambulance_number
    def display_emergency_details(self):
        super().display_patient_details()
        print("Emergency Level : " , self.emergency_level)
        print("Ambulance Number : " , self.ambulance_number)


h = HospitalRecord("john hopkins" , 23 , "MD" ,104 , "flu" , 202 , 101 , "positive","patient")
h.display_complete_record()