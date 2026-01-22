# Step 1: Use a lightweight Python base image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Step 4: Copy the rest of your app code
COPY app.py .

# Step 5: Expose the port Flask runs on
EXPOSE 8080

# Step 6: Start the app
CMD ["python", "app.py"]
