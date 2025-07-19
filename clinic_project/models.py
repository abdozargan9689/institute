from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birth_date = Column(Date)

    lab_tests = relationship("LabTest", back_populates="patient")
    treatments = relationship("Treatment", back_populates="patient")

    def __repr__(self):
        return f"<Patient(id={self.id}, name='{self.name}')>"

class LabTest(Base):
    __tablename__ = 'lab_tests'

    id = Column(Integer, primary_key=True)
    test_name = Column(String)
    test_date = Column(Date)
    patient_id = Column(Integer, ForeignKey('patients.id'))

    patient = relationship("Patient", back_populates="lab_tests")

    def __repr__(self):
        return f"<LabTest(id={self.id}, test_name='{self.test_name}')>"

class Treatment(Base):
    __tablename__ = 'treatments'

    id = Column(Integer, primary_key=True)
    treatment_name = Column(String)
    treatment_date = Column(Date)
    patient_id = Column(Integer, ForeignKey('patients.id'))

    patient = relationship("Patient", back_populates="treatments")

    def __repr__(self):
        return f"<Treatment(id={self.id}, treatment_name='{self.treatment_name}')>"
