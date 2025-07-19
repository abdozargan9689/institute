import unittest
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from clinic_project.models import Base, Patient, LabTest, Treatment
from clinic_project import crud

class TestCrud(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.db = Session()

    def tearDown(self):
        self.db.close()

    def test_create_and_get_patient(self):
        patient = Patient(name="John Doe", birth_date=date(1990, 1, 1))
        created_patient = crud.create_patient(self.db, patient)
        self.assertIsNotNone(created_patient.id)
        self.assertEqual(created_patient.name, "John Doe")

        retrieved_patient = crud.get_patient(self.db, created_patient.id)
        self.assertEqual(retrieved_patient.name, "John Doe")

    def test_create_and_get_lab_test(self):
        patient = Patient(name="Jane Doe", birth_date=date(1992, 2, 2))
        created_patient = crud.create_patient(self.db, patient)

        lab_test = LabTest(test_name="Blood Test", test_date=date(2023, 1, 1))
        created_lab_test = crud.create_lab_test(self.db, lab_test, created_patient.id)
        self.assertIsNotNone(created_lab_test.id)
        self.assertEqual(created_lab_test.test_name, "Blood Test")

        lab_tests = crud.get_lab_tests_by_patient(self.db, created_patient.id)
        self.assertEqual(len(lab_tests), 1)
        self.assertEqual(lab_tests[0].test_name, "Blood Test")

    def test_create_and_get_treatment(self):
        patient = Patient(name="Jim Doe", birth_date=date(1994, 3, 3))
        created_patient = crud.create_patient(self.db, patient)

        treatment = Treatment(treatment_name="Antibiotics", treatment_date=date(2023, 1, 1))
        created_treatment = crud.create_treatment(self.db, treatment, created_patient.id)
        self.assertIsNotNone(created_treatment.id)
        self.assertEqual(created_treatment.treatment_name, "Antibiotics")

        treatments = crud.get_treatments_by_patient(self.db, created_patient.id)
        self.assertEqual(len(treatments), 1)
        self.assertEqual(treatments[0].treatment_name, "Antibiotics")

if __name__ == '__main__':
    unittest.main()
