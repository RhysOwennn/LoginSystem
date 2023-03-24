from pydantic import BaseModel


class Settings(BaseModel):
    authjwt_secret_key: str = "my_jwt_secret"


# class User(BaseModel):
#     username: str
#     email: str
#     password: str


class User(BaseModel):
    username: str
    password: str