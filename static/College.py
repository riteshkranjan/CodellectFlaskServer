from sqlalchemy import Column, Integer, String, DateTime
from flask import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import AlchemyEncoder

__author__ = 'Ritesh_Ranjan'

Base = declarative_base()


class College(Base):
    __tableName_ = 'college'
    COLLEGE_ID = Column(Integer, primary_key=True)
    COLLEGE_NAME = Column(String(20))
    ADDRESS = Column(String(200))
    AUTO_RENEW = Column(Integer, default=0)
    LICENSE_EXPIRE_DATE = Column(DateTime)

    @property
    def serialize(self):
        return json.dumps(self, cls=AlchemyEncoder)

engine = create_engine('postgresql:///codellect_db', echo=True)
Base.metadata.create_all(engine)
