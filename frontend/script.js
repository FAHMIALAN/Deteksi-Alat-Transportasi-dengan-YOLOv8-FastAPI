// Definisikan elemen dan URL di awal agar mudah diubah
const API_BASE_URL = "http://127.0.0.1:8000";
const uploadForm = document.getElementById("uploadForm");
const fileInput = document.getElementById("fileInput");
const modeSelect = document.getElementById("modeSelect");
const statusDiv = document.getElementById("status");
const outputImage = document.getElementById("outputImage");
const outputVideo = document.getElementById("outputVideo");

function updateStatus(message, type) {
    statusDiv.textContent = message;
    statusDiv.className = `status-${type}`; 
}

function displayResult(url, type) {
    outputImage.classList.add('hidden');
    outputVideo.classList.add('hidden');

    if (type === 'image') {
        outputImage.src = url;
        outputImage.classList.remove('hidden');
    } else {
        outputVideo.src = url;
        outputVideo.classList.remove('hidden');
    }
}

window.addEventListener("DOMContentLoaded", async () => {
    try {
        const response = await fetch(API_BASE_URL);
        const data = await response.json();
        if (data.status === "ok") {
            updateStatus("✅ Backend terhubung, siap mendeteksi!", "success");
        }
    } catch (error) {
        updateStatus("❌ Gagal terhubung ke backend. Pastikan server sudah berjalan.", "error");
    }
});

uploadForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const file = fileInput.files[0];

    if (!file) {
        updateStatus("Pilih file terlebih dahulu.", "error");
        return;
    }

    const mode = modeSelect.value;
    const endpoint = mode === "image" ? "/detect-image" : "/detect-video";
    const formData = new FormData();
    formData.append("file", file);

    updateStatus(`Mengunggah dan memproses ${mode}...`, "loading");

    try {
        const response = await fetch(API_BASE_URL + endpoint, {
            method: "POST",
            body: formData,
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.detail || "Gagal memproses file di server.");
        }

        const blob = await response.blob();
        const objectURL = URL.createObjectURL(blob);
        
        displayResult(objectURL, mode);
        updateStatus(`Deteksi ${mode} berhasil!`, "success");

    } catch (error) {
        console.error("Error:", error);
        updateStatus(`Error: ${error.message}`, "error");
    }
});