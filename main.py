from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# routings
from apis.routers.index import router as Rooting

# config
from configs.config import config

app = FastAPI(title=config["TITLE"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=config["HOST"], port=config["PORT"])

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Rooting)
