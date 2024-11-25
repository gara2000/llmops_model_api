# Use Python 3.9 as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy model and inference script
COPY model.joblib app.py /app/

# Install dependencies
RUN pip install --no-cache-dir joblib scikit-learn numpy flask

# Expose port 8080 for Flask
EXPOSE 8080

# Run inference script using Flask
CMD ["python3", "inference.py"]
