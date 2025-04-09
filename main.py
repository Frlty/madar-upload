from fastapi import FastAPI, File, UploadFile, Form
import shutil
import os

app = FastAPI()
@app.api_route("/", methods=["GET", "POST", "HEAD", "OPTIONS"])
async def root_test():
    return {"message": "Server is alive", "status": "ok"}

@app.post("/upload/")
async def upload_file(
    image: UploadFile = File(...),
    latitude: float = Form(...),
    longitude: float = Form(...),
    timestamp: str = Form(None)
):
    os.makedirs("uploads", exist_ok=True)
    filepath = f"uploads/{image.filename}"
    with open(filepath, "wb") as f:
        shutil.copyfileobj(image.file, f)

    return {
        "status": "success",
        "filename": image.filename,
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": timestamp
    }
