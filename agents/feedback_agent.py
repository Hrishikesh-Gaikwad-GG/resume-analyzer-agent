from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()
llm = ChatOpenAI(temperature = 0.3)

prompt = PromptTemplate(
    input_variables = ['missing_skills', 'ats_score'],
    template = '''
    The resume ATS score is {ats_score}%.
    Missing skills: {missing_skills}

    Give concise, actionalble resume improvement suggestions.
'''
)

def generate_feedback(state):
    feedback = llm.invoke(
        prompt.format(missing_skills = ', '.join(state['missing_skills']),
                      ats_score = state['ats_score']
            
        )
    )

    return {
        **state,
        'feedback': feedback.content
    }

