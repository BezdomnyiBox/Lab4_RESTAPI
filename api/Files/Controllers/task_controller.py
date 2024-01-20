from Models.task_model import TaskModel
from Models.user_model import UserModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для договора
#######################################
def read_all(iden):
    check = UserModel.get_or_none(user_id=iden)
    if check is not None:
        out_object = list(TaskModel.select().where(TaskModel.user_id == iden).dicts()) 
        return out_object, 201       
    else:
        abort(
            404,
            f"Task with user ID {iden} can't be found",
        )

def create(person):
    iden = person.get("id")
    user_id = person.get("user_id")
    desc= person.get("desc")
    
    check = TaskModel.get_or_none(task_id=iden)
    if check is None: 
        TaskModel.create(task_id= iden,
                         user_id= user_id,
                         task_description = desc
                         )
        out_object = TaskModel.select().where(TaskModel.task_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"Task with ID {iden} can't be create",
        )
        
def update(iden, person):
    check = TaskModel.get_or_none(task_id=iden)
    if check is not None:
        query = TaskModel.update(user_id=person.get("user_id"),
                                 task_description=person.get("desc")).where(TaskModel.task_id == iden)
        query.execute()
        out_object = TaskModel.select().where(TaskModel.task_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object   
    else:
        abort(
            404,
            f"Task with ID {iden} not found"
        )

def delete(iden):
    check = TaskModel.get_or_none(task_id=iden)
    if check is not None:
        query = TaskModel.delete().where(TaskModel.task_id == iden)
        query.execute()
        return make_response(
            f"Task with ID {iden} successfully deleted", 204
        )
    else:
        abort(
            404,
            f"Task with ID {iden} not found"
        )