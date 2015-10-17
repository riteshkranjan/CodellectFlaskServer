from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from flask import json
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, relationship, backref

import CodellectEnums
from sqlalchemy import create_engine
import AlchemyEncoder
import CommonUtils

__author__ = 'Ritesh_Ranjan'

Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    ID = Column(Integer, primary_key=True)
    EMAIL_ID = Column(String(50), nullable=False, index=True)
    PASSWORD = Column(String(50), nullable=False)
    COLLEGE_ID = Column(Integer, ForeignKey('college.COLLEGE_ID'))
    COLLEGE = relationship("college", backref=backref("users", uselist=False))
    FIRST_NAME = Column(String(50))
    MIDDLE_NAME = Column(String(50))
    LAST_NAME = Column(String(50))
    AGE = Column(Integer)
    SEX = Column(Integer, default=CodellectEnums.GenderEnum.Male)

    @validates('EMAIL_ID')
    def validate_email(self, address):
        assert '@' in address
        return address

    @validates('SEX')
    def validate_sex(self, gender):
        assert gender in CodellectEnums.GenderEnum
        return gender

    def validate_sex(self, id):
        assert id in CodellectEnums.DeviceId
        return id

    @property
    def serialize(self):
        return json.dumps(self, cls=AlchemyEncoder)


engine = create_engine(CommonUtils.dbtype + ':///' + CommonUtils.dbname, echo=True)
Base.metadata.create_all(engine)
