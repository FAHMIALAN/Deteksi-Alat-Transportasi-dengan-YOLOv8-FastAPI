# Deteksi Alat Transportasi dengan YOLOv8 & FastAPI

📖 Ringkasan Proyek
Proyek ini adalah sebuah aplikasi web full-stack yang mampu mendeteksi berbagai jenis alat transportasi (seperti mobil, motor, bus) dari gambar atau video yang diunggah oleh pengguna.

Aplikasi ini dibangun dengan arsitektur modern yang memisahkan antara backend (logika AI) dan frontend (tampilan pengguna), di mana keduanya berkomunikasi melalui REST API.

🛠️ Teknologi yang Digunakan
Backend
Python 3.10+

FastAPI: Framework web asinkron untuk membangun API yang cepat dan efisien.

Uvicorn: Server ASGI untuk menjalankan aplikasi FastAPI.

YOLOv8 (Ultralytics): Model deep learning canggih untuk deteksi objek secara real-time.

OpenCV-Python: Library untuk pemrosesan gambar dan frame video.

MoviePy: Library untuk merangkai kembali frame video yang telah diproses.

Frontend
HTML5

CSS3

JavaScript (ES6+): Untuk interaktivitas, menangani upload file, dan menampilkan hasil secara dinamis.

Bootstrap 5: Framework CSS untuk membangun antarmuka yang modern dan responsif dengan cepat.

Bootstrap Icons: Untuk mempercantik tampilan dengan ikon.

📁 Struktur Proyek
Struktur folder proyek diatur agar rapi dan mudah dikelola, memisahkan antara logika backend, tampilan frontend, dan aset model.

transport_detector/
├── .venv/                   # (Dibuat lokal, tidak di-upload) Folder virtual environment
│
├── backend/                 # Semua logika sisi server
│   ├── __init__.py
│   ├── main.py              # File utama API (FastAPI)
│   ├── detect.py            # Logika deteksi objek dengan YOLOv8
│   ├── utils.py             # Fungsi-fungsi pembantu
│   └── uploads/             # (Dibuat otomatis) Tempat menyimpan video asli
│   └── results/             # (Dibuat otomatis) Tempat menyimpan video hasil
│
├── frontend/                # Semua file antarmuka pengguna
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── yolov8_weights/          # Tempat menyimpan file model .pt
│   └── yolov8s.pt
│
├── .gitignore               # Daftar file/folder yang diabaikan oleh Git
│
└── requirements.txt         # Daftar semua package Python yang dibutuhkan

🚀 Cara Menjalankan Proyek
Ikuti langkah-langkah berikut untuk menjalankan proyek ini di komputermu.

1. Persiapan Awal
Pastikan kamu sudah menginstal Python 3.10 atau versi yang lebih baru.

Download atau clone repositori ini ke komputermu:

git clone https://github.com/FAHMIALAN/Deteksi-Alat-Transportasi-dengan-YOLOv8-FastAPI.git
cd Deteksi-Alat-Transportasi-dengan-YOLOv8-FastAPI

2. Setup Backend
Buka terminal di folder utama proyek, lalu jalankan perintah berikut secara berurutan:

# 1. Buat dan aktifkan virtual environment
# Di Windows:
python -m venv .venv
.\.venv\Scripts\activate

# Di macOS/Linux:
# python3 -m venv .venv
# source .venv/bin/activate

# 2. Install semua package yang dibutuhkan dari daftar belanjaan
pip install -r requirements.txt

# 3. Download file model YOLOv8 (jika belum ada)
# Pastikan file 'yolov8s.pt' sudah ada di dalam folder 'yolov8_weights'
# Jika belum, download dari terminal dengan perintah (untuk Windows):
# Invoke-WebRequest -Uri https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8s.pt -OutFile yolov8_weights\yolov8s.pt

# 4. Jalankan server backend
uvicorn backend.main:app --reload

Server akan berjalan di http://127.0.0.1:8000. Biarkan terminal ini tetap terbuka.

3. Jalankan Frontend
Buka File Explorer.

Navigasi ke folder frontend.

Klik dua kali pada file index.html untuk membukanya di browser.

Aplikasi sekarang siap digunakan!

🔌 Endpoint API
GET /: Endpoint health-check untuk memastikan backend aktif.

POST /detect-image: Menerima file gambar, melakukan deteksi, dan mengembalikan hasil gambar secara langsung (in-memory).

POST /detect-video: Menerima file video, melakukan deteksi, dan mengembalikan file video hasil.

💡 Potensi Pengembangan
Model Kustom dengan Roboflow: Melatih model YOLOv8 dengan dataset kustom (misalnya, untuk mendeteksi angkot, becak, bajaj) menggunakan Roboflow untuk meningkatkan akurasi dan relevansi deteksi di Indonesia.

Deteksi Real-time dari Webcam: Menambahkan fitur untuk mendeteksi objek langsung dari input webcam pengguna.

Progress Bar untuk Video: Menampilkan progress bar yang lebih informatif saat memproses video, karena proses ini bisa memakan waktu lama.

Deployment: Men-deploy aplikasi ini ke layanan cloud seperti Heroku, Vercel, atau VPS agar bisa diakses secara online oleh siapa saja.
