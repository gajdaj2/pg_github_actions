from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/calc")
async def calculate(a: int, b: int) -> int:
    return a + b



