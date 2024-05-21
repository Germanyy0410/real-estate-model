# Sử dụng một base image có Python và Flask
FROM python:3.9-slim

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép các file requirements.txt và cài đặt các dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ nội dung vào thư mục làm việc
COPY . .

# Expose port mà Flask sẽ chạy
EXPOSE 5000

# Lệnh để chạy ứng dụng Flask
CMD ["python", "server.py"]
