from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return 1/0
