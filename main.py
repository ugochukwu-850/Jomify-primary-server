from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This would eventually be the renderer for the home page or landing page ."}