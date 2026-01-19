import sys
from pathlib import Path
import tempfile
import os

from fastapi import FastAPI, UploadFile, File, Form

from fastapi.middleware.cors import CORSMiddleware


ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))

from graph.resume_graph import resume_graph

app = FastAPI(
    title='Resume Analyzer Agent API',
    description = "LangGraph - powered Resume ATS and Feedback API",
    version = "1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def health():
    return {"Status": 'ok'}

@app.post('/analyze')
async def analyze_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...)
):
    with tempfile.NamedTemporaryFile(delete = False, suffix = '.pdf') as tmp:
        content = await resume.read()
        tmp.write(content)
        resume_path = tmp.name

    try:

        result = resume_graph.invoke({
            'resume_path': resume_path,
            'job_description': job_description
        })

        return {
            "ats_score": result["ats_score"],
            "matched_skills": result["matched_skills"],
            "missing_skills": result["missing_skills"],
            "feedback": result["feedback"]
        }
    finally:
        os.remove(resume_path)