from pydantic import BaseModel, Field, ConfigDict


# User Registration
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=8, max_length=72)


# User Login
class UserLogin(BaseModel):
    username: str
    password: str


# User Response
class UserResponse(BaseModel):
    id: int
    username: str

    model_config = ConfigDict(from_attributes=True)


# JWT Token Response
class Token(BaseModel):
    access_token: str
    token_type: str


# Create Note
class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1, max_length=5000)


# Update Note
class NoteUpdate(BaseModel):
    title: str | None = Field(default=None, max_length=100)
    content: str | None = Field(default=None, max_length=5000)


# Note Response
class NoteResponse(BaseModel):
    id: int
    title: str
    content: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)