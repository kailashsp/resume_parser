from app.utils.llm_integration import LLM
from app.models import create_dynamic_resume_scoring_model, ResumeCriteria, ResumeScoring

llm_inst = LLM(model_name="gemini")

async def score_resume_with_llm(resume, criteria):
    response_schema = create_dynamic_resume_scoring_model(criteria)
    prompt = f"""Create a resume scoring system that evaluate the candidate based on the following criteria: 

  {criteria}
     
    {resume}
analyze the content and assign a score from 1 to 5 for each criterion, where 1 is the lowest and 5 is the highest. Then, calculate the total score by summing up the individual criterion scores. 
replace the criteria type with the given criteria
"""
    import json
    response = await llm_inst(prompt, response_schema)
    print(json.loads(response))
    return response

async def extract_criteria_with_llm(text):
    response_schema= ResumeCriteria
    prompt = "Generate the criteria to be evaluated for the job description"
    criteria = await llm_inst(prompt + text, response_schema)
    return criteria
    
    