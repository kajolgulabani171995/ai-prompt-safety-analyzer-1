import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from analyzer import analyze_prompt

app = FastAPI(title="AI Prompt Safety Analyzer")

app.mount("/static", StaticFiles(directory="static"), name="static")


class PromptRequest(BaseModel):
    prompt: str


@app.get("/")
async def root():
    return FileResponse("static/index.html")


@app.post("/analyze")
async def analyze(request: PromptRequest):
    if not request.prompt.strip():
        return {"error": "Prompt cannot be empty"}
    result = analyze_prompt(request.prompt)
    return result


@app.get("/health")
async def health():
    return {"status": "ok"}