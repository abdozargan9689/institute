from sqlalchemy.orm import Session
from clinic_project import models

def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.id == patient_id).first()

def get_patients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Patient).offset(skip).limit(limit).all()

def create_patient(db: Session, patient: models.Patient):
    db.add(patient)
    db.commit()
    db.refresh(patient)
    return patient

def create_lab_test(db: Session, lab_test: models.LabTest, patient_id: int):
    lab_test.patient_id = patient_id
    db.add(lab_test)
    db.commit()
    db.refresh(lab_test)
    return lab_test

def get_lab_tests_by_patient(db: Session, patient_id: int):
    return db.query(models.LabTest).filter(models.LabTest.patient_id == patient_id).all()

def create_treatment(db: Session, treatment: models.Treatment, patient_id: int):
    treatment.patient_id = patient_id
    db.add(treatment)
    db.commit()
    db.refresh(treatment)
    return treatment

def get_treatments_by_patient(db: Session, patient_id: int):
    return db.query(models.Treatment).filter(models.Treatment.patient_id == patient_id).all()
