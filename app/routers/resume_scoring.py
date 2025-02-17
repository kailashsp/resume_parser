from fastapi import APIRouter, File, UploadFile,  Query
from typing import List
from fastapi.responses import StreamingResponse
from app.utils.file_processing import extract_text_from_file
from app.utils.llm_processing import score_resume_with_llm
import pandas as pd
from io import BytesIO
import json

router = APIRouter()

@router.post("/score-resumes", tags=["Resume Scoring"])
async def score_resumes(
    criteria: List[str] = Query(..., description="List of criteria to score against"),
    files: List[UploadFile] = File(...)
):
    """
    Score multiple resumes against given criteria.

    Parameters:
    - criteria (List[str]): List of criteria to score the resumes against
    - files (List[UploadFile]): List of resume files (PDF, DOCX, or TXT format)

    Returns:
    - StreamingResponse: An Excel file containing the scores

    The Excel file will have the following columns:
    - candidate_name: Name of the candidate
    - [criteria]: One column for each criterion, containing the score
    - total_score: The total score for the candidate

    Example query:
    ```
    POST /score-resumes?criteria=Python&criteria=Machine%20Learning&criteria=Communication
    ```

    Note: The response is a downloadable Excel file.
    """
    results = []
    for file in files:
        text = await extract_text_from_file(file)
        score_response = await score_resume_with_llm(text, criteria)
        score_response_json = json.loads(score_response)
        results.append({
            "candidate_name": score_response_json['candidate_name'],
            **{crit: score for crit, score in score_response_json.items() if crit not in {'candidate_name','total_score'}},
            "total_score": score_response_json["total_score"]
        })
    
    df = pd.DataFrame(results)
    output = BytesIO()
    df.to_excel(output, index=False)
    output.seek(0)
    
    return StreamingResponse(
        output,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={"Content-Disposition": "attachment; filename=scores.xlsx"}
    )