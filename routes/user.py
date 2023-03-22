from fastapi import APIRouter

from models.user import User
from config.db import connection
from schemas.user import userEntity, usersEntity
from bson import ObjectId 

user = APIRouter()

@user.get('/')
async def find_all_users():
    return usersEntity(connection.users.user_collection.find())

@user.get('/{id}')
async def find_user(id):
    return userEntity(connection.users.user_collection.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user: User):
    connection.users.user_collection.insert_one(dict(user))
    return usersEntity(connection.users.user_collection.find())


@user.put('/{id}')
async def update_user(id, user: User):
    connection.users.user_collection.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(user)})
    return userEntity(connection.users.user_collection.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id, user: User):
    connection.local.user.find_one_and_delete({"_id":ObjectId(id)})
    return userEntity(connection.users.user_collection.find_one({"_id":ObjectId(id)}))