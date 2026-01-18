import sys
# print(sys.path)
import streamlit as st
import tempfile
import os
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR))
# print(sys.path)

from graph.resume_graph import resume_graph

st.set_page_config(
    page_title = 'Resume Analyzer Agent',
    layout = 'centered'
)

st.title('Resume Analyzer Agent')
st.caption('LangGraph-powered ATS & Resume Feedback System')


uploaded_file = st.file_uploader(
    "Upload your resume (PDF only)",
    type = ['pdf']
)

job_description = st.text_area(
    "Paste the Job Description",
    height = 200,
    placeholder = "Looking for a Python developer with FastAPI, Docker, AWS..."
)

analyze_button = st.button('Analyze Resume')

if analyze_button:
    if uploaded_file is None or not job_description.strip():
        st.warning('Please upload a resume and provide a job description.')

    else:

        with st.spinner('Analyzing resume...'):
            
            with tempfile.NamedTemporaryFile(delete = False, suffix = '.pdf') as tmp:
                tmp.write(uploaded_file.read())
                resume_path = tmp.name

            result = resume_graph.invoke({
                'resume_path': resume_path,
                'job_description': job_description
            })

            os.remove(resume_path)


        st.success("Analysis Complete...")

        st.subheader('ATS Score')
        st.metric(label = 'Score', value = f'{result['ats_score']}%')

        col1, col2 = st.columns(2)


        with col1:
            st.subheader('Matched skills')
            if result['matched_skills']:
                for skill in result['matched_skills']:
                    st.markdown(f'- {skill}')

            else:
                st.write('No matched skill found.')


        with col2:
            st.subheader("Missing skills")
            if result['missing_skills']:
                for skill in result['missing_skills']:
                    st.markdown(f'- {skill}')


            else:
                st.write('No missing skills')


        
        st.subheader("Resume Improvement Feedback")
        st.write(result['feedback'])