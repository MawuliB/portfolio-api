from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://mawuli:ZeV4bKGI9llkpfqynrsEHqs13exW6YmL@dpg-cfmbj14gqg469ktg1flg-a/db_zz2w"

engine = create_engine(DATABASE_URL)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
