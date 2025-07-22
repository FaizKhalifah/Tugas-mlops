
# Gunakan base image yang ringan

# 225150207111069_Raihan Fadhillah Baihaqi 			
# 225150207111075_Hernando Atha 				
# 225150207111066_Muhammad Alfaiz Khalifah Alamsyah 	
# 225150200111034_Qyan Rommy Mario				
# 225150201111029_Davin Dalana Fidelio Fredra	

# Gunakan base image Python

FROM python:3.10-slim

# Atur environment variable agar tidak buffering (baik untuk log)
ENV PYTHONUNBUFFERED=1

# Buat direktori kerja di dalam container
WORKDIR /app

# Salin file requirements terlebih dahulu (agar caching lebih efisien)
COPY requirements.txt .

# Install dependencies (lebih efisien pakai --upgrade pip dulu)
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Salin seluruh project ke dalam container
COPY . .

# Jika aplikasi utama di app/app.py
CMD ["python", "app/app.py"]
