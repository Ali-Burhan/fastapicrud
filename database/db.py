from sqlmodel import Session, SQLModel, create_engine
from typing import Annotated
from fastapi import Depends

# postgresql://postgres:mysecretpassword@localhost:5432/mydatabase
postgress_url = "postgresql://postgres:786786@localhost:5432/practise"

# connect_args = {"check_same_thread": False}
engine = create_engine(postgress_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
