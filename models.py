from sqlmodel import Field, SQLModel, Relationship


class UserAddressLink(SQLModel, table=True):
  user_id: int = Field(foreign_key="user.id", primary_key=True)
  address_id: int = Field(foreign_key="address.id", primary_key=True)

class User(SQLModel, table=True):
  id: int = Field(primary_key=True)
  name: str
  email: str 
  
  profile: "Profile" | None = Relationship(back_populates="user")
  post : list["Post"] = Relationship(back_populates="user")
  
  
  

# ONE_TO_ONE Relationship
class Profile(SQLModel, table=True):
  id: int = Field(primary_key=True)
  
  # Each User has one Profile
  user_id: int = Field(foreign_key="user.id", unique=True)
  bio: str
  
  user : "User" = Relationship(back_populates="profile")
  


# ONE_TO_MANY
class Post(SQLModel, table=True):
  id: int = Field(primary_key=True)
  
  # Each User has multiple post
  user_id: int = Field(foreign_key="user.id")
  title: str
  content: str
  
  user : "User" = Relationship(back_populates="post")
  

# MANY_TO_MANY
class Address(SQLModel, table=True):
  id: int = Field(primary_key=True)
  street: str
  city: str
  