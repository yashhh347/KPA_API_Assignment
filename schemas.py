from pydantic import BaseModel

class PersonalDetailsBase(BaseModel):
    name: str
    phone_number: str
    email: str

class PersonalDetailsCreate(PersonalDetailsBase):
    pass

class PersonalDetailsResponse(PersonalDetailsBase):
    id: int

    class Config:
        orm_mode = True
