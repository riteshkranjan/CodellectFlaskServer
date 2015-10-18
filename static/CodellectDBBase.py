from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates, relationship, backref
import CodellectEnums
from sqlalchemy import create_engine
from flask import json
import AlchemyEncoder, CommonUtils

__author__ = 'Ritesh_Ranjan'

Base = declarative_base()

class College(Base):
    __tablename__ = 'college'
    # __table_args__ = {'schema':CommonUtils.dbschema}

    COLLEGE_ID = Column(Integer, primary_key=True)
    COLLEGE_NAME = Column(String(20))
    ADDRESS = Column(String(200))
    AUTO_RENEW = Column(Integer, default=0)
    LICENSE_EXPIRE_DATE = Column(DateTime)

    @property
    def serialize(self):
        return json.dumps(self, cls=AlchemyEncoder)


class Users(Base):
    __tablename__ = 'users'

    ID = Column(Integer, primary_key=True)
    EMAIL_ID = Column(String(50), nullable=False, index=True)
    PASSWORD = Column(String(50), nullable=False)
    COLLEGE_ID = Column(Integer, ForeignKey('college.COLLEGE_ID'))
    COLLEGE = relationship("College", backref=backref("Users", uselist=False))
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


class UserSessions(Base):
    __tablename__ = 'user_session'
    # __table_args__ = {'schema':CommonUtils.dbschema}

    ID = Column(Integer, primary_key=True)
    USER_ID = Column(Integer, ForeignKey('users.ID'))
    USERS = relationship("Users", backref=backref("UserSessions", uselist=False))
    SESSION_ID = Column(String(30), nullable=False)
    IS_ACTIVE = Column(Integer, default=0)
    LAST_SESSION_ID = Column(String(30))
    CLIENT_IP_ADDRESS = Column(String(15))
    CLIENT_DEVICE_TYPE_ID = Column(Integer, default=0)

    @validates('CLIENT_DEVICE_TYPE_ID')
    def validate_device_id(self, id):
        assert id in CodellectEnums.DeviceId
        return id

    @property
    def serialize(self):
        return json.dumps(self, cls=AlchemyEncoder)

class Rating(Base):
    __tablename__ = 'rating'

    ID = Column(Integer, primary_key=True)
    RATING_ON = Column(Integer)
    VALUE = Column(Integer)
    COUNT = Column(Integer)

    @validates('RATING_ON')
    def validate_device_id(self, id):
        assert id in CodellectEnums.ContentType
        return id

class Modules(Base):
    __tablename__ = 'modules'

    ID = Column(Integer, primary_key=True)
    NAME = Column(String(20), nullable=False, index=True)
    DESCRIPTION = Column(String(200))
    PARENT_ID = Column(Integer)
    COLLEGE_ID = Column(Integer, ForeignKey('college.COLLEGE_ID'))
    # many to one relattion COLLEGE = relationship("College", backref=backref("modules", uselist=False))
    ATTENDED_USER_COUNT = Column(Integer)
    IMAGE = Column(String(200))

class TutorialSubtopic(Base):
    __tablename__ = 'tutorial_subtopic'

    ID = Column(Integer,primary_key=True)
    NAME = Column(String(20),nullable=False,index=True)
    DESCRIPTION = Column(String(200))
    MODULE_ID = Column(Integer, ForeignKey('modules.ID'))
    #many to many relattion ship

class TutorialVideo(Base):
    __tablename__ = 'tutorial_video'

    ID = Column(Integer, primary_key=True)
    NAME = Column(String(20), nullable=False, index=True)
    DESCRIPTION = Column(String(200))
    SUBTOPIC_ID = Column(Integer,ForeignKey('tutorial_subtopic.ID'))
    #many to many relationship to be added here
    SEQUENCE_NO = Column(Integer)
    REFERENCE_LINK = Column(String(100))

class TutorialQbank(Base):
    __tablename__ = 'tutorial_qbank'

    ID = Column(Integer, primary_key=True)
    SUBTOPIC_ID = Column(Integer,ForeignKey('tutorial_subtopic.ID'))
    #many to many relationship to be added here
    DESCRIPTION = Column(String(200))
    QUESTION_BANK_TYPE = Column(Integer)
    CORRECT_ANSWERS = Column(String(1000))
    WRONG_ANSWERS = Column(String(1000))
    MAX = Column(Integer)
    AVERAGE_SOLVE_TIME = Column(Integer)
    TAG = Column(String(50))
    APPROACH = Column(String(200))
    HINT = Column(String(200))
    QUESTION_TYPE = Column(Integer)
    TEST_CASE_INPUT = Column(String(1000))
    TEST_CASE_OUTPUT = Column(String(1000))

    @validates('QUESTION_BANK_TYPE')
    def validate_device_id(self, id):
        assert id in CodellectEnums.QuestionBankType
        return id

    @validates('QUESTION_TYPE')
    def validate_device_id(self, id):
        assert id in CodellectEnums.QuestionType
        return id

class UserBookmark(Base):
    __tablename__ = "user_bookmark"

    ID = Column(Integer, primary_key=True)
    USER_ID = Column(Integer, ForeignKey('users.ID'))
    #add many to one relation ship here
    BOOKMARK_ON = Column(Integer)
    BOOKMARK_ID = Column(Integer)

    @validates('BOOKMARK_ON')
    def validate_device_id(self, id):
        assert id in CodellectEnums.ContentType
        return id

class UserProgress(Base):
    __tablename__ = "user_progress"

    ID = Column(Integer, primary_key=True)
    USER_ID = Column(Integer, ForeignKey('users.ID'))
    #add many to one relation ship here
    QUESTION_BANK_ID = Column(Integer)
    VIDEO_ID = Column(Integer)
    MODULE_ID = Column(Integer)
    SUBTOPIC_ID = Column(Integer)

class UserScore(Base):
    __tablename__ = "user_score"

    ID = Column(Integer, primary_key=True)
    USER_ID = Column(Integer, ForeignKey('users.ID'))
    #add many to one relation ship here
    SOLVE_TIME = Column(Integer)
    SCORE = Column(Integer)
    SUGGESTIONS = Column(String(200))

engine = create_engine(CommonUtils.dbtype + ':///' + CommonUtils.dbname, echo=True)
Base.metadata.create_all(engine)
