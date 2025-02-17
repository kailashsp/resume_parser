from pydantic import BaseModel, Field, create_model
from typing import List

class ResumeCriteria(BaseModel):
    criteria: List[str]

class CriteriaScore(BaseModel):
    criteria_type : int
    
class ResumeScoring(BaseModel):
    candidate_name : str
    critertia_score : List[CriteriaScore]

def create_dynamic_resume_scoring_model(criteria):
    fields = {
        "candidate_name": (str, Field())
    }
    print(criteria)
    for criterion in criteria:
        fields[criterion] = (int, Field())
    
    fields["total_score"] = (int, Field())
    
    return create_model("DynamicResumeScoringModel", **fields)
