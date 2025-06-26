import string
import random
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/password-generator")
def passwordgenerator(length: int):
    
    password = []
    for i in range(length):
        randomchar = ''.join(random.choices(string.ascii_letters + string.digits + string.printable))
        password.append(randomchar)
        
    return ''.join(password)
    

@app.get("/ping")
async def ping():
    return JSONResponse(content={"message": "pong"}, status_code=200)
