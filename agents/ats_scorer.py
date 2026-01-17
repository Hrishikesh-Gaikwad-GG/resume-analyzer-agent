def ats_score(state):
    total = len(state['matched_skills']) + len(state['missing_skills'])
    score = int((len(state['matched_skills']) / max(total, 1)) * 100)

    return {
        **state,
        'ats_score': score
    }