#  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣦⣴⣶⣾⣿⣶⣶⣶⣶⣦⣤⣄⠀⠀⠀⠀⠀⠀⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢠⡶⠻⠛⠟⠋⠉⠀⠈⠤⠴⠶⠶⢾⣿⣿⣿⣷⣦⠄⠀⠀⠀                 𓐓  main.py 𓐔           
#  ⠀⠀⠀⠀⠀⢀⠔⠋⠀⠀⠤⠒⠒⢲⠀⠀⠀⢀⣠⣤⣤⣬⣽⣿⣿⣿⣷⣄⠀⠀
#  ⠀⠀⠀⣀⣎⢤⣶⣾⠅⠀⠀⢀⡤⠏⠀⠀⠀⠠⣄⣈⡙⠻⢿⣿⣿⣿⣿⣿⣦⠀      Eng: oussama <oussama.ezzaou@gmail.com>
#  ⢀⠔⠉⠀⠊⠿⠿⣿⠂⠠⠢⣤⠤⣤⣼⣿⣶⣶⣤⣝⣻⣷⣦⣍⡻⣿⣿⣿⣿⡀
#  ⢾⣾⣆⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
#  ⠀⠈⢋⢹⠋⠉⠙⢦⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇       Created: 2025/10/27 14:55:33 by oussama
#  ⠀⠀⠀⠑⠀⠀⠀⠈⡇⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇       Updated: 2025/10/31 11:37:24 by oussama
#  ⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⢀⣾⣿⣿⠿⠟⠛⠋⠛⢿⣿⣿⠻⣿⣿⣿⣿⡿⠀
#  ⠀⠀⠀⠀⠀⠀⠀⢀⠇⠀⢠⣿⣟⣭⣤⣶⣦⣄⡀⠀⠀⠈⠻⠀⠘⣿⣿⣿⠇⠀
#  ⠀⠀⠀⠀⠀⠱⠤⠊⠀⢀⣿⡿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠘⣿⠏⠀⠀                             𓆩♕𓆪
#  ⠀⠀⠀⠀⠀⡄⠀⠀⠀⠘⢧⡀⠀⠀⠸⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠐⠋⠀⠀⠀                     𓄂 oussama ezzaou𓆃
#  ⠀⠀⠀⠀⠀⠘⠄⣀⡀⠸⠓⠀⠀⠀⠠⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

# ===[ Imports ]===============================================================
from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel, Field
from enum import IntEnum

app = FastAPI()


class Case(IntEnum):
    single = 1
    engaged = 2
    merried = 3


# ===[ Schema: ]===============================================================
class UserBase(BaseModel):
    name: str = Field(min_length=1, max_length=10, description="Hello World")
    case: Case = Field(default=Case.single)


# ===[ User ]===
class User(UserBase):
    id: int = Field(0)


# ===[ UserCreate ]===
class UserCreate(UserBase):
    pass


# ===[ UserUpdate ]===
class UserUpdate(BaseModel):
    name: Optional[str] = None
    case: Optional[Case] = 0


# ===[ users ]===
users = [
    User(id=0, name="oussama", case=Case.single),
    User(id=1, name="hamza", case=Case.single),
    User(id=2, name="omar", case=Case.engaged),
    User(id=3, name="abdelmajid", case=Case.merried),
]


# ===[ get ]===================================================================
# Using Path parameters to pass data in the `URL`
@app.get("/{id}", response_model=User)
def get_user(id: int):
    for user in users:
        if user.id == id:
            return user
    raise HTTPException(status_code=404, detail="User Not Found")


@app.get("/", response_model=list[User])
def get_users(end: int):
    return users[: end] if end else users


# ===[ post ]==================================================================
@app.post("/create", response_model=User)
def post_function(user: UserCreate):
    id = users.index(users[-1]) + 1
    new_user = User(id=id, name=user.name, case=user.case)
    users.append(User(id=id, name=user.name, case=user.case))
    return new_user

# NOTE:------------------------------------------------------------------------
# - 'Creation' does not require the [ id ],
# - It is choosed by me, so no need to use the `User` Model
# - That is why we should use another Model class that does not contain
#   the `id` as an attributes for good readibility and in a profional way.


# ===[ put ]===================================================================
@app.put("/put/{id}", response_model=User)
def put_function(id: int, user: UserUpdate):
    for us in users:
        if us.id == id:
            if us.name is not None:
                us.name = user.name
                us.case = user.case
            return us
    raise HTTPException(status_code=404, detail="User Not Found")


# NOTE:------------------------------------------------------------------------
# - The `Update` process does not require, to update all fields, we can update
#   one field or more, which means these fields stay optional
# - We need to create another `class model` for the response that does require
#   optional values `UserUpdate`


# ===[ delete ]================================================================
@app.delete("/delete/{id}")
def delete_function(id: int):
    for us in users:
        if us.id == id:
            return users.pop(users.index(us))
    raise HTTPException(status_code=404, detail="User Not Found")
