from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import articles, members, categories

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hasegawa Lab API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(articles.router)
app.include_router(members.router)
app.include_router(categories.router)


@app.get("/")
def root():
    return {"status": "ok"}
