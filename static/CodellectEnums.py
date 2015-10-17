from enum import Enum
__author__ = 'Ritesh_Ranjan'

class GenderEnum(Enum):
    Male = 0
    Female = 1
    Other = 2

class QuestionType(Enum):
    Tutorial = 0
    Challenging = 1
    Skipper = 2

class DeviceId(Enum):
    Web = 0;
    Mobile = 1
    Tablet = 2
    SettopBox = 3

#print(GenderEnum.__sizeof__())
#print(GenderEnum.Female)