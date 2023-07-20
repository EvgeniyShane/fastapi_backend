from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str

class Article(BaseModel):
    title: str
    content: str
    owner: User