from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from core.config import settings
from core.logging_config import configure_logging
from core.security import api_key_auth_middleware
from core.size_limit import SizeLimitMiddleware
from db.database import init_db, close_db
from routers import ingest, query, entity, alerts, agent

load_dotenv()
configure_logging()

app = FastAPI(title="Memory API — Online Test (Zep + OpenAI)")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request size limit
app.add_middleware(SizeLimitMiddleware, max_content_size_mb=25)

# API Key / JWT middleware
app.middleware("http")(api_key_auth_middleware)

# Routers
app.include_router(ingest.router, prefix="/ingest", tags=["ingest"])
app.include_router(query.router, prefix="/query", tags=["query"])
app.include_router(entity.router, prefix="/entity", tags=["entity"])
app.include_router(alerts.router, prefix="/alerts", tags=["alerts"])
app.include_router(agent.router, prefix="/agent", tags=["agent"])

@app.on_event("startup")
async def on_startup():
    await init_db()

@app.on_event("shutdown")
async def on_shutdown():
    await close_db()

@app.get("/health")
async def health():
    return {"status": "ok"}
