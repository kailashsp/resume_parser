import json
from fastapi import APIRouter, File, UploadFile
from app.utils.file_processing import extract_text_from_file
from app.utils.llm_processing import extract_criteria_with_llm


router = APIRouter()

@router.post("/extract-criteria", tags=["Criteria Extraction"])
async def extract_criteria(file: UploadFile = File(...)):
    """
    Extract ranking criteria from a job description file.

    Parameters:
    - file (UploadFile): The job description file (PDF, DOCX, or TXT format)

    Returns:
    - Dict[str, List[str]]: A dictionary containing the extracted criteria
    
    Example:
        {
            "criteria": [
                "Python programming",
                "Machine learning",
                "Data analysis",
                "Communication skills"
            ]
        }
    """
    text = await extract_text_from_file(file)
    criteria = await extract_criteria_with_llm(text)
    return {"criteria": json.loads(criteria)['criteria']}

