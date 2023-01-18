from pydantic import BaseModel

class UserSchema(BaseModel):
    cpf: str
    nome: str
    email: str
    telefone: str