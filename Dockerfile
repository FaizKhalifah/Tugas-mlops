# Gunakan base image Python
FROM python:3.10-slim

# Buat workdir
WORKDIR /app

# Salin semua isi project ke dalam container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Jalankan aplikasi
CMD ["python", "app/app.py"]
