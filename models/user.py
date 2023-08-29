from pydantic import BaseModel
import datetime
from typing import Optional


class UserModel(BaseModel):
    id: Optional[int]
    username: str
    password: str
    email: str
    is_active: bool
    is_admin: bool
    created_at: datetime.datetime = datetime.datetime.now()
    updated_at: datetime.datetime = datetime.datetime.now()
