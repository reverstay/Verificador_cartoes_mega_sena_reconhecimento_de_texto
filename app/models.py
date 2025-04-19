from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import datetime

Base = declarative_base()

class Jogo(Base):
    __tablename__ = 'jogos'
    id        = Column(Integer, primary_key=True)
    imagem    = Column(String, nullable=False)
    numeros   = Column(String, nullable=False)  # ex: "03,15,22,33,46,58"
    criado_em = Column(DateTime, default=datetime.datetime.utcnow)

def get_session(db_path="sqlite:///../db/mega.db"):
    engine = create_engine(db_path, echo=False, future=True)
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()
