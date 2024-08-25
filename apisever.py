from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Define the data model for POST request
class UserRequest(BaseModel):
    user_id: int
    college_email: str
    college_roll_number: str
    numbers: List[int]
    alphabets: List[str]

# POST method endpoint
@app.post("/process/")
async def process_data(request: UserRequest):
    # Logic to determine the highest lowercase alphabet
    lowercase_alphabets = [char for char in request.alphabets if char.islower()]
    highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None
    
    # Response dictionary
    response = {
        "status": "success",
        "user_id": request.user_id,
        "college_email": request.college_email,
        "college_roll_number": request.college_roll_number,
        "numbers": request.numbers,
        "alphabets": request.alphabets,
        "highest_lowercase": highest_lowercase
    }
    return response

# GET method endpoint
@app.get("/operation_code/")
async def get_operation_code():
    operation_code = "OPERATION1234"  # This can be any predefined code or dynamically generated
    return {"operation_code": operation_code}
