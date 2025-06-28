# backend/utils.py

from pathlib import Path
import uuid
import aiofiles
from fastapi import UploadFile

async def save_upload_file(upload_file: UploadFile, destination_folder: Path) -> Path:
    """
    Simpan UploadFile FastAPI ke disk secara asinkron dan kembalikan path lengkapnya.

    Args:
        upload_file (UploadFile): File yang diunggah dari request.
        destination_folder (Path): Folder tujuan untuk menyimpan file.

    Returns:
        Path: Path lengkap ke file yang baru disimpan.
    """
    try:
        file_extension = Path(upload_file.filename).suffix
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        destination_path = destination_folder / unique_filename

        async with aiofiles.open(destination_path, "wb") as out_file:
            while content := await upload_file.read(1024):  
                await out_file.write(content)

        return destination_path
    except Exception as e:
        print(f"Error saat menyimpan file: {e}")
        return None