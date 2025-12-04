# Gunakan base image Python yang ringan
FROM python:3.10-slim

# Set working directory di dalam container
WORKDIR /app

# Copy requirements terlebih dahulu (untuk caching layer docker)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy seluruh sisa kode ke dalam container
COPY . .

# Perintah yang dijalankan ketika container dimulai
CMD ["python", "train.py"]
