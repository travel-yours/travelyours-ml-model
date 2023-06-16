# Menggunakan image base python
FROM python:3.9

# Set working directory di dalam container
WORKDIR /app

# Menyalin requirements.txt ke dalam container
COPY requirements.txt .

# Menginstall dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Menyalin seluruh kode aplikasi ke dalam container
COPY . .

EXPOSE 8080
# Menjalankan aplikasi Python
CMD ["python", "app.py"]
