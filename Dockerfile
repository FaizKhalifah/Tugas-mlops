# 225150207111069_Raihan Fadhillah Baihaqi 			
# 225150207111075_Hernando Atha 				
# 225150207111066_Muhammad Alfaiz Khalifah Alamsyah 	
# 225150200111034_Qyan Rommy Mario				
# 225150201111029_Davin Dalana Fidelio Fredra	

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
