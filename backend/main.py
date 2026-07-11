from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "This is agent brief app"}

