# backend/main.py

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse, Response # Import Response untuk in-memory
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path
import uvicorn
from ultralytics import YOLO

# --- Import fungsi dari file lain di dalam package 'backend' ---
# Kita akan pakai fungsi 'in-memory' untuk gambar
from .detect import detect_image_in_memory, detect_video
from .utils import save_upload_file

# --- Inisialisasi Aplikasi dan Path ---
app = FastAPI(title="YOLOv8 Transport Detector")

# Tentukan path absolut untuk manajemen file yang andal
BASE_DIR = Path(__file__).resolve().parent
UPLOADS_DIR = BASE_DIR / "uploads"
RESULTS_DIR = BASE_DIR / "results"
WEIGHTS_DIR = BASE_DIR.parent / "yolov8_weights"

# Buat direktori yang diperlukan saat aplikasi dimulai
UPLOADS_DIR.mkdir(exist_ok=True)
RESULTS_DIR.mkdir(exist_ok=True)

# --- Muat Model YOLOv8 (Hanya sekali saat startup) ---
model_path = WEIGHTS_DIR / "yolov8s.pt"
if not model_path.exists():
    raise FileNotFoundError(f"File model tidak ditemukan di {model_path}. Harap download dan letakkan di sana.")
model = YOLO(model_path)
print("✅ Model YOLOv8 berhasil dimuat.")

# --- Konfigurasi CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Endpoints API ---
@app.get("/")
def read_root():
    return {"status": "ok", "message": "Backend YOLOv8 aktif 🚀"}

@app.post("/detect-image")
async def detect_image_route(file: UploadFile = File(...)):

    image_bytes = await file.read()
    
    result_bytes = detect_image_in_memory(model, image_bytes)
    
    if not result_bytes:
        raise HTTPException(status_code=500, detail="Gagal memproses deteksi gambar.")

    return Response(content=result_bytes, media_type="image/jpeg")

@app.post("/detect-video")
async def detect_video_route(file: UploadFile = File(...)):
    uploaded_path = await save_upload_file(file, UPLOADS_DIR)
    if not uploaded_path:
        raise HTTPException(status_code=500, detail="Gagal menyimpan file.")

    output_path = RESULTS_DIR / (uploaded_path.stem + ".mp4")
    result_file = detect_video(model, uploaded_path, output_path)

    if not result_file:
        raise HTTPException(status_code=500, detail="Gagal memproses deteksi video.")
        
    return FileResponse(result_file, media_type="video/mp4")

if __name__ == "__main__":
    print("🚀 Menjalankan backend di http://127.0.0.1:8000")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True, app_dir="backend")

