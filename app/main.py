from fastapi import FastAPI

app = FastAPI(
    title = "Exocortex AI",
    description = "An AI platform for augumented human cognition",
    version = "0.1.0"
)

@app.get("/")
def root():
    return {
        "project": "Exocortex AI",
        "status": "Running",
        "version": "0.1.0"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

