from enum import Enum
__author__ = 'Ritesh_Ranjan'

class GenderEnum(Enum):
    Male = 0
    Female = 1
    Other = 2

class QuestionBankType(Enum):
    Tutorial = 0
    Challenging = 1
    Skipper = 2

class QuestionType(Enum):
    Objective = 0
    Coding = 1
    Other = 2

class DeviceId(Enum):
    Web = 0
    Mobile = 1
    Tablet = 2
    SettopBox = 3

class ContentType(Enum):
    User = 0
    Module = 1
    SubTopic = 2
    Video = 3
    Question = 4

#print(GenderEnum.__sizeof__())
#print(GenderEnum.Female)