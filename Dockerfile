<<<<<<< HEAD
# Use Python 3.11 slim image for Hugging Face Spaces
FROM python:3.11-slim
=======
# Use Python 3.12 slim image
FROM python:3.12-slim
>>>>>>> 93950817c04823890ebb69d631bbdf19b522c613

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

<<<<<<< HEAD
# Expose port for Hugging Face Spaces
EXPOSE 7860

# Environment variables for Hugging Face
ENV PYTHONPATH=/app
ENV CHAINLIT_HOST=0.0.0.0
ENV CHAINLIT_PORT=7860

# Run the application
CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "7860"]
=======
# Create non-root user for security
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Expose port for Chainlit
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run the application
CMD ["chainlit", "run", "app.py", "--host", "0.0.0.0", "--port", "8080"]
>>>>>>> 93950817c04823890ebb69d631bbdf19b522c613
