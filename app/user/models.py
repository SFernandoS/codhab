from fastapi import HTTPException
from sqlalchemy import Column, Integer, String
from app.databases import Base
import re


class User(Base):
    __tablename__ = 'USUARIOS'

    id = Column('id', Integer, autoincrement=True, primary_key=True)
    cpf = Column(String(11), nullable=True)
    nome = Column(String(80), nullable=True)
    email = Column(String(120), nullable=True)
    telefone = Column(String(11), nullable=True)

    def __init__(self, cpf, nome, email, telefone):
        self.cpf = self.check_cpf(cpf)
        self.nome = self.check_name(nome)
        self.email = self.check_email(email)
        self.telefone = self.check_tell(telefone)

    def json(self):
        return {
            'id': self.id,
            'cpf': self.cpf,
            'nome': self.nome,
            'email': self.email,
            'telefone': self.telefone
        }

    @staticmethod
    def set_user(user, cpf, nome, email, telefone):
        user.cpf = User.check_cpf(cpf)\
            if cpf else user.cpf
        user.nome = User.check_name(nome)\
            if nome else user.nome
        user.email = User.check_email(email)\
            if email else user.email
        user.telefone = User.check_tell(telefone)\
            if telefone else user.telefone

    @staticmethod
    def check_cpf(cpf) -> String:
        numbers = [int(digit) for digit in cpf if digit.isdigit()]
        if len(numbers) != 11 or len(set(numbers)) == 1:
            raise HTTPException(status_code=400, detail="Invalid cpf")
        return cpf

    @staticmethod
    def check_name(name) -> String:
        if (re.search(r'\d', name)):
            raise HTTPException(status_code=400, detail="Invalid name")
        elif (len(name) == 0):
            raise HTTPException(status_code=400, detail="Invalid name")
        return name

    @staticmethod
    def check_email(email) -> String:
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not (re.fullmatch(regex, email)):
            raise HTTPException(status_code=400, detail="Invalid email")
        return email

    @staticmethod
    def check_tell(telefone) -> String:
        numbers = [int(digit) for digit in telefone if digit.isdigit()]
        if len(numbers) != 11 or len(set(numbers)) == 1:
            raise HTTPException(status_code=400, detail="Invalid tell")
        return telefone
