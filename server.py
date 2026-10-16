#!/usr/bin/env python3
"""Minimal OpenAPI echo tool for Family AI GitHub self-install smoke tests."""
from __future__ import annotations

import os
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel, Field

BIND = os.environ.get("TOOL_BIND", "127.0.0.1")
PORT = int(os.environ.get("TOOL_PORT", "28901"))

app = FastAPI(
    title="Hello Family OWUI Tool",
    description="Benign echo tool installed from GitHub for GLM self-service smoke tests.",
    version="1.0.0",
)


class EchoRequest(BaseModel):
    message: str = Field(..., description="Text to echo back")


@app.get("/healthz", include_in_schema=False)
def healthz() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/openapi.json", include_in_schema=False)
def openapi_json() -> dict[str, Any]:
    return app.openapi()


@app.post("/echo", operation_id="echo_message")
def echo_message(body: EchoRequest) -> dict[str, Any]:
    return {"ok": True, "echo": body.message, "tool": "hello-family-owui-tool"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=BIND, port=PORT, log_level="info")
