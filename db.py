from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///health.db")
Base = declarative_base()

class HealthData(Base):
    __tablename__ = "health_data"

    id = Column(Integer, primary_key=True)
    device_id = Column(String)
    heart_rate = Column(Integer)
    temperature = Column(Float)
    spo2 = Column(Integer)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
