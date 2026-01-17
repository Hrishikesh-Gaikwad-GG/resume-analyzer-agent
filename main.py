from graph.resume_graph import resume_graph


result = resume_graph.invoke({
        "resume_path": "resume.pdf",
        "job_description": "Looking for a Python developer with FastAPI, Docker, AWS"
    })

print(result["ats_score"])
print(result["feedback"])