from peewee import *
from Models.base_model import BaseModel
from Models.user_model import UserModel

class TaskModel(BaseModel):
       task_id = AutoField(column_name='task_id')
       user_id = ForeignKeyField(UserModel, to_field='user_id')
       task_description = TextField(column_name='task_description', null=True) 

       class Meta:
              table_name = 'tasks'