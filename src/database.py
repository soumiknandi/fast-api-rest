import os
from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = os.environ['username'] if "username" in os.environ else "postgres"
password = os.environ['password'] if "password" in os.environ else "password"
host = os.environ['host'] if "host" in os.environ else "localhost"
database = os.environ['database'] if "database" in os.environ else "fastapi"
port = os.environ['port'] if "port" in os.environ else 5432

url_object = URL.create(
    "postgresql",
    username,
    password,
    host,
    port,
    database
)

engine = create_engine(url_object)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()