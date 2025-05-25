from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load student marks from file
DATA_FILE = Path(__file__).parent.parent / "marks.json"
with open(DATA_FILE, "r") as f:
    student_marks = json.load(f)

@app.get("/")
async def get_marks(request: Request):
    names = request.query_params.getlist("name")
    marks = [student_marks.get(name, None) for name in names]
    return {"marks": marks}
