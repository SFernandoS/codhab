from sqlalchemy import Column, Integer, String
from databases import Base


class User(Base):
    __tablename__ = 'USUARIOS'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    cpf = Column(String(11), nullable=True)
    nome = Column(String(80), nullable=True)
    email = Column(String(120), nullable=True)
    telefone = Column(String(11), nullable=True)

    def json(self):
        return {
            'id': self.id,
            'cpf': self.cpf,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone
        }