from Models.user_model import UserModel
from flask import abort, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model

#######################################
#CRUD для юзера
#######################################

def create(person):
    iden = person.get("id")
    name = person.get("name")

    
    check = UserModel.get_or_none(user_id=iden)
    if check is None: 
        UserModel.create(user_id = iden,
                         user_name= name
                         )
        out_object = UserModel.select().where(UserModel.user_id == iden).get()
        out_object = model_to_dict(out_object)
        return out_object, 201       
    else:
        abort(
            406,
            f"User with name {name} can't be create",
        )
        