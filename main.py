from fastapi import FastAPI

app = FastAPI()
# I added a while true to keep the function running.
while True:
    @app.get("/")
    def read_root():
        return {"Hello": "World"}
    break