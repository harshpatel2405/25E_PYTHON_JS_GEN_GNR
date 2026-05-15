'''
Create class Patient:

patient name
disease

Create class IndoorPatient:

room number
days admitted

Calculate hospital bill.

Formula:
Bill=Days * Charge Per Day
'''


class Patient:
    def __init__(self, patientName, disease):
        self.patientName = patientName
        self.disease = disease

    def displayPatient(self):
        print("Patient Name :",self.patientName)
        print("Disease :",self.disease)


class IndoorPatient(Patient):
    ChargePerDay = 450

    def __init__(self, rn, da, patientName, disease):
        super().__init__(patientName, disease)
        self.roomNumber = rn
        self.daysAdmitted = da

    def calculateHospitalBill(self):
        Bill = self. daysAdmitted * self.ChargePerDay
        print("Total Bill : ",Bill)

    def displayIndoorPatient(self):
        self.displayPatient()
        print("Room Number :",self.roomNumber)
        print("Days Admitted :",self.daysAdmitted)
        self.calculateHospitalBill()

I = IndoorPatient(101,5,"Jacob","Chicken Pox")
I.displayIndoorPatient()
