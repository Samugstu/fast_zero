from http import HTTPStatus

from fastapi import FastAPI  # type: ignore

from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
  return {'message': 'Olár mundo'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):

  user_com_id = UserDB(
    id=len(database) + 1,
    **user.model_dump()
    )

  database.append(user_com_id)
  return user_com_id
