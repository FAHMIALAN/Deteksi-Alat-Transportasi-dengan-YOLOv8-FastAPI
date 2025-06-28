# 🚗 Deteksi Alat Transportasi dengan YOLOv8 & FastAPI

## 📖 Ringkasan Proyek

Proyek ini adalah aplikasi web full-stack yang mampu mendeteksi berbagai jenis alat transportasi seperti **mobil**, **motor**, dan **bus** dari gambar atau video yang diunggah oleh pengguna.

Aplikasi dibangun dengan arsitektur modern yang memisahkan antara backend (logika AI) dan frontend (tampilan pengguna), keduanya terhubung melalui REST API.

---

## 🛠️ Teknologi yang Digunakan

### 🔙 Backend
- **Python 3.10+**
- **FastAPI** – Framework web asinkron untuk membangun API yang cepat dan efisien.
- **Uvicorn** – Server ASGI untuk menjalankan aplikasi FastAPI.
- **YOLOv8 (Ultralytics)** – Model deep learning canggih untuk deteksi objek real-time.
- **OpenCV-Python** – Library untuk pemrosesan gambar dan frame video.
- **MoviePy** – Untuk merangkai kembali frame video yang telah diproses.

### 🌐 Frontend
- **HTML5**
- **CSS3**
- **JavaScript (ES6+)** – Untuk interaktivitas, upload file, dan tampilan hasil.
- **Bootstrap 5** – Framework CSS untuk UI responsif dan modern.
- **Bootstrap Icons** – Untuk menambahkan ikon yang menarik.

---

## 📁 Struktur Proyek

Struktur folder proyek diatur dengan rapi untuk memisahkan antara backend, frontend, dan aset model:

```
transport_detector/
├── .venv/                  # Virtual environment lokal (tidak diupload)
│
├── backend/                # Semua logika sisi server
│   ├── __init__.py
│   ├── main.py             # File utama API (FastAPI)
│   ├── detect.py           # Logika deteksi objek dengan YOLOv8
│   ├── utils.py            # Fungsi-fungsi pembantu
│   ├── uploads/            # (Dibuat otomatis) Tempat menyimpan video asli
│   └── results/            # (Dibuat otomatis) Tempat menyimpan video hasil
│
├── frontend/               # Semua file antarmuka pengguna
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── yolov8_weights/         # Tempat menyimpan file model .pt
│   └── yolov8s.pt
│
├── .gitignore              # Daftar file/folder yang diabaikan oleh Git
└── requirements.txt        # Daftar semua package Python yang dibutuhkan
```

---

## 🚀 Cara Menjalankan Proyek

### 1. Persiapan Awal

Pastikan kamu sudah menginstal **Python 3.10 atau lebih baru**.

Clone repositori ini ke komputermu:

```bash
git clone https://github.com/FAHMIALAN/Deteksi-Alat-Transportasi-dengan-YOLOv8-FastAPI.git
cd Deteksi-Alat-Transportasi-dengan-YOLOv8-FastAPI
```

---

### 2. Setup Backend

Buka terminal di folder utama proyek, lalu jalankan perintah berikut:

```bash
# 1. Buat dan aktifkan virtual environment
# Di Windows:
python -m venv .venv
.venv\Scripts\activate

# Di macOS/Linux:
# python3 -m venv .venv
# source .venv/bin/activate

# 2. Install semua dependencies
pip install -r requirements.txt

# 3. Pastikan model YOLOv8 sudah tersedia
# Jika belum ada, download model:
# (Untuk Windows PowerShell)
Invoke-WebRequest -Uri https://github.com/ultralytics/assets/releases/download/v8.2.0/yolov8s.pt -OutFile yolov8_weights\yolov8s.pt

# 4. Jalankan server backend
uvicorn backend.main:app --reload
```

Server akan berjalan di: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Biarkan terminal ini tetap terbuka.

---

### 3. Jalankan Frontend

- Buka File Explorer.
- Navigasi ke folder `frontend/`.
- Klik dua kali pada file `index.html` untuk membukanya di browser.

Aplikasi sekarang siap digunakan!

---

## 🔌 Endpoint API

| Metode | Endpoint         | Deskripsi                                                                 |
|--------|------------------|--------------------------------------------------------------------------|
| GET    | `/`              | Health-check untuk memastikan backend aktif.                            |
| POST   | `/detect-image`  | Menerima file gambar, melakukan deteksi, dan mengembalikan hasil gambar. |
| POST   | `/detect-video`  | Menerima file video, melakukan deteksi, dan mengembalikan file video hasil.|

---

## 💡 Potensi Pengembangan

- **Model Kustom dengan Roboflow**  
  Melatih model YOLOv8 menggunakan dataset lokal (angkot, becak, bajaj) untuk deteksi yang lebih relevan di Indonesia.

- **Deteksi Real-time dari Webcam**  
  Menambahkan fitur deteksi langsung dari input webcam pengguna.

- **Progress Bar saat Proses Video**  
  Menampilkan indikator progress saat video sedang diproses.

- **Deployment ke Cloud**  
  Men-deploy aplikasi ke platform seperti Heroku, Vercel, Render, atau VPS agar dapat diakses online.

---

## 🤝 Kontribusi

Pull request sangat terbuka!  
Silakan fork proyek ini dan ajukan PR untuk penambahan fitur atau perbaikan bug.

---

## 📄 Lisensi

Proyek ini berada di bawah lisensi **MIT**.  
Silakan digunakan, dimodifikasi, dan disebarluaskan secara bebas sesuai kebutuhan.

---
