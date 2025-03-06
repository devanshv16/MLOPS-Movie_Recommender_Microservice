# Use the official Python image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy all project files into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI default port
EXPOSE 8000

# Run the FastAPI app (correcting the module path)
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]