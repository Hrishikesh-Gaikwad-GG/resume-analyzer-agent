from typing import TypedDict, List, Optional

class ResumeState(TypedDict):
    resume_text: str
    skills: List[str]
    matched_skills: List[str]
    missing_skills: List[str]
    ats_score: Optional[int]
    feedback: Optional[str]
    job_description: str
    resume_path: str

    