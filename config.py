from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://dan:123@localhost/central')
session = sessionmaker(bind=engine)
con = session()

base = declarative_base()