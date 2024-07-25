from fastapi import FastAPI  # type: ignore
from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', response_model=Message)
def read_root():
  return {'message': 'Olár mundo'}
