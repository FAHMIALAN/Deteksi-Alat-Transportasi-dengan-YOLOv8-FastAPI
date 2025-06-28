# backend/detect.py

from ultralytics import YOLO
import cv2
from moviepy.editor import ImageSequenceClip
from pathlib import Path
import numpy as np

def detect_image_in_memory(model: YOLO, image_bytes: bytes) -> bytes:
    """
    Deteksi objek pada gambar dari data bytes di memori.
    """
    try:
        np_array = np.frombuffer(image_bytes, np.uint8)
        image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

        results = model.predict(source=image, verbose=False)[0]
        annotated_frame = results.plot()
        
        is_success, buffer = cv2.imencode(".jpg", annotated_frame)
        if not is_success:
            return None
            
        return buffer.tobytes()
        
    except Exception as e:
        print(f"Error pada deteksi gambar di memori: {e}")
        return None

def detect_video(model: YOLO, video_path: Path, output_path: Path) -> str:
    """
    Fungsi deteksi video (berbasis file).
    """
    try:
        cap = cv2.VideoCapture(str(video_path))
        frames = []
        fps = cap.get(cv2.CAP_PROP_FPS)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            results = model.predict(source=frame, verbose=False)[0]
            annotated_frame = results.plot()
            annotated_frame_rgb = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
            frames.append(annotated_frame_rgb)

        cap.release()

        if not frames:
            return None

        clip = ImageSequenceClip(frames, fps=fps)
        clip.write_videofile(str(output_path), codec="libx264")
        
        return str(output_path)
    except Exception as e:
        print(f"Error pada deteksi video: {e}")
        return None
