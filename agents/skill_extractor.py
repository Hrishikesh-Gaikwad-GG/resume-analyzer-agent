from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature = 0)

prompt = PromptTemplate(
    input_variables=["resume_text"],
    template="""
    Extract all technical skills, tools, frameworks, and programming languages
    from the resume below.

    Return ONLY a comma-separated string.

    Resume:
    {resume_text}
    """
)

def extract_skills(state):

    response = llm.invoke(prompt.format(resume_text = state['resume_text']))

    skills = [s.strip() for s in response.content.split(', ') if s.strip()]

    return {'skills': skills}