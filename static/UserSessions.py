from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, relationship, backref
import CodellectEnums
from sqlalchemy import create_engine
from flask import json
import AlchemyEncoder

__author__ = 'Ritesh_Ranjan'

Base = declarative_base()


class UserSessions(Base):
    __tableName_ = 'user_session'
    ID = Column(Integer,primary_key=True)
    USER_ID = Column(Integer,ForeignKey('users.ID'))
    USERS = relationship("users", backref=backref("user_session", uselist=False))
    SESSION_ID = Column(String(30),nullable=False)
    IS_ACTIVE = Column(Integer,default=0)
    LAST_SESSION_ID = Column(String(30))
    CLIENT_IP_ADDRESS = Column(String(15))
    CLIENT_DEVICE_TYPE_ID = Column(Integer,default=0)
    @validates('CLIENT_DEVICE_TYPE_ID')

    def validate_sex(self, id):
        assert id in CodellectEnums.DeviceId
        return id

    @property
    def serialize(self):
        return json.dumps(self, cls=AlchemyEncoder)

engine = create_engine('postgresql:///codellect_db', echo=True)
Base.metadata.create_all(engine)


