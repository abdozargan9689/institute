from datetime import date
from clinic_project.database.database import SessionLocal, init_db
from clinic_project.models import Patient, LabTest, Treatment
from clinic_project import crud

def main():
    init_db()
    db = SessionLocal()

    while True:
        print("\n--- Clinic Management System ---")
        print("1. Add Patient")
        print("2. View Patient")
        print("3. Add Lab Test")
        print("4. Add Treatment")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter patient name: ")
            birth_date_str = input("Enter birth date (YYYY-MM-DD): ")
            birth_date = date.fromisoformat(birth_date_str)
            patient = Patient(name=name, birth_date=birth_date)
            crud.create_patient(db, patient)
            print("Patient added successfully!")

        elif choice == '2':
            patient_id = int(input("Enter patient ID: "))
            patient = crud.get_patient(db, patient_id)
            if patient:
                print(f"\nPatient ID: {patient.id}")
                print(f"Name: {patient.name}")
                print(f"Birth Date: {patient.birth_date}")

                print("\nLab Tests:")
                lab_tests = crud.get_lab_tests_by_patient(db, patient_id)
                for test in lab_tests:
                    print(f"- {test.test_name} ({test.test_date})")

                print("\nTreatments:")
                treatments = crud.get_treatments_by_patient(db, patient_id)
                for treatment in treatments:
                    print(f"- {treatment.treatment_name} ({treatment.treatment_date})")
            else:
                print("Patient not found.")

        elif choice == '3':
            patient_id = int(input("Enter patient ID: "))
            test_name = input("Enter lab test name: ")
            test_date_str = input("Enter test date (YYYY-MM-DD): ")
            test_date = date.fromisoformat(test_date_str)
            lab_test = LabTest(test_name=test_name, test_date=test_date)
            crud.create_lab_test(db, lab_test, patient_id)
            print("Lab test added successfully!")

        elif choice == '4':
            patient_id = int(input("Enter patient ID: "))
            treatment_name = input("Enter treatment name: ")
            treatment_date_str = input("Enter treatment date (YYYY-MM-DD): ")
            treatment_date = date.fromisoformat(treatment_date_str)
            treatment = Treatment(treatment_name=treatment_name, treatment_date=treatment_date)
            crud.create_treatment(db, treatment, patient_id)
            print("Treatment added successfully!")

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
