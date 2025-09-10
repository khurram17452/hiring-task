from pydantic import BaseModel, EmailStr, StringConstraints
from typing import Annotated

# Define reusable type for name with length limits
NameStr = Annotated[str, StringConstraints(min_length=2, max_length=50)]

class UserBase(BaseModel):
    name: NameStr
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    class Config:
        orm_mode = True
