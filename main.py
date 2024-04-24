from fastapi import FastAPI

# routings
from apis.routers.index import router as Rooting

# config
from configs.config import config

app = FastAPI(title=config["TITLE"])

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=config["HOST"], port=config["PORT"])

app.include_router(Rooting)
