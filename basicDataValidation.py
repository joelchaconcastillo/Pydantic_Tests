from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    age: int

# Creating an instance and validating data
user_data = {
    "username": "john_doe",
    "email": "johndoe@example.com",
    "age": 10
}
user = User(**user_data)

print(user.username)  # "john_doe"
print(user.email)     # "johndoe@example.com"
print(user.age)       # 30
