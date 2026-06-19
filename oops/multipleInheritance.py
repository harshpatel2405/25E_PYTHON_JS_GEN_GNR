class Parent1:
    def __init__(self, a):
        self.a = a

    def displayParent1(self):
        print("(Parent1) A : ", self.a)


class Parent2:
    def __init__(self, b):
        self.b = b

    def displayParent2(self):
        print("(Parent2) B : ", self.b)


class Child(Parent1, Parent2):
    def __init__(self, a, b, c):
        Parent1.__init__(self, a)
        Parent2.__init__(self,b)
        self.c = c

    def displayChild(self):
        super().displayParent1()
        super().displayParent2()
        print("(Child)   C : ", self.c)

c = Child(10, 20, 30)
c.displayChild()


'''
Create a Python program for a Hospital Management System using Multiple Inheritance and Multilevel Inheritance.

Requirements:

1. Create a base class named Person
   - Attributes:
     - name
     - age
   - Method:
     - display_person_details()

2. Create a class named Doctor that inherits from Person
   - Attributes:
     - specialization
     - doctor_id
   - Method:
     - display_doctor_details()

3. Create another class named Patient that inherits from Person
   - Attributes:
     - disease
     - patient_id
   - Method:
     - display_patient_details()

4. Create a class named MedicalReport
   - Attributes:
     - report_number
     - test_result
   - Method:
     - display_report()

5. Create a class named HospitalRecord using Multiple Inheritance
   - Inherit from:
     - Doctor
     - Patient
     - MedicalReport
   - Method:
     - display_complete_record()

6. Create another class named EmergencyPatient using Multilevel Inheritance
   - EmergencyPatient should inherit from Patient
   - Add:
     - emergency_level
     - ambulance_number
   - Method:
     - display_emergency_details()

7. Functional Requirements:
   - Accept details from user
   - Display all hospital records properly
   - Show doctor details, patient details, and medical report together
   - Show emergency patient information separately

8. Concepts To Use:
   - Multiple Inheritance
   - Multilevel Inheritance
   - Constructors
   - super()
   - Method calling
   - Object creation

9. Additional Requirement:
   - Create separate objects for HospitalRecord and EmergencyPatient
   - Display outputs using menu-driven format

'''