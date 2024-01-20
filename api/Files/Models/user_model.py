from peewee import *
from Models.base_model import BaseModel

class UserModel(BaseModel):
       user_id = AutoField(column_name='user_id')
       user_name = TextField(column_name='user_name', null=True)          
       class Meta:
              table_name = 'users'