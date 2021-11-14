from fastapi import FastAPI, Form
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return { "Lux app":"Jambo Dunia" }

@app.post("/signup/")
async def signup(name : str = Form(...),country: str = Form(...),email: str = Form(...),username: str = Form(...),password: str = Form(...) ):
    return { "name":name,"country":country,"email":email,"username":username, "password":password }
@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return{ "username": username, "password": password}
if __name__ == "__main__":
    uvicorn.run('server:app', port=8000, reload=False)