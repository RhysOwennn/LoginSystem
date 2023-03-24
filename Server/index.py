
from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from models.user import Settings, User
from fastapi_jwt_auth import AuthJWT
from fastapi_jwt_auth.exceptions import AuthJWTException
from fastapi.middleware.cors import CORSMiddleware
from config.db import connection
from schemas.user import userEntity, usersEntity
from bson import ObjectId 

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@AuthJWT.load_config
def get_config():
    return Settings()


@app.exception_handler(AuthJWTException)
def authjwt_exception_handler(request: Request, exc: AuthJWTException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message}
    )

@app.post('/login')
def login(user: User, Authorize: AuthJWT = Depends()):

    found_user = connection.users.user_collection.find_one({"username": user.username, "password": user.password})

    if found_user is None:
        return {"error": "Invalid username or password"}
    
    access_token = Authorize.create_access_token(subject=user.username)
    return {"access_token": access_token}

@app.get('/test-jwt')
def user(Authorize: AuthJWT = Depends()):
    
    Authorize.jwt_required()
    return {"user": 123124124, 'data': 'jwt test works'} 
    #current_user = Authorize.get_jwt_subject()
    #return {"user": current_user, 'data': 'jwt test works'}

@app.get('/')
async def find_all_users():
    return usersEntity(connection.users.user_collection.find())

@app.get('/{id}')
async def find_user(id):
    return userEntity(connection.users.user_collection.find_one({"_id":ObjectId(id)}))

@app.post('/')
async def create_user(user: User):
    connection.users.user_collection.insert_one(dict(user))
    return usersEntity(connection.users.user_collection.find())


@app.put('/{id}')
async def update_user(id, user: User):
    connection.users.user_collection.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(user)})
    return userEntity(connection.users.user_collection.find_one({"_id":ObjectId(id)}))

@app.delete('/{id}')
async def delete_user(id, user: User):
    connection.local.user.find_one_and_delete({"_id":ObjectId(id)})
    return userEntity(connection.users.user_collection.find_one({"_id":ObjectId(id)}))
