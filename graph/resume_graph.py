from langgraph.graph import StateGraph
from graph.state import ResumeState

from agents.resume_parser import parse_resume
from agents.skill_extractor import extract_skills
from agents.job_matcher import match_job
from agents.ats_scorer import ats_score
from agents.feedback_agent import generate_feedback

graph = StateGraph(ResumeState)

graph.add_node('parse_resume', parse_resume)
graph.add_node('extract_skills', extract_skills)
graph.add_node('match_job', match_job)
graph.add_node('ats_score', ats_score)
graph.add_node('feedback', generate_feedback)

graph.set_entry_point('parse_resume')

graph.add_edge('parse_resume', 'extract_skills')
graph.add_edge('extract_skills', 'match_job')
graph.add_edge('match_job', 'ats_score')
graph.add_edge('ats_score', 'feedback')

resume_graph = graph.compile()


if __name__ == '__main__':


    result = resume_graph.invoke({
        "resume_path": "resume.pdf",
        "job_description": "Looking for a Python developer with FastAPI, Docker, AWS"
    })

    print(result["ats_score"])
    print(result["feedback"])

