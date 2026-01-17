from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import json
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature = 0)

prompt = PromptTemplate(
    input_variables=["skills", "job_description"],
    template="""
    Given the candidate skills and job description,
    identify:
    1. matched_skills
    2. missing_skills

    Skills: {skills}
    Job Description: {job_description}

    Return JSON with keys matched_skills and missing_skills.
    """
)

def match_job(state):
    response = llm.invoke(
        prompt.format(
            skills = ', '.join(state['skills']),
            job_description = state['job_description']
        )
    )

    data = json.loads(response.content)

    return {
        **state,
        'matched_skills': data['matched_skills'],
        'missing_skills': data['missing_skills']
    }

