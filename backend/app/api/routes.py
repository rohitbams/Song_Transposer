from fastapi import APIRouter, UploadFile, Form, HTTPException
from app.utils.youtube import download_youtube_audio
from app.services.key_detection import detect_key
from app.services.transposer import transpose_audio

router = APIRouter()

@router.post("/download")
def download_route(youtube_url: str = Form(...)):
    """
    Download audio from a YouTube video and return the local file path.
    """
    try:
        file_path = download_youtube_audio(youtube_url)
        return {"status": "success", "file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/analyse")
def analyze_route(file_path: str = Form(...)):
    """
    Analyse the given audio file and return the detected key.
    """
    result = detect_key(file_path)
    return result

@router.post("/transpose")
def transpose_route(
    file_path: str = Form(...),
    original_key: str = Form(...),
    target_key: str = Form(...)
):
    """
    Transpose an audio file from original_key to target_key.
    """
    try:
        output_file = transpose_audio(file_path, original_key, target_key)
        return {"status": "success", "file_path": output_file}
    except Exception as e:
        return {"status": "error", "message": str(e)}