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
    
    # --- New Tree Columns ---
    gesho = Column(Integer, default=0)
    giravila = Column(Integer, default=0)
    diceres = Column(Integer, default=0)
    wanza = Column(Integer, default=0)
    papaya = Column(Integer, default=0)
    moringa = Column(Integer, default=0)
    lemon = Column(Integer, default=0)
    arzelibanos = Column(Integer, default=0)
    guava = Column(Integer, default=0)
