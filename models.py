from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
# Import the Base from your database configuration file
from database import Base, engine

class Woreda(Base):
    __tablename__ = "woredas"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    
    # Relationship to Kebeles
    kebeles = relationship("Kebele", back_populates="parent_woreda", cascade="all, delete-orphan")

class Kebele(Base):
    __tablename__ = "kebeles"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    woreda_id = Column(Integer, ForeignKey("woredas.id"))
    
    # Relationship back to Woreda
    parent_woreda = relationship("Woreda", back_populates="kebeles")

class Farmer(Base):
    __tablename__ = "farmers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    f_type = Column(String)
    woreda = Column(String)
    kebele = Column(String)
    phone = Column(String)
    audio_url = Column(String)
    registered_by = Column(String)
    
    # --- Tree Seedling Varieties ---
    gesho = Column(Integer, default=0)
    giravila = Column(Integer, default=0)
    diceres = Column(Integer, default=0)
    wanza = Column(Integer, default=0)
    papaya = Column(Integer, default=0)
    moringa = Column(Integer, default=0)
    lemon = Column(Integer, default=0)
    arzelibanos = Column(Integer, default=0)
    guava = Column(Integer, default=0)

# Function to create the tables in the database
def create_tables():
    Base.metadata.create_all(bind=engine)
