from enum import Enum
from pydantic import BaseModel, Field, conlist

class GenderEnum(str, Enum):
    Male = "Male"
    Female = "Female"


class User(BaseModel):
    Age: str
    Gender: GenderEnum
    Education: str
    Country: str 
    Ethnicity: str
    Nscore: int = Field(..., gt=12, lt=60)
    Escore: int = Field(..., gt=16, lt=59)
    Oscore: int = Field(..., gt=24, lt=60)
    Ascore: int = Field(..., gt=12, lt=60)
    Cscore: int = Field(..., gt=17, lt=59)
    Impulsive: int = Field(..., gt=1, lt=10)
    SS: int = Field(..., gt=1, lt=11)

class Result(BaseModel):
    Alcohol: int
    Amphet: int
    Amyl: int
    Benzos: int
    Caffeine: int
    Cannabis: int
    Chocolate: int
    Coke: int
    Crack: int
    Ecstasy: int
    Heroin: int
    Ketamine: int
    Legalh: int
    LSD: int
    Meth: int
    Mushrooms: int
    Nicotine: int
    Semer: int
    VSA: int

